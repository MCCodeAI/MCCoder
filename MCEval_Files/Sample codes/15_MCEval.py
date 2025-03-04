# Write python code to Start a helical interpolation motion command of clockwise circular interpolation of Axis 4 and 5 with center position  (100, 120), rotation degree 720, and velocity 1060, while concurrently moving axis 8 as the linear axis to position 140.
    # Axes = [4, 5, 8]

    helicalCommand = Motion_HelicalIntplCommand()

    # Execute Helical Motion
    helicalCommand.SetAxis(0, 4)
    helicalCommand.SetAxis(1, 5)
    helicalCommand.zAxis = 8
    helicalCommand.SetCenterPos(0, 100)
    helicalCommand.SetCenterPos(1, 120)
    helicalCommand.zEndPos = 140
    helicalCommand.clockwise = 1
    helicalCommand.arcLengthDegree = 720
    helicalCommand.profile.type = ProfileType.Trapezoidal
    helicalCommand.profile.velocity = 1060
    helicalCommand.profile.acc = 10000
    helicalCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartHelicalIntplPos(helicalCommand)
    if ret != 0:
        print('StartHelicalIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4, 5 and 8 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 3
    axisSel.SetAxis(0, 4)
    axisSel.SetAxis(1, 5)
    axisSel.SetAxis(2, 8)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
        