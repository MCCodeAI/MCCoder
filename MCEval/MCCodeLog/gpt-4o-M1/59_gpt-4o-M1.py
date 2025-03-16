
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing spline buffer for channel 0
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Create a new spline buffer for channel 0 with a size of 100
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set up the spline command with trapezoidal profile
spl = AdvMotion_ProfileSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 6)  # Axis 6
spl.SetAxis(1, 9)  # Axis 9
spl.profile = Profile()
spl.profile.type = ProfileType.Trapezoidal
spl.profile.velocity = 1600
spl.profile.acc = 10000
spl.profile.dec = 10000

# Define the spline points
pt = []

pt.append(AdvMotion_SplinePoint())
pt[0].SetPos(0, 0)
pt[0].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[1].SetPos(0, 25)
pt[1].SetPos(1, -50)

pt.append(AdvMotion_SplinePoint())
pt[2].SetPos(0, 50)
pt[2].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[3].SetPos(0, 75)
pt[3].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[4].SetPos(0, 100)
pt[4].SetPos(1, 0)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_Profile error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 6)
axes.SetAxis(1, 9)

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Free the spline buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

sleep(0.5)
