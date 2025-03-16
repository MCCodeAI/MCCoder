
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# This script performs several motion commands:
# 1. Creates and executes a cyclic buffer for Axis 1.
#    It moves to position 60 in 100 cycles, then moves a relative 140 in 100 cycles,
#    then moves to position -100 in 200 cycles.
# 2. Executes a PVT command for Axis 2 with six points.
# 3. Executes a PT command for Axis 3 with five points.
# 4. Executes a VT command for Axis 4 with five points.
# 5. Moves Axis 5 by a distance of 60 at a velocity of 1400.
# 6. Executes a 1.5-second total time cubic spline motion for Axis 5 and Axis 6
#    with five defined points.

from time import sleep

# ---------------------------- 1. Cyclic Buffer for Axis 1 ----------------------------

Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

# Open a cyclic buffer memory space for Axis 1 with a buffer size of 1024 cycles.
ret = Wmx3Lib_cyc.OpenCyclicBuffer(1, 1024)
if ret != 0:
    print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    # Exit or handle error as needed.

# Start cyclic buffer execution for Axis 1.
ret = Wmx3Lib_cyc.Execute(1)
if ret != 0:
    print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
    # Exit or handle error as needed.

# Create a command instance for cyclic buffer commands.
cyclicCmd = CyclicBufferSingleAxisCommand()

# Add an absolute position command: move to position 60 in 100 cycles.
cyclicCmd.type = CyclicBufferCommandType.AbsolutePos
cyclicCmd.intervalCycles = 100
cyclicCmd.command = 60
ret = Wmx3Lib_cyc.AddCommand(1, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))

# Add a relative position command: move a relative distance 140 in 100 cycles.
cyclicCmd.type = CyclicBufferCommandType.RelativePos
cyclicCmd.intervalCycles = 100
cyclicCmd.command = 140
ret = Wmx3Lib_cyc.AddCommand(1, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))

# Add an absolute position command: move to position -100 in 200 cycles.
cyclicCmd.type = CyclicBufferCommandType.AbsolutePos
cyclicCmd.intervalCycles = 200
cyclicCmd.command = -100
ret = Wmx3Lib_cyc.AddCommand(1, cyclicCmd)
if ret != 0:
    print('AddCommand error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))

# Wait for the cyclic buffer execution to finish before closing the buffer.
while True:
    ret, cyc_status = Wmx3Lib_cyc.GetStatus(1)
    if cyc_status.remainCount <= 0:
        break
    sleep(0.1)

# Close the cyclic buffer memory space.
ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
if ret != 0:
    print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))


# ---------------------------- 2. PVT Command for Axis 2 ----------------------------

pvt = Motion_PVTCommand()
pvt_param = Motion_PVTPoint()
pvt.axis = 2
pvt.pointCount = 6

# Point 0: (0, 0, 0)
pvt_param.pos = 0
pvt_param.velocity = 0
pvt_param.timeMilliseconds = 0
pvt.SetPoints(0, pvt_param)

# Point 1: (50, 1000, 100)
pvt_param.pos = 50
pvt_param.velocity = 1000
pvt_param.timeMilliseconds = 100
pvt.SetPoints(1, pvt_param)

# Point 2: (100, 2000, 200)
pvt_param.pos = 100
pvt_param.velocity = 2000
pvt_param.timeMilliseconds = 200
pvt.SetPoints(2, pvt_param)

# Point 3: (200, 3000, 300)
pvt_param.pos = 200
pvt_param.velocity = 3000
pvt_param.timeMilliseconds = 300
pvt.SetPoints(3, pvt_param)

# Point 4: (300, 1000, 400)
pvt_param.pos = 300
pvt_param.velocity = 1000
pvt_param.timeMilliseconds = 400
pvt.SetPoints(4, pvt_param)

# Point 5: (200, 0, 500)
pvt_param.pos = 200
pvt_param.velocity = 0
pvt_param.timeMilliseconds = 500
pvt.SetPoints(5, pvt_param)

ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the PVT motion for Axis 2 is finished.
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))


# ---------------------------- 3. PT Command for Axis 3 ----------------------------

pt = Motion_PTCommand()
pt_param = Motion_PTPoint()
pt.axis = 3
pt.pointCount = 5

# Point 0: (50, 0)
pt_param.pos = 50
pt_param.timeMilliseconds = 0
pt.SetPoints(0, pt_param)

# Point 1: (-50, 100)
pt_param.pos = -50
pt_param.timeMilliseconds = 100
pt.SetPoints(1, pt_param)

# Point 2: (50, 200)
pt_param.pos = 50
pt_param.timeMilliseconds = 200
pt.SetPoints(2, pt_param)

# Point 3: (-50, 300)
pt_param.pos = -50
pt_param.timeMilliseconds = 300
pt.SetPoints(3, pt_param)

# Point 4: (0, 400)
pt_param.pos = 0
pt_param.timeMilliseconds = 400
pt.SetPoints(4, pt_param)

ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the PT motion for Axis 3 is finished.
ret = Wmx3Lib_cm.motion.Wait(3)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))


# ---------------------------- 4. VT Command for Axis 4 ----------------------------

vt = Motion_VTCommand()
vt_param = Motion_VTPoint()
vt.axis = 4
vt.pointCount = 5

# Point 0: (60, 0)
vt_param.velocity = 60
vt_param.timeMilliseconds = 0
vt.SetPoints(0, vt_param)

# Point 1: (-60, 100)
vt_param.velocity = -60
vt_param.timeMilliseconds = 100
vt.SetPoints(1, vt_param)

# Point 2: (60, 200)
vt_param.velocity = 60
vt_param.timeMilliseconds = 200
vt.SetPoints(2, vt_param)

# Point 3: (-60, 300)
vt_param.velocity = -60
vt_param.timeMilliseconds = 300
vt.SetPoints(3, vt_param)

# Point 4: (0, 400)
vt_param.velocity = 0
vt_param.timeMilliseconds = 400
vt.SetPoints(4, vt_param)

ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the VT motion for Axis 4 is finished.
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))


# ---------------------------- 5. Simple Relative Move for Axis 5 ----------------------------

moveCmd = Motion_SimpleMoveCommand()
moveCmd.axis = 5
moveCmd.distance = 60
moveCmd.velocity = 1400

ret = Wmx3Lib_cm.motion.StartSimpleMove(moveCmd)
if ret != 0:
    print('StartSimpleMove error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the simple move for Axis 5 is finished.
ret = Wmx3Lib_cm.motion.Wait(5)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))


# ---------------------------- 6. Cubic Spline for Axis 5 and Axis 6 ----------------------------

cSpline = Motion_CubicSplineCommand()
cSpline.axisCount = 2
cSpline.totalTimeMilliseconds = 1500  # 1.5 seconds = 1500 milliseconds
cSpline.pointCount = 5

# Assign the axes: first axis is 5, second axis is 6.
cSpline.SetAxis(0, 5)
cSpline.SetAxis(1, 6)

# Define the cubic spline points.
# Point 0: (0, 0)
cSpline.SetPoints(0, 0, 0)
# Point 1: (25, 50)
cSpline.SetPoints(1, 25, 50)
# Point 2: (50, 0)
cSpline.SetPoints(2, 50, 0)
# Point 3: (75, -50)
cSpline.SetPoints(3, 75, -50)
# Point 4: (100, 0)
cSpline.SetPoints(4, 100, 0)

ret = Wmx3Lib_cm.motion.StartCubicSpline(cSpline)
if ret != 0:
    print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the cubic spline motion for Axis 5 and Axis 6 is finished.
axesSel = AxisSelection()
axesSel.axisCount = 2
axesSel.SetAxis(0, 5)
axesSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axesSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
