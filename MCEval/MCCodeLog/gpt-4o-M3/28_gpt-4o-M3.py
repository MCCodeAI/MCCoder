
# Axes = [8, 9]
# Inputs = []
# Outputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Allocate buffer memory for a spline execution channel with 100 points for Channel 0.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set the spline command options, specifying Axis 8 and Axis 9, with a total time of 1,000 milliseconds to complete the spline motion.
splineCommand = AdvMotion_TotalTimeSplineCommand()
splineCommand.dimensionCount = 2
splineCommand.SetAxis(0, 8)
splineCommand.SetAxis(1, 9)
splineCommand.totalTimeMilliseconds = 1000

# Set the spline point data with 9 points.
splinePoint = []

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[0].SetPos(0, 0)
splinePoint[0].SetPos(1, 0)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[1].SetPos(0, 10)
splinePoint[1].SetPos(1, -10)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[2].SetPos(0, -20)
splinePoint[2].SetPos(1, 20)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[3].SetPos(0, 30)
splinePoint[3].SetPos(1, -30)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[4].SetPos(0, -40)
splinePoint[4].SetPos(1, 40)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[5].SetPos(0, 50)
splinePoint[5].SetPos(1, -50)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[6].SetPos(0, -60)
splinePoint[6].SetPos(1, 60)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[7].SetPos(0, 70)
splinePoint[7].SetPos(1, -70)

splinePoint.append(AdvMotion_SplinePoint())
splinePoint[8].SetPos(0, 0)
splinePoint[8].SetPos(1, 0)

# Execute the spline command.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, 9, splinePoint)
if ret != 0:
    print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the spline motion to complete. Start a blocking wait command, returning only when Axis 8 and Axis 9 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 8)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Free buffer memory for the spline execution channel. (Normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
