
# Axes = [3, 5]
# IOInputs = []
# IOOutputs = []

import math

# Task 1: Path interpolation with look-ahead channel 10
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free and create buffer for look-ahead channel 10
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
sleep(0.1)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
if ret != 0:
    print(f'CreatePathIntplLookaheadBuffer error: {ret}')
    exit()

# Configure look-ahead parameters
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 3)
conf.SetAxis(1, 5)
conf.compositeVel = 1500
conf.compositeAcc = 10000
conf.sampleDistance = 10
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
if ret != 0:
    print(f'SetPathIntplLookaheadConfiguration error: {ret}')
    exit()

# Add path points with smooth transitions
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 4
points = [(50, 0), (50, 50), (0, 50), (0, 0)]

for i in range(4):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 5)
    point.linear.SetTarget(0, points[i][0])
    point.linear.SetTarget(1, points[i][1])
    if i < 3:  # Apply smooth radius to first three segments
        point.linear.smoothRadius = 12
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
if ret != 0:
    print(f'AddPathIntplLookaheadCommand error: {ret}')
    exit()

# Execute motion
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
if ret != 0:
    print(f'StartPathIntplLookahead error: {ret}')
    exit()

# Wait for completion
axis_sel = AxisSelection()
axis_sel.axisCount = 2
axis_sel.SetAxis(0, 3)
axis_sel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret}')
    exit()

# Free buffer
Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)


# Task 2: Cubic spline motion
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print(f'CreateSplineBuffer error: {ret}')
    exit()

spline_command = AdvMotion_TotalTimeSplineCommand()
spline_command.dimensionCount = 2
spline_command.SetAxis(0, 3)
spline_command.SetAxis(1, 5)
spline_command.totalTimeMilliseconds = 1000

# Define spline points
spline_points = [
    (0, 0), (10, 10), (-20, -20), (30, 30),
    (-40, -40), (50, 50), (-60, -60), (70, 70), (-80, -80)
]

spline_objects = []
for pt in spline_points:
    sp = AdvMotion_SplinePoint()
    sp.SetPos(0, pt[0])
    sp.SetPos(1, pt[1])
    spline_objects.append(sp)

# Execute spline motion
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spline_command, 9, spline_objects)
if ret != 0:
    print(f'StartCSplinePos_TotalTime error: {ret}')
    exit()

# Wait for completion
axis_sel = AxisSelection()
axis_sel.axisCount = 2
axis_sel.SetAxis(0, 3)
axis_sel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret}')
    exit()

# Free spline buffer
Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)


# Task 3: Synchronous control
# Establish master-slave relationship
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(3, 5)
if ret != 0:
    print(f'SetSyncMasterSlave error: {ret}')
    exit()

# First movement to 120
pos_command = Motion_PosCommand()
pos_command.profile.type = ProfileType.Trapezoidal
pos_command.axis = 3
pos_command.target = 120
pos_command.profile.velocity = 1000
pos_command.profile.acc = 10000
pos_command.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(pos_command)
if ret != 0:
    print(f'First StartPos error: {ret}')
    exit()
Wmx3Lib_cm.motion.Wait(3)

# Second movement to 240
pos_command.target = 240
ret = Wmx3Lib_cm.motion.StartPos(pos_command)
if ret != 0:
    print(f'Second StartPos error: {ret}')
    exit()
Wmx3Lib_cm.motion.Wait(3)

# Release synchronization
Wmx3Lib_cm.sync.ResolveSync(5)


# Task 4: PVT interpolation
pvti = Motion_PVTIntplCommand()
pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, 20)
pvti.SetPointCount(1, 20)

# Generate circular points
center = (-50, 0)
radius = 50
for i in range(20):
    theta = 2 * math.pi * i / 20
    x = center[0] + radius * math.cos(theta)
    y = center[1] + radius * math.sin(theta)
    
    # Axis 3 parameters
    pvt_axis3 = Motion_PVTPoint()
    pvt_axis3.pos = x
    pvt_axis3.velocity = 100
    pvt_axis3.timeMilliseconds = i * 100
    pvti.SetPoints(0, i, pvt_axis3)
    
    # Axis 5 parameters
    pvt_axis5 = Motion_PVTPoint()
    pvt_axis5.pos = y
    pvt_axis5.velocity = 100
    pvt_axis5.timeMilliseconds = i * 100
    pvti.SetPoints(1, i, pvt_axis5)

# Execute PVT command
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print(f'StartPVT_Intpl error: {ret}')
    exit()

# Final wait for motion completion
axis_sel = AxisSelection()
axis_sel.axisCount = 2
axis_sel.SetAxis(0, 3)
axis_sel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
if ret != 0:
    print(f'Final Wait_AxisSel error: {ret}')
    exit()
