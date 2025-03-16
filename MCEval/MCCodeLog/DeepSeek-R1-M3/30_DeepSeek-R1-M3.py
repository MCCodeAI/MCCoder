
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
sleep(0.1)

ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

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
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 2.5
path.SetPoint(0, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 50)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 5
path.SetPoint(1, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 50)
point.linear.smoothRadius = 10
path.SetPoint(2, point)

point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 0)
point.linear.SetAxis(1, 1)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
