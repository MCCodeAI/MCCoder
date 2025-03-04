# Write python code to Execute an absolute position linear interpolation motion command. Control Axis 0 and Axis 1 to linearly interpolate to position (300, 100). Set the maximum velocity of Axis 0 to 600 and Axis 1 to 500, with a maximum acceleration and deceleration of Axis 0 to 4000 and Axis 1 to 3000.
    # Axes = [0, 1]

    lin = Motion_LinearIntplCommand()

    # Execute absolute position linear interpolation motion command
    lin.axisCount = 2
    lin.SetAxis(0, 0)
    lin.SetAxis(1, 1)

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    lin.SetTarget(0, 300)
    lin.SetTarget(1, 100)

    lin.SetMaxVelocity(0, 600)
    lin.SetMaxVelocity(1, 500)

    lin.SetMaxAcc(0, 4000)
    lin.SetMaxAcc(1, 3000)

    lin.SetMaxDec(0, 4000)
    lin.SetMaxDec(1, 3000)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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
