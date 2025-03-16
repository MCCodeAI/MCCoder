# Write python code to Execute an absolute position triggered linear interpolation motion command.Control Axis 0 and Axis 1 to linearly interpolate to (100, 100) at a velocity of 1000 with acceleration and deceleration of 10000. Wait for 1 millisecond, then execute the trigger linear interpolation motion command. When the remaining distance is 30, trigger Axis 0 and Axis 1 to (200, 0). After previous interpolation completes, when the remaining distance is 30, trigger Axis 0 and Axis 1 to (200, 0).And using same trigger and condition to trigger Axis 0 and Axis 1 to (300, 100),(400, 0) and (500, 100).
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

    lin.SetTarget(0, 100)
    lin.SetTarget(1, 100)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    sleep(0.001)

    lin.SetTarget(0, 200)
    lin.SetTarget(1, 0)

    trig.triggerAxis = 0
    trig.triggerType = TriggerType.RemainingDistance
    trig.triggerValue = 30

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the first interpolation completes before setting trigger for third interpolation
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).commandReady == 1):
            break
        sleep(0.1)

    lin.SetTarget(0, 300)
    lin.SetTarget(1, 100)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the second interpolation completes before setting trigger for fourth interpolation
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).commandReady == 1):
            break
        sleep(0.1)

    lin.SetTarget(0, 400)
    lin.SetTarget(1, 0)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
    if ret != 0:
        print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the third interpolation completes before setting trigger for fifth interpolation
    while True:
        # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
        ret, CmStatus = Wmx3Lib_cm.GetStatus()
        if (CmStatus.GetAxesStatus(0).commandReady == 1):
            break
        sleep(0.1)

    lin.SetTarget(0, 500)
    lin.SetTarget(1, 100)

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
    
