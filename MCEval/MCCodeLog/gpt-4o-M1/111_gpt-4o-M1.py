
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# Create and execute a cyclic buffer memory space for Axis 1
cyclic_buffer_axis_1 = CyclicBuffer(Wmx3Lib)
ret = cyclic_buffer_axis_1.OpenCyclicBuffer(1, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

ret = cyclic_buffer_axis_1.Execute(1)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

# Move to position 60 within 100 cycles
command = CyclicBufferSingleAxisCommand()
command.type = CyclicBufferCommandType.AbsolutePos
command.intervalCycles = 100
command.command = 60
ret = cyclic_buffer_axis_1.AddCommand(1, command)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

# Move a relative distance of 140 within 100 cycles
command.type = CyclicBufferCommandType.RelativePos
command.intervalCycles = 100
command.command = 140
ret = cyclic_buffer_axis_1.AddCommand(1, command)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

# Move to position -100 within 200 cycles
command.type = CyclicBufferCommandType.AbsolutePos
command.intervalCycles = 200
command.command = -100
ret = cyclic_buffer_axis_1.AddCommand(1, command)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

# Wait for cyclic buffer execution to end
while True:
    ret, status = cyclic_buffer_axis_1.GetStatus(1)
    if status.remainCount <= 0:
        break
    sleep(0.1)

# Close the cyclic buffer memory space
ret = cyclic_buffer_axis_1.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
    return

# Execute a PVT command for Axis 2
pvt = Motion_PVTCommand()
pvt.axis = 2
pvt.pointCount = 6

points = [
    (0, 0, 0),
    (50, 1000, 100),
    (100, 2000, 200),
    (200, 3000, 300),
    (300, 1000, 400),
    (200, 0, 500)
]

for i, (pos, vel, time) in enumerate(points):
    pvt_point = Motion_PVTPoint()
    pvt_point.pos = pos
    pvt_point.velocity = vel
    pvt_point.timeMilliseconds = time
    pvt.SetPoints(i, pvt_point)

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a PT command for Axis 3
pt = Motion_PTCommand()
pt.axis = 3
pt.pointCount = 5

points = [
    (50, 0),
    (-50, 100),
    (50, 200),
    (-50, 300),
    (0, 400)
]

for i, (pos, time) in enumerate(points):
    pt_point = Motion_PTPoint()
    pt_point.pos = pos
    pt_point.timeMilliseconds = time
    pt.SetPoints(i, pt_point)

ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a VT command for Axis 4
vt = Motion_VTCommand()
vt.axis = 4
vt.pointCount = 5

points = [
    (60, 0),
    (-60, 100),
    (60, 200),
    (-60, 300),
    (0, 400)
]

for i, (vel, time) in enumerate(points):
    vt_point = Motion_VTPoint()
    vt_point.velocity = vel
    vt_point.timeMilliseconds = time
    vt.SetPoints(i, vt_point)

ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 5 by a distance of 60 with a velocity of 1400
move_command = Motion_MoveCommand()
move_command.axis = 5
move_command.distance = 60
move_command.velocity = 1400

ret = Wmx3Lib_cm.motion.StartMove(move_command)
if ret != 0:
    print('StartMove error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(5)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a cubic spline for Axis 5 and Axis 6
spline = Motion_CubicSplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 5)
spline.SetAxis(1, 6)
spline.totalTimeSeconds = 1.5

points = [
    (0, 0),
    (25, 50),
    (50, 0),
    (75, -50),
    (100, 0)
]

for i, (pos5, pos6) in enumerate(points):
    spline.SetPoint(i, 0, pos5)
    spline.SetPoint(i, 1, pos6)

ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
if ret != 0:
    print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 5)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
