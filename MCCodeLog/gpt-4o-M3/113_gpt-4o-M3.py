
# Axes = [3, 5]

# Task 1: Path Interpolation with Look-Ahead
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing buffer for look-ahead channel 10
Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)

# Allocate buffer memory for path interpolation with look-ahead channel 10
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set configuration for path interpolation with look-ahead channel 10
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

# Add interpolation commands to the path interpolation with look-ahead channel
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4

# Define points with smooth radius
points = [
    (50, 0, 12),
    (50, 50, 12),
    (0, 50, 12),
    (0, 0, 12)
]

for i, (x, y, radius) in enumerate(points):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 5)
    point.linear.SetTarget(0, x)
    point.linear.SetTarget(1, y)
    point.linear.smoothRadius = radius
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Start the motion for the path interpolation with look-ahead channel
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for path interpolation with look-ahead channel
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Task 2: Cubic Spline Motion Command
# Allocate buffer memory for a spline execution channel
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 3)
splineCommand.SetAxis(1, 5)
splineCommand.totalTimeMilliseconds = 1000

# Define spline points
splinePoints = [
    (0, 0),
    (10, 10),
    (-20, -20),
    (30, 30),
    (-40, -40),
    (50, 50),
    (-60, -60),
    (70, 70),
    (-80, -80)
]

splinePoint = []
for x, y in splinePoints:
    pt = AdvMotion_SplinePoint()
    pt.SetPos(0, x)
    pt.SetPos(1, y)
    splinePoint.append(pt)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(splinePoints), splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the spline execution channel
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Task 3: Synchronous Control and Motion
# Establish synchronous control between master axis 3 and slave axis 5
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(3, 5)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 3 to position 120
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

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 3 to position 240
posCommand.target = 240
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Release the synchronization
ret = Wmx3Lib_cm.sync.ResolveSync(5)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 4: PVT Interpolation Command
pvti = Motion_PVTIntplCommand()

# Define PVT points for a circle
import math

circle_points = 20
radius = 50
center_x = -50
center_y = 0
velocity = 100
time_increment = 100

pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, circle_points)
pvti.SetPointCount(1, circle_points)

for i in range(circle_points):
    angle = 2 * math.pi * i / circle_points
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    time = i * time_increment

    pvtparameter0 = Motion_PVTPoint()
    pvtparameter1 = Motion_PVTPoint()

    pvtparameter0.pos = x
    pvtparameter0.velocity = velocity
    pvtparameter0.timeMilliseconds = time

    pvtparameter1.pos = y
    pvtparameter1.velocity = velocity
    pvtparameter1.timeMilliseconds = time

    pvti.SetPoints(0, i, pvtparameter0)
    pvti.SetPoints(1, i, pvtparameter1)

ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
