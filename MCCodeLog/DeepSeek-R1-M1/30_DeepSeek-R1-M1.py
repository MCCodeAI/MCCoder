
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free existing buffer for channel 10
Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
sleep(0.1)

# Create path interpolation buffer with 1000 points
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code: ' + str(ret) + ' - ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure path interpolation parameters
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 0)
conf.SetAxis(1, 1)
conf.compositeVel = 1500
conf.compositeAcc = 20000
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error: ' + str(ret) + ' - ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Create path command with 4 points
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

# Point 1: (50, 0) with radius 2.5
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 2.5
path.SetPoint(0, point)

# Point 2: (50, 50) with radius 5
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 5
path.SetPoint(1, point)

# Point 3: (0, 50) with radius 10
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 10
path.SetPoint(2, point)

# Point 4: (0, 0) no smoothing
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
path.SetPoint(3, point)

# Add commands to buffer
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error: ' + str(ret) + ' - ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start motion execution
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error: ' + str(ret) + ' - ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for motion completion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error: ' + str(ret) + ' - ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer resources
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error: ' + str(ret) + ' - ' + Wmx3Lib_adv.ErrorToString(ret))
    return
