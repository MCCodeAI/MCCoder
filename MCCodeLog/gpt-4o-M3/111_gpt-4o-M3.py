
# Axes = [1, 2, 3, 4, 5, 6]

# Create and execute a cyclic buffer memory space for Axis 1
Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Open cyclic buffer for Axis 1
ret = Wmx3Lib_cyc.OpenCyclicBuffer(1, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Start execution of cyclic buffer for Axis 1
ret = Wmx3Lib_cyc.Execute(1)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Add commands to cyclic buffer
cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()

# Move to position 60 within 100 cycles
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

# Wait for cyclic buffer execution to end
while True:
    ret, cyc_Status = Wmx3Lib_cyc.GetStatus(1)
    if cyc_Status.remainCount <= 0:
        break
    sleep(0.1)

# Close the cyclic buffer
ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    return

# Execute a PVT command for Axis 2
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 6

# Define point data
points = [
    (0, 0, 0),
    (50, 1000, 100),
    (100, 2000, 200),
    (200, 3000, 300),
    (300, 1000, 400),
    (200, 0, 500)
]

for i, (pos, vel, time) in enumerate(points):
    pvtparameter.pos = pos
    pvtparameter.velocity = vel
    pvtparameter.timeMilliseconds = time
    pvt.SetPoints(i, pvtparameter)

# Start PVT motion
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for motion to finish
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a PT command for Axis 3
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 3
pt.pointCount = 5

# Define point data
points = [
    (50, 0),
    (-50, 100),
    (50, 200),
    (-50, 300),
    (0, 400)
]

for i, (pos, time) in enumerate(points):
    ptparameter.pos = pos
    ptparameter.timeMilliseconds = time
    pt.SetPoints(i, ptparameter)

# Start PT motion
ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for motion to finish
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a VT command for Axis 4
vt = Motion_VTCommand()
vtparameter = Motion_VTPoint()

vt.axis = 4
vt.pointCount = 5

# Define point data
points = [
    (60, 0),
    (-60, 100),
    (60, 200),
    (-60, 300),
    (0, 400)
]

for i, (vel, time) in enumerate(points):
    vtparameter.velocity = vel
    vtparameter.timeMilliseconds = time
    vt.SetPoints(i, vtparameter)

# Start VT motion
ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for motion to finish
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 5 by a distance of 60 with a velocity of 1400
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 60
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to a specified distance relatively
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for motion to finish
ret = Wmx3Lib_cm.motion.Wait(5)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute a total time cubic spline of Axis 5 and Axis 6
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)

# Create the spline channel buffer
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
spl = AdvMotion_TotalTimeSplineCommand()

spl.dimensionCount = 2
spl.SetAxis(0, 5)
spl.SetAxis(1, 6)
spl.totalTimeMilliseconds = 1500

pt = []

pt.append(AdvMotion_SplinePoint())
pt[0].SetPos(0, 0)
pt[0].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[1].SetPos(0, 25)
pt[1].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[2].SetPos(0, 50)
pt[2].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[3].SetPos(0, 75)
pt[3].SetPos(1, -50)

pt.append(AdvMotion_SplinePoint())
pt[4].SetPos(0, 100)
pt[4].SetPos(1, 0)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 5)
axes.SetAxis(1, 6)

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Free the spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
