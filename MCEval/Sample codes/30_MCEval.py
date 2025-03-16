# Write python code to Execute a sequence of linear interpolation commands using trigger motion functions and Wait functions. Control Axis 0 and Axis 1 to linearly interpolate to (100, 0) at a velocity of 500，and then trigger Axis 0 and Axis 1 to linearly interpolate to (100, 100), (0, 100) and (0, 0) respectively when the remaining distance is 20.
    # Axes = [0, 1]

    lin = Motion_LinearIntplCommand()
    trig = Trigger()
    wait = Motion_WaitCondition()

    # Set interpolation command parameters
    lin.axisCount = 2
    lin.SetAxis(0, 0)
    lin.SetAxis(1, 1)

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 500
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    # Set trigger parameters (trigger at 2000 remaining distance)
    trig.triggerAxis = 0
    trig.triggerType = TriggerType.RemainingDistance
    trig.triggerValue = 20

    # Set wait condition parameters
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 0)

    # Execute linear interpolation to position (100, 0)
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 0)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger linear interpolation to position (100, 100)
    sleep(0.001)
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 100)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger linear interpolation to position (0, 100)
    lin.SetTarget(0, 0)
    lin.SetTarget(1, 100)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger linear interpolation to position (0, 0)
    lin.SetTarget(0, 0)
    lin.SetTarget(1, 0)

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
    
