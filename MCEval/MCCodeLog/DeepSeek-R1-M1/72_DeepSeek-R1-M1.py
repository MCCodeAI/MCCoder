
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplLookaheadCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    
# Create the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()

conf.axisCount = 2
conf.SetAxis(0, 2)
conf.SetAxis(1, 7)
conf.compositeVel = 2200
conf.compositeAcc = 10000
conf.sampleDistance = 50
conf.stopOnEmptyBuffer = True
conf.setAngleTolerance = True
conf.angleToleranceDegrees = 11

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look ahead commands
path.numPoints = 5

# Segment 1: Line to (50, 0)
point1 = AdvMotion_PathIntplLookaheadCommandPoint()
point1.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point1.linear.axisCount = 2
point1.linear.SetAxis(0, 2)
point1.linear.SetAxis(1, 7)
point1.linear.SetTarget(0, 50)
point1.linear.SetTarget(1, 0)
path.SetPoint(0, point1)

# Segment 2: Circular to (50, 0) through (50, 100)
point2 = AdvMotion_PathIntplLookaheadCommandPoint()
point2.type = AdvMotion_PathIntplLookaheadSegmentType.Circular
point2.circular.axisCount = 2
point2.circular.SetAxis(0, 2)
point2.circular.SetAxis(1, 7)
point2.circular.SetTarget(0, 50)
point2.circular.SetTarget(1, 0)
point2.circular.SetCenterPos(0, 50)
point2.circular.SetCenterPos(1, 100)
point2.circular.SetDirection(1)  # 1 for clockwise
path.SetPoint(1, point2)

# Segment 3: Line to (100, 0)
point3 = AdvMotion_PathIntplLookaheadCommandPoint()
point3.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point3.linear.axisCount = 2
point3.linear.SetAxis(0, 2)
point3.linear.SetAxis(1, 7)
point3.linear.SetTarget(0, 100)
point3.linear.SetTarget(1, 0)
path.SetPoint(2, point3)

# Sleep for 0.5 seconds
point4 = AdvMotion_PathIntplLookaheadCommandPoint()
point4.type = AdvMotion_PathIntplLookaheadSegmentType.Sleep
point4.sleep.duration = 0.5
path.SetPoint(3, point4)

# Segment 4: Line to (150, 100)
point5 = AdvMotion_PathIntplLookaheadCommandPoint()
point5.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point5.linear.axisCount = 2
point5.linear.SetAxis(0, 2)
point5.linear.SetAxis(1, 7)
point5.linear.SetTarget(0, 150)
point5.linear.SetTarget(1, 100)
path.SetPoint(4, point5)

# Segment 5: Line to (200, 0)
point6 = AdvMotion_PathIntplLookaheadCommandPoint()
point6.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point6.linear.axisCount = 2
point6.linear.SetAxis(0, 2)
point6.linear.SetAxis(1, 7)
point6.linear.SetTarget(0, 200)
point6.linear.SetTarget(1, 0)
path.SetPoint(5, point6)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with look ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look ahead to complete
Wmx3Lib_cm.motion.Wait(2)
timeoutCounter = 0
# Wait until the path interpolation with look ahead is in Stopped state
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if (pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped):
        break
    sleep(0.1)
    timeoutCounter = timeoutCounter + 1
    if (timeoutCounter > 500):
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if (timeoutCounter > 500):
    print('PathIntplLookahead Running timeout.!')
    return
# Free the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
