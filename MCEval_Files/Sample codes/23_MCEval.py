# Write python code to Execute an absolute position triggered linear interpolation motion command.Control Axis 0 and Axis 1 to linearly interpolate to (150, 30) at a velocity of 1000 with acceleration and deceleration of 10000. Wait for 1 millisecond, then execute the trigger linear interpolation motion command. When the completed distance of Axis 0 reaches 100, move Axis 0 and Axis 1 to (-100, -10).
    # Axes = [0, 1]

    lin = Motion_LinearIntplCommand()
    trig = Trigger()

    # Execute normal motion command
    lin.axisCount = 2
    lin.SetAxis(0, 0)
    lin.SetAxis(1, 1)

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    lin.SetTarget(0, 150)
    lin.SetTarget(1, 30)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    sleep(0.001)

    lin.SetTarget(0, -100)
    lin.SetTarget(1, -10)

    trig.triggerAxis = 0
    trig.triggerType = TriggerType.CompletedDistance
    trig.triggerValue = 100

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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
    
