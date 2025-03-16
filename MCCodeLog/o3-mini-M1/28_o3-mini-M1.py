
# Axes = [8, 9]
# IOInputs = []
# IOOutputs = []

# This script initiates a cubic spline motion command for Axes 8 and 9.
# The motion is defined with 9 spline points and a total execution time of 1000ms.
# After starting the motion, the script waits until both axes have stopped moving,
# and then frees the allocated spline buffer.

# Assume that the following objects and classes are defined in the environment:
#   Wmx3Lib, AdvancedMotion, AdvMotion_TotalTimeSplineCommand, AdvMotion_SplinePoint,
#   Wmx3Lib_cm, AxisSelection
#
# No motion libraries are explicitly imported here per instructions.

# Free any previous spline buffer for channel 0 (optional but recommended).
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)

# Create the spline channel buffer with a capacity of 100 points.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Set up the total time cubic spline command for two axes.
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 8)
splineCommand.SetAxis(1, 9)
splineCommand.totalTimeMilliseconds = 1000

# Define the 9 spline points for the motion.
splinePoints = []

# 1st point: (0, 0)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 0)
pt.SetPos(1, 0)
splinePoints.append(pt)

# 2nd point: (10, -10)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 10)
pt.SetPos(1, -10)
splinePoints.append(pt)

# 3rd point: (-20, 20)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, -20)
pt.SetPos(1, 20)
splinePoints.append(pt)

# 4th point: (30, -30)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 30)
pt.SetPos(1, -30)
splinePoints.append(pt)

# 5th point: (-40, 40)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, -40)
pt.SetPos(1, 40)
splinePoints.append(pt)

# 6th point: (50, -50)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 50)
pt.SetPos(1, -50)
splinePoints.append(pt)

# 7th point: (-60, 60)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, -60)
pt.SetPos(1, 60)
splinePoints.append(pt)

# 8th point: (70, -70)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 70)
pt.SetPos(1, -70)
splinePoints.append(pt)

# 9th point: (0, 0)
pt = AdvMotion_SplinePoint()
pt.SetPos(0, 0)
pt.SetPos(1, 0)
splinePoints.append(pt)

# Execute the cubic spline command using the prepared command structure and points.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 9, splinePoints)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the spline motion to complete by blocking until both axes become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 8)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Free the spline buffer.
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
