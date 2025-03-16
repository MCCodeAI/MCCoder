
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

from time import sleep

# Create an instance of AdvancedMotion using the Wmx3Lib handle
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation with look ahead buffer on channel 0
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create a new path interpolation with look ahead buffer on channel 0 with a buffer size of 1000
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with look ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
# In the command we follow the order specified in the question (Axis 9 then Axis 6),
# even though the header comment lists axes sorted in ascending order.
conf.SetAxis(0, 9)
conf.SetAxis(1, 6)
conf.compositeVel = 2000
conf.compositeAcc = 2000
conf.sampleDistance = 50
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Prepare the path interpolation command with look ahead
path = AdvMotion_PathIntplLookaheadCommand()
# There are five points in the motion path.
path.numPoints = 5

# First point: (200, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 9)  # Axis 9 gets 200
point.linear.SetAxis(1, 6)  # Axis 6 gets 0
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 0)
path.SetPoint(0, point)

# Second point: (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 9)  # Axis 9 remains 200
point.linear.SetAxis(1, 6)  # Axis 6 becomes 200
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
path.SetPoint(1, point)

# Third point: (0, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 9)  # Axis 9 moves to 0
point.linear.SetAxis(1, 6)  # Axis 6 remains at 200
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 200)
path.SetPoint(2, point)

# Fourth point: (0, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 9)  # Axis 9 stays 0
point.linear.SetAxis(1, 6)  # Axis 6 moves to 0
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
path.SetPoint(3, point)

# Fifth point: (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 9)  # Axis 9 moves to 200
point.linear.SetAxis(1, 6)  # Axis 6 moves to 200
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
path.SetPoint(4, point)

# Add the complete path interpolation command to channel 0
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Start executing the path interpolation with look ahead on channel 0
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Since this is a continuous path interpolation command,
# we only wait for the overall motion to complete after starting the interpolation.
# Here we wait until one of the axes (Axis 9) stops moving.
Wmx3Lib_cm.motion.Wait(9)

# Optionally, poll the path interpolation status until it reaches the Stopped state.
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('PathIntplLookahead Running timeout.!')
        exit()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

# Free the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
