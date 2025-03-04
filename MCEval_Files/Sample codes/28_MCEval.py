# Write python code to Execute a sequence of motion commands using trigger motion functions and Wait functions.Move Axis 0 as 100 distance with 1000 velocity, and trigger it to move as -100 distance when the remaining time is 0, and then move as 200 distance, and -200 distance after waiting it to be overridable.
    # Axes = [0]

    pos = Motion_PosCommand()
    tpos = Motion_TriggerPosCommand()
    wait = Motion_WaitCondition()

    # Set position command parameters
    pos.axis = 0
    pos.profile.type = ProfileType.Trapezoidal;
    pos.profile.velocity = 1000
    pos.profile.acc = 10000
    pos.profile.dec = 10000

    # Set triggered position command parameters
    tpos.axis = 0
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.velocity = 1000
    tpos.profile.acc = 10000
    tpos.profile.dec = 10000
    tpos.trigger.triggerAxis = 0
    tpos.trigger.triggerType = TriggerType.RemainingTime
    tpos.trigger.triggerValue = 0

    # Set wait condition parameters, waiting Axis 0 to be overridable.
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 0)

    # Execute motion to move axis forward 100
    pos.target = 100

    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to move axis backward 100 at the end of the previous motion
    tpos.target = -100

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to move axis forward 200 at the end of the previous motion
    tpos.target = 200

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to move axis backward 20000 at the end of the previous motion
    tpos.target = -200
    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
