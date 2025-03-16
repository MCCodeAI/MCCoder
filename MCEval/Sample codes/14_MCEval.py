# Write python code to Start a clockwise circular interpolation motion command of Axis 0 and 1 with center position (100, 200), arc length 360, and velocity 1000.
    # Axes = [0, 1]

    circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()

    # Execute Circular Interpolation of Axis 0 and 1 with center position (100, 200), arc length 360, velocity 1000.
    circularIntplCommand.SetAxis(0, 0)
    circularIntplCommand.SetAxis(1, 1)
    circularIntplCommand.SetCenterPos(0, 100)
    circularIntplCommand.SetCenterPos(1, 200)
    circularIntplCommand.clockwise = 1
    circularIntplCommand.arcLengthDegree = 360
    circularIntplCommand.profile.type = ProfileType.Trapezoidal
    circularIntplCommand.profile.velocity = 1000
    circularIntplCommand.profile.acc = 10000
    circularIntplCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
    if ret != 0:
        print('StartCircularIntplPos_RadiusAndEnd error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

