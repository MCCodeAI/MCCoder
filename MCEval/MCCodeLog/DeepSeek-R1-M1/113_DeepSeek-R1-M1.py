
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Task 1: Path interpolation with look-ahead channel 10
Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)

sleep(0.1)

ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 1500
conf.compositeAcc = 10000
conf.sampleDistance = 100
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

# Define path points with smooth radius
points = [(50, 0), (50, 50), (0, 50), (0, 0)]
smooth_radii = [12, 0, 0, 0]

for i in range(4):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 5)
    point.linear.SetTarget(0, points[i][0])
    point.linear.SetTarget(1, points[i][1])
    if smooth_radii[i] > 0:
        point.linear.smoothRadius = smooth_radii[i]
    path.SetPoint(i, point)

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
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 2: Cubic spline motion
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 3)
splineCommand.SetAxis(1, 5)
splineCommand.totalTimeMilliseconds = 1000

splinePoint = []
points = [(0, 0), (10, 10), (-20, -20), (30, 30), (-40, -40), (50, 50), (-60, -60), (70, 70), (-80, -80)]
for i, (x, y) in enumerate(points):
    splinePoint.append(AdvMotion_SplinePoint())
    splinePoint[i].SetPos(0, x)
    splinePoint[i].SetPos(1, y)

ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(points), splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 3: Synchronous control
sync = AdvSync_SyncData()
sync.masterAxis = 3
sync.slaveAxis = 5
sync.type = AdvSync_SyncType.Position
sync.ratio = 1.0

ret = Wmx3Lib_adv.advSync.StartSync(0, sync)
if ret != 0:
    print('StartSync error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

posCommand.target = 240
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

ret = Wmx3Lib_adv.advSync.StopSync(0)
if ret != 0:
    print('StopSync error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Task 4: PVT interpolation
pvtCommand = AdvMotion_PVTCommand()
pvtCommand.axisCount = 2
pvtCommand.SetAxis(0, 3)
pvtCommand.SetAxis(1, 5)
pvtCommand.numPoints = 20

theta = 0
time = 0
for i in range(20):
    x = -50 + 50 * cos(theta)
    y = 0 + 50 * sin(theta)
    
    pvtPoint = AdvMotion_PVTPoint()
    pvtPoint.SetPos(0, x)
    pvtPoint.SetPos(1, y)
    pvtPoint.SetVel(0, 100)
    pvtPoint.SetVel(1, 100)
    pvtPoint.time = time
    
    pvtCommand.SetPoint(i, pvtPoint)
    
    theta += 2 * pi / 20
    time += 100

ret = Wmx3Lib_adv.advMotion.StartPVT(pvtCommand)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
