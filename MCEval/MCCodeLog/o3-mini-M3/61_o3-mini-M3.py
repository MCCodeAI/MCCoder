
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

# This script executes a velocity and acceleration limited cubic spline motion for Axis 1 and Axis 4.
# The spline follows the points: (0, 0), (25, -60), (50, 0), (75, -80), (100, 0), (125, 80), (150, 0).
# Velocity limits: 500 for Axis 1, 800 for Axis 4.
# Acceleration limits: 5000 for Axis 1, 8000 for Axis 4.
# Composite limits: velocity = 1000, acceleration = 10000.
#
# The motion waits until both axes finish moving before freeing the spline buffer.

import time

# Assume the existence of the required classes and objects as defined in the motion library:
#   AdvancedMotion, AdvMotion_VelAccLimitedSplineCommand, AdvMotion_SplinePoint, AxisSelection,
#   and an instance Wmx3Lib and the motion system Wmx3Lib_cm.

# Create an instance of the advanced motion interface using the motion library object.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previous spline buffer on channel 0.
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Create the spline channel buffer with a capacity for 200 points.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
if ret != 0:
    print('CreateSplineBuffer error code ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

time.sleep(0.001)

# Set up the velocity and acceleration limited spline command.
spl = AdvMotion_VelAccLimitedSplineCommand()
spl.dimensionCount = 2

# Map the command's axis indices to the actual hardware axes:
# Index 0 corresponds to Axis 1 and index 1 corresponds to Axis 4.
spl.SetAxis(0, 1)
spl.SetAxis(1, 4)

# Set individual velocity limits.
spl.SetVelLimit(0, 500)   # Velocity limit for Axis 1.
spl.SetVelLimit(1, 800)   # Velocity limit for Axis 4.

# Set individual acceleration limits.
spl.SetAccLimit(0, 5000)  # Acceleration limit for Axis 1.
spl.SetAccLimit(1, 8000)  # Acceleration limit for Axis 4.

# Set composite (combined) velocity and acceleration limits.
spl.compositeVel = 1000
spl.compositeAcc = 10000

# Increase the sample multiplier for a smoother spline (especially when points are sparse).
spl.sampleMultiplier = 20

# Define the spline points.
# Each spline point is created and its positions for the two command dimensions are set.
coordinates = [
    (0,   0),
    (25, -60),
    (50,   0),
    (75, -80),
    (100,  0),
    (125, 80),
    (150,  0)
]

pts = []
for pos in coordinates:
    pt = AdvMotion_SplinePoint()
    # For the spline command, index 0 represents Axis 1, index 1 represents Axis 4.
    pt.SetPos(0, pos[0])
    pt.SetPos(1, pos[1])
    pts.append(pt)

# Execute the velocity and acceleration limited cubic spline motion.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_VelAccLimited(0, spl, len(pts), pts)
if ret != 0:
    print('StartCSplinePos_VelAccLimited error code ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Wait for both axis motions to complete.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)  # Axis 1.
axes.SetAxis(1, 4)  # Axis 4.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Free the spline buffer now that the motion is completed.
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

time.sleep(0.5)
