
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# Task 1: Cyclic Buffer for Axis 1
Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Create cyclic buffer with 1024 cycles
ret = Wmx3Lib_cyc.OpenCyclicBuffer(1, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Start execution
ret = Wmx3Lib_cyc.Execute(1)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Add commands
cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()

# Move to position 60 in 100 cycles
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 60
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

# Move relative 140 in 100 cycles
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 140
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

# Move to position -100 in 200 cycles
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 200
cyclicBufferSingleAxisCommand.command = -100
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

# Wait for completion
while True:
    ret, cyc_Status = Wmx3Lib_cyc.GetStatus(1)
    if cyc_Status.remainCount <= 0:
        break
    sleep(0.1)

# Close cyclic buffer
ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return


# Task 2: PVT Command for Axis 2
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 5

# Define points
pvtparameter.pos = 0
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 0
pvt.SetPoints(0, pvtparameter)

pvtparameter.pos = 50
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 100
pvt.SetPoints(1, pvtparameter)

pvtparameter.pos = 100
pvtparameter.velocity = 2000
pvtparameter.timeMilliseconds = 200
pvt.SetPoints(2, pvtparameter)

pvtparameter.pos = 200
pvtparameter.velocity = 3000
pvtparameter.timeMilliseconds = 300
pvt.SetPoints(3, pvtparameter)

pvtparameter.pos = 300
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 400
pvt.SetPoints(4, pvtparameter)

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return


# Task 3: PT Command for Axis 3
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 3
pt.pointCount = 5

# Define points
ptparameter.pos = 50
ptparameter.timeMilliseconds = 0
pt.SetPoints(0, ptparameter)

ptparameter.pos = -50
ptparameter.timeMilliseconds = 100
pt.SetPoints(1, ptparameter)

ptparameter.pos = 50
ptparameter.timeMilliseconds = 200
pt.SetPoints(2, ptparameter)

ptparameter.pos = -50
ptparameter.timeMilliseconds = 300
pt.SetPoints(3, ptparameter)

ptparameter.pos = 0
ptparameter.timeMilliseconds = 400
pt.SetPoints(4, ptparameter)

ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return


# Task 4: VT Command for Axis 4
vt = Motion_VTCommand()
vtparameter = Motion_VTPoint()

vt.axis = 4
vt.pointCount = 5

# Define points
vtparameter.velocity = 60
vtparameter.timeMilliseconds = 0
vt.SetPoints(0, vtparameter)

vtparameter.velocity = -60
vtparameter.timeMilliseconds = 100
vt.SetPoints(1, vtparameter)

vtparameter.velocity = 60
vtparameter.timeMilliseconds = 200
vt.SetPoints(2, vtparameter)

vtparameter.velocity = -60
vtparameter.timeMilliseconds = 300
vt.SetPoints(3, vtparameter)

vtparameter.velocity = 0
vtparameter.timeMilliseconds = 400
vt.SetPoints(4, vtparameter)

ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return


# Task 5: Move Axis 5 by distance
lin = Motion_LinearIntplCommand()
lin.axisCount = 1
lin.SetAxis(0, 5)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1400
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 60)

ret = Wmx3Lib_cm.motion.StartLinearIntplDist(lin)
if ret != 0:
    print('StartLinearIntplDist error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.Wait(5)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return


# Task 6: Cubic Spline for Axes 5 and 6
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

# Clear and create buffer
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
Wmx3Lib_buf.StartRecordBufferChannel(0)

spline = Motion_CubicSplineCommand()
spline.axisCount = 2
spline.SetAxis(0, 5)
spline.SetAxis(1, 6)
spline.pointCount = 5

# Define points
spline.SetPoint(0, 0, 0)
spline.SetPoint(1, 25, 50)
spline.SetPoint(2, 50, 0)
spline.SetPoint(3, 75, -50)
spline.SetPoint(4, 100, 0)

ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
if ret != 0:
    print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End recording and execute
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for completion
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 5)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Cleanup
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
