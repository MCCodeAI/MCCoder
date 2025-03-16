
# Axes = [9, 6]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing spline buffer
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Create the spline channel buffer
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options
spl = AdvMotion_SCurveSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 9)
spl.SetAxis(1, 6)
spl.velocity = 1200
spl.acceleration = 5000

# Define the spline points
pt = []

pt.append(AdvMotion_SplinePoint())
pt[0].SetPos(0, 0)
pt[0].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[1].SetPos(0, 30)
pt[1].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[2].SetPos(0, 60)
pt[2].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[3].SetPos(0, 90)
pt[3].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[4].SetPos(0, 120)
pt[4].SetPos(1, 0)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_SCurve(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_SCurve error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 9)
axes.SetAxis(1, 6)

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
