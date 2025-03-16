
# Axes = [8, 9]
# IOInputs = []
# IOOutputs = []

# Create the AdvancedMotion object instance (assume Wmx3Lib is already defined)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any pre-existing spline buffer on channel 0 (if it exists)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
# If ret equals 65627 (Channel buffer memory not allocated), it is safe to ignore.
if ret != 0 and ret != 65627:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Allocate buffer memory for the spline execution channel (Channel 0) with capacity for 100 points
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Set up the spline command options for a total time spline motion.
# This motion will move along 2 axes: Axis 8 and Axis 9, and complete in 1500 milliseconds (1.5 seconds)
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 8)
splineCommand.SetAxis(1, 9)
splineCommand.totalTimeMilliseconds = 1500

# Define the spline points (5 points) for the cubic spline motion.
# The points are: (0, 0), (25, 50), (50, 0), (75, -50), (100, 0)
points = []

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 0)     # Position on Axis 8
pt.SetPos(1, 0)     # Position on Axis 9
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 25)
pt.SetPos(1, 50)
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 50)
pt.SetPos(1, 0)
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 75)
pt.SetPos(1, -50)
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 100)
pt.SetPos(1, 0)
points.append(pt)

# Execute the cubic spline motion command on channel 0 using the defined spline command and points.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(points), points)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait until both Axis 8 and Axis 9 have stopped moving.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 8)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Free the spline buffer (this is usually done at the end of the application or after the motion is complete)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
