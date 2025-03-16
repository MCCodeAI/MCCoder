
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# Task 1: Cyclic Buffer for Axis 1
Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Create a new cyclic buffer memory space for Axis 1, with a size of 1,024 cycles.
ret = Wmx3Lib_cyc.OpenCyclicBuffer(1, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Start the execution of the cyclic position command buffer for Axis 1.
ret = Wmx3Lib_cyc.Execute(1)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move to position 60 within 100 cycles
cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 60
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move a relative distance of 140 within 100 cycles
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 140
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move to position -100 within 200 cycles
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 200
cyclicBufferSingleAxisCommand.command = -100
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Close the cyclic buffer memory space.
ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Task 2: PVT Command for Axis 2
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 6

# Define point data
points = [(0, 0, 0), (50, 1000, 100), (100, 2000, 200), (200, 3000, 300), (300, 1000, 400), (200, 0, 500)]
for i, (pos, vel, time) in enumerate(points):
    pvtparameter.pos = pos
    pvtparameter.velocity = vel
    pvtparameter.timeMilliseconds = time
    pvt.SetPoints(i, pvtparameter)

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(2)

# Task 3: PT Command for Axis 3
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 3
pt.pointCount = 5

# Define point data
points = [(50, 0), (-50, 100), (50, 200), (-50, 300), (0, 400)]
for i, (pos, time) in enumerate(points):
    ptparameter.pos = pos
    ptparameter.timeMilliseconds = time
    pt.SetPoints(i, ptparameter)

ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

# Task 4: VT Command for Axis 4
vt = Motion_VTCommand()
vtparameter = Motion_VTPoint()

vt.axis = 4
vt.pointCount = 5

# Define point data
points = [(60, 0), (-60, 100), (60, 200), (-60, 300), (0, 400)]
for i, (vel, time) in enumerate(points):
    vtparameter.velocity = vel
    vtparameter.timeMilliseconds = time
    vt.SetPoints(i, vtparameter)

ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Task 5: Move Axis 5 by distance of 60 with velocity 1400
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 60
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(5)

# Task 6: Cubic Spline for Axes 5 and 6
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 5)
splineCommand.SetAxis(1, 6)
splineCommand.totalTimeMilliseconds = 1500

points = [(0, 0), (25, 50), (50, 0), (75, -50), (100, 0)]
splinePoint = []
for pos5, pos6 in points:
    pt = AdvMotion_SplinePoint()
    pt.SetPos(0, pos5)
    pt.SetPos(1, pos6)
    splinePoint.append(pt)

ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(points), splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
