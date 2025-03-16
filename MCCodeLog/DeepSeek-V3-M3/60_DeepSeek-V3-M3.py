
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)

# Create the spline channel buffer
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

sleep(0.001)
# Set the spline command options
spl = AdvMotion_VelAccLimitedSplineCommand()
spl.dimensionCount = 2
spl.SetAxis(0, 6)
spl.SetAxis(1, 9)
spl.SetVelLimit(0, 1200)
spl.SetVelLimit(1, 1200)
spl.SetAccLimit(0, 5000)
spl.SetAccLimit(1, 5000)
spl.compositeVel = 1200
spl.compositeAcc = 5000
spl.sampleMultiplier = 20

# Set the spline point data
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
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_VelAccLimited(0, spl, 5, pt)

if ret != 0:
    print('StartCSplinePos_VelAccLimited error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
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
