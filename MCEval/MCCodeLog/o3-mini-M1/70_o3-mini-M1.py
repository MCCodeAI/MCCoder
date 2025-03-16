
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

from time import sleep

# Create an instance of the advanced motion class (assumed pre-initialized Wmx3Lib)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation look-ahead buffer on channel 0
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
# Create the path interpolation with look-ahead buffer (buffer size 1000)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with look-ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
# Use index 0 for Axis 1 and index 1 for Axis 4 (sorted order)
conf.SetAxis(0, 1)
conf.SetAxis(1, 4)
conf.compositeVel = 1100
# Set the composite acceleration (use the acceleration limit given for each axis)
conf.compositeAcc = 8800
conf.stopOnEmptyBuffer = True
# Set the sample distance along the path
conf.sampleDistance = 50
# Set individual acceleration limits
conf.SetAccLimit(0, 8800)
conf.SetAccLimit(1, 8800)
# Set individual velocity limits: Axis 1 = 700, Axis 4 = 500
conf.SetVelocityLimit(0, 700)
conf.SetVelocityLimit(1, 500)

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create the path interpolation command with look-ahead
path = AdvMotion_PathIntplLookaheadCommand()
# There are five interpolation points.
path.numPoints = 5

# First point: (200, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 10
path.SetPoint(0, point)

# Second point: (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(1, point)

# Third point: (0, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(2, point)

# Fourth point: (0, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 10
path.SetPoint(3, point)

# Fifth point: (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(4, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Execute the path interpolation with look-ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the path interpolation motion to complete
timeoutCounter = 0
while True:
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
    if ret != 0:
        print('GetPathIntplLookaheadStatus error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        break
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('PathIntplLookahead Running timeout!')
        break

# Free the path interpolation with look-ahead buffer (normally done at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
