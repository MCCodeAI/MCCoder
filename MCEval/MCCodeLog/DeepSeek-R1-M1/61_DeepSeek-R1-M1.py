
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Create the spline buffer with sufficient capacity
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

sleep(0.001)

# Configure the spline command
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
spl.sampleMultiplier = 20  # Increased for better accuracy

# Define the spline points
pt = []
points = [(0, 0), (25, -60), (50, 0), (75, -80), (100, 0), (125, 80), (150, 0)]

for i, (x, y) in enumerate(points):
    pt.append(AdvMotion_SplinePoint())
    pt[i].SetPos(0, x)  # Axis 1 position
    pt[i].SetPos(1, y)  # Axis 4 position

# Execute the spline motion
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_VelAccLimited(0, spl, len(points), pt)
if ret != 0:
    print('StartCSplinePos_VelAccLimited error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 1)
axes.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Free the spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

sleep(0.5)
