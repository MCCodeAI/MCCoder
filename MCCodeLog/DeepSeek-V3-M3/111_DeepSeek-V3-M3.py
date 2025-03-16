
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# Task 1: Create and execute a cyclic buffer memory space for Axis 1
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

# Dynamically add points to move from the current position to the absolute position of 60 within 100 cycles.
cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 60
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move a relative distance of 140 within 100 cycles.
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
cyclicBufferSingleAxisCommand.intervalCycles = 100
cyclicBufferSingleAxisCommand.command = 140
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Move to position -100 within 200 cycles.
cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
cyclicBufferSingleAxisCommand.intervalCycles = 200
cyclicBufferSingleAxisCommand.command = -100
ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Wait for Cyclic buffer executing to end
while True:
    ret, cyc_Status = Wmx3Lib_cyc.GetStatus(1)
    if cyc_Status.remainCount <= 0:
        break
    sleep(0.1)

# Close the cyclic buffer memory space.
ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Task 2: Execute a PVT command for Axis 2
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 6

# Define point data
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

pvtparameter.pos = 200
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 500
pvt.SetPoints(5, pvtparameter)

# Start PVT motion
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 3: Execute a PT command for Axis 3
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 3
pt.pointCount = 5

# Define point data
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

# Start PT motion
ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 4: Execute a VT command for Axis 4
vt = Motion_VTCommand()
vtparameter = Motion_VTPoint()

vt.axis = 4
vt.pointCount = 5

# Define point data
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

# Start VT motion
ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Task 5: Move Axis 5 by a distance of 60 with a velocity of 1400
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 60
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to a specified distance relatively.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(5)

# Task 6: Execute a total time(1.5s) cubic spline of Axis 5 and Axis 6
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Allocate buffer memory for a spline execution channel with 100 points for Channel 0.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options, specifying Axis 5 and Axis 6, with a total time of 1,500 milliseconds to complete the spline motion.
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 5)
splineCommand.SetAxis(1, 6)
splineCommand.totalTimeMilliseconds = 1500

# Set the spline point data with 5 points.
splinePoint = []

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[0].SetPos(0, 0)
splinePoint[0].SetPos(1, 0)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[1].SetPos(0, 25)
splinePoint[1].SetPos(1, 50)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[2].SetPos(0, 50)
splinePoint[2].SetPos(1, 0)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[3].SetPos(0, 75)
splinePoint[3].SetPos(1, -50)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[4].SetPos(0, 100)
splinePoint[4].SetPos(1, 0)

# Execute the spline command.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 5, splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete. Start a blocking wait command, returning only when Axis 5 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the spline execution channel. (Normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
