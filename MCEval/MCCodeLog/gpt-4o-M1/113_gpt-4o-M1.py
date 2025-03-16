
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = []

# Initialize the AdvancedMotion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# 1. Start path interpolation with look-ahead for Axes 3 and 5
path = AdvMotion_PathIntplCommand()
path.SetAxis(0, 3)
path.SetAxis(1, 5)
path.enableConstProfile = 1
path.profile = Profile()
path.profile.type = ProfileType.Trapezoidal
path.profile.velocity = 1500
path.profile.acc = 10000
path.profile.dec = 10000
path.numPoints = 4

# Define points for path interpolation
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, 50)
path.SetTarget(1, 0, 0)
path.SetSmoothRadius(0, 12)

path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 1, 50)
path.SetTarget(1, 1, 50)
path.SetSmoothRadius(1, 12)

path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, 0)
path.SetTarget(1, 2, 50)
path.SetSmoothRadius(2, 12)

path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 3, 0)
path.SetTarget(1, 3, 0)

# Start path interpolation
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for path interpolation to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 3)
axes.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# 2. Start cubic spline motion command for Axes 3 and 5
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 3)
splineCommand.SetAxis(1, 5)
splineCommand.totalTimeMilliseconds = 1000

# Define spline points
splinePoint = []
points = [(0, 0), (10, 10), (-20, -20), (30, 30), (-40, -40), (50, 50), (-60, -60), (70, 70), (-80, -80)]
for i, (x, y) in enumerate(points):
    point = AdvMotion_SplinePoint()
    point.SetPos(0, x)
    point.SetPos(1, y)
    splinePoint.append(point)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(splinePoint), splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for spline motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# 3. Establish synchronous control between master axis 3 and 5
syncControl = AdvSync_SyncControl()
syncControl.masterAxis = 3
syncControl.slaveAxis = 5
ret = Wmx3Lib_adv.advSync.StartSyncControl(syncControl)
if ret != 0:
    print('StartSyncControl error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Move Axis 3 to position 120 and 240 with velocity 1000
for target in [120, 240]:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 3
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    Wmx3Lib_cm.motion.Wait(3)

# 4. Execute PVT interpolation command for Axis 3 and Axis 5
pvtCommand = AdvMotion_PVTCommand()
pvtCommand.axisCount = 2
pvtCommand.SetAxis(0, 3)
pvtCommand.SetAxis(1, 5)

# Define circle points for PVT interpolation
import math
circle_points = []
diameter = 100
center = (-50, 0)
for i in range(20):
    angle = 2 * math.pi * i / 20
    x = center[0] + (diameter / 2) * math.cos(angle)
    y = center[1] + (diameter / 2) * math.sin(angle)
    circle_points.append((x, y))

# Add PVT points
for i, (x, y) in enumerate(circle_points):
    pvtPoint = AdvMotion_PVTPoint()
    pvtPoint.SetPos(0, x)
    pvtPoint.SetPos(1, y)
    pvtPoint.SetVel(0, 100)
    pvtPoint.SetVel(1, 100)
    pvtPoint.time = (i + 1) * 100
    pvtCommand.AddPoint(pvtPoint)

# Execute PVT command
ret = Wmx3Lib_adv.advMotion.StartPVTPos(pvtCommand)
if ret != 0:
    print('StartPVTPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for PVT motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
