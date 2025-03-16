
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)

# Create the spline channel buffer
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
spl = AdvMotion_VelAccLimitedSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 1)  # Axis 1
spl.SetAxis(1, 4)  # Axis 4
spl.SetVelLimit(0, 500)  # Velocity limit for Axis 1
spl.SetVelLimit(1, 800)  # Velocity limit for Axis 4
spl.SetAccLimit(0, 5000)  # Acceleration limit for Axis 1
spl.SetAccLimit(1, 8000)  # Acceleration limit for Axis 4
spl.compositeVel = 1000
spl.compositeAcc = 10000
spl.sampleMultiplier = 20

# Set the spline point data
pt = []

# Define the points for the spline
points = [(0, 0), (25, -60), (50, 0), (75, -80), (100, 0), (125, 80), (150, 0)]

for i, (pos1, pos4) in enumerate(points):
    pt.append(AdvMotion_SplinePoint())
    pt[i].SetPos(0, pos1)  # Position for Axis 1
    pt[i].SetPos(1, pos4)  # Position for Axis 4

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_VelAccLimited(0, spl, len(points), pt)
if ret != 0:
    print('StartCSplinePos_VelAccLimited error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)  # Axis 1
axes.SetAxis(1, 4)  # Axis 4
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Free the spline buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
