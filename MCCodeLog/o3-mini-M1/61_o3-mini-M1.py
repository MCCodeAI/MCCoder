
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

from time import sleep

# Create an instance of the AdvancedMotion class using Wmx3Lib (assumed to be defined)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previous spline buffer (usually done at the start or end of the application)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Create the spline channel buffer with a sufficient buffer size (e.g., 200)
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

sleep(0.001)
# Set the spline command options for velocity and acceleration limited cubic spline

spl = AdvMotion_VelAccLimitedSplineCommand()
spl.dimensionCount = 2

# Map the spline dimensions to the actual axes:
#  Dimension index 0 corresponds to Axis 1
#  Dimension index 1 corresponds to Axis 4
spl.SetAxis(0, 1)
spl.SetAxis(1, 4)

# Set individual velocity limits for each axis
spl.SetVelLimit(0, 500)   # Velocity limit for Axis 1
spl.SetVelLimit(1, 800)   # Velocity limit for Axis 4

# Set individual acceleration limits for each axis
spl.SetAccLimit(0, 5000)  # Acceleration limit for Axis 1
spl.SetAccLimit(1, 8000)  # Acceleration limit for Axis 4

# Set composite limits
spl.compositeVel = 1000
spl.compositeAcc = 10000

# Increase the sample multiplier to improve the accuracy of the generated profile
spl.sampleMultiplier = 20

# Define the spline points as provided: (pos for Axis 1, pos for Axis 4)
points = [
    (0, 0),
    (25, -60),
    (50, 0),
    (75, -80),
    (100, 0),
    (125, 80),
    (150, 0)
]

# Create an array to hold the spline point objects
pt = []
for (p0, p1) in points:
    point = AdvMotion_SplinePoint()
    point.SetPos(0, p0)  # Position for Axis 1 (dimension 0)
    point.SetPos(1, p1)  # Position for Axis 4 (dimension 1)
    pt.append(point)

numPoints = len(pt)

# Execute the velocity and acceleration limited cubic spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_VelAccLimited(0, spl, numPoints, pt)
if ret != 0:
    print('StartCSplinePos_VelAccLimited error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Wait for the spline motion to complete on the specified axes.
# This wait is issued after the motion command completes.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)
axes.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Free the spline buffer (normally done at the end of the operation)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

sleep(0.5)
