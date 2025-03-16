
# Axes = [8, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free the spline buffer before creating a new one
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
spl = AdvMotion_TotalTimeSplineCommand()

spl.dimensionCount = 2
spl.SetAxis(0, 8)
spl.SetAxis(1, 9)
spl.totalTimeMilliseconds = 1500  # Total time for the spline motion is 1.5 seconds

# Define the spline points
pt = []

pt.append(AdvMotion_SplinePoint())
pt[0].SetPos(0, 0)
pt[0].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[1].SetPos(0, 25)
pt[1].SetPos(1, 50)

pt.append(AdvMotion_SplinePoint())
pt[2].SetPos(0, 50)
pt[2].SetPos(1, 0)

pt.append(AdvMotion_SplinePoint())
pt[3].SetPos(0, 75)
pt[3].SetPos(1, -50)

pt.append(AdvMotion_SplinePoint())
pt[4].SetPos(0, 100)
pt[4].SetPos(1, 0)

# Execute the spline command
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spl, 5, pt)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 8)
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
