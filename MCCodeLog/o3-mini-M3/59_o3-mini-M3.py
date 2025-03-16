
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

# Create an instance of the AdvancedMotion class to access advanced motion functions.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previous spline buffer from channel 0.
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
# If the error code is 65627, it indicates that channel buffer memory was never allocated; ignore that error.
if ret != 0 and ret != 65627:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create the spline channel buffer.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

sleep(0.001)

# Set up the spline command options for a trapezoidal profile type cubic spline.
spl = AdvMotion_ProfileSplineCommand()
spl.dimensionCount = 2
# Set the axes in ascending order: dimension 0 -> Axis 6, dimension 1 -> Axis 9.
spl.SetAxis(0, 6)
spl.SetAxis(1, 9)
spl.profile = Profile()
spl.profile.type = ProfileType.Trapezoidal
spl.profile.velocity = 1600
spl.profile.acc = 10000
spl.profile.dec = 10000

# Define the 5 spline points.
pt = []

# Point 1: (0, 0)
point = AdvMotion_SplinePoint()
point.SetPos(0, 0)
point.SetPos(1, 0)
pt.append(point)

# Point 2: (25, -50)
point = AdvMotion_SplinePoint()
point.SetPos(0, 25)
point.SetPos(1, -50)
pt.append(point)

# Point 3: (50, 0)
point = AdvMotion_SplinePoint()
point.SetPos(0, 50)
point.SetPos(1, 0)
pt.append(point)

# Point 4: (75, 50)
point = AdvMotion_SplinePoint()
point.SetPos(0, 75)
point.SetPos(1, 50)
pt.append(point)

# Point 5: (100, 0)
point = AdvMotion_SplinePoint()
point.SetPos(0, 100)
point.SetPos(1, 0)
pt.append(point)

# Execute the cubic spline command.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_Profile error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for both axes (6 and 9) to complete the spline motion.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 6)
axes.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Free the spline buffer (normally done at the end of the motion).
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

sleep(0.5)
