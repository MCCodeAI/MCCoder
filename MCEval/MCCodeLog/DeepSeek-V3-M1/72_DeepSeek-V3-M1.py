
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplLookaheadCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
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

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look ahead commands
path.numPoints = 5

# Segment 1: Line to (50, 0)
Point1 = AdvMotion_PathIntplLookaheadCommandPoint()
Point1.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
Point1.linear.axisCount = 2
Point1.linear.SetAxis(0, 2)
Point1.linear.SetAxis(1, 7)
Point1.linear.SetTarget(0, 50)
Point1.linear.SetTarget(1, 0)
path.SetPoint(0, Point1)

# Segment 2: Circular to (50, 0) through (50, 100)
Point2 = AdvMotion_PathIntplLookaheadCommandPoint()
Point2.type = AdvMotion_PathIntplLookaheadSegmentType.Circular
Point2.circular.axisCount = 2
Point2.circular.SetAxis(0, 2)
Point2.circular.SetAxis(1, 7)
Point2.circular.SetTarget(0, 50)
Point2.circular.SetTarget(1, 0)
Point2.circular.SetCenterPos(0, 50)
Point2.circular.SetCenterPos(1, 100)
Point2.circular.SetDirection(1)  # 1 for counterclockwise, -1 for clockwise
path.SetPoint(1, Point2)

# Segment 3: Line to (100, 0)
Point3 = AdvMotion_PathIntplLookaheadCommandPoint()
Point3.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
Point3.linear.axisCount = 2
Point3.linear.SetAxis(0, 2)
Point3.linear.SetAxis(1, 7)
Point3.linear.SetTarget(0, 100)
Point3.linear.SetTarget(1, 0)
path.SetPoint(2, Point3)

# Segment 4: Sleep for 0.5 seconds
Point4 = AdvMotion_PathIntplLookaheadCommandPoint()
Point4.type = AdvMotion_PathIntplLookaheadSegmentType.Delay
Point4.delay.delayTime = 0.5
path.SetPoint(3, Point4)

# Segment 5: Line to (150, 100)
Point5 = AdvMotion_PathIntplLookaheadCommandPoint()
Point5.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
Point5.linear.axisCount = 2
Point5.linear.SetAxis(0, 2)
Point5.linear.SetAxis(1, 7)
Point5.linear.SetTarget(0, 150)
Point5.linear.SetTarget(1, 100)
path.SetPoint(4, Point5)

# Segment 6: Line to (200, 0)
Point6 = AdvMotion_PathIntplLookaheadCommandPoint()
Point6.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
Point6.linear.axisCount = 2
Point6.linear.SetAxis(0, 2)
Point6.linear.SetAxis(1, 7)
Point6.linear.SetTarget(0, 200)
Point6.linear.SetTarget(1, 0)
path.SetPoint(5, Point6)

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

# Free the path interpolation with look ahead buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
