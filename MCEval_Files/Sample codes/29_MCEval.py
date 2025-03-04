# Write python code to Execute a sequence of motion commands using trigger motion functions and Wait functions. Move Axis 0 to position 180 with 20 velocity, and trigger the velocity override to 40, 60, 40, and 20 respectively when the completed time is 1s.
    # Axes = [0]

    pos = Motion_PosCommand()
    tpos = Motion_TriggerPosCommand()
    wait = Motion_WaitCondition()

    # Set position command parameters
    pos.axis = 0
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.acc = 1000
    pos.profile.dec = 1000
    pos.target = 180

    # Set triggered position command parameters
    tpos.axis = 0
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.acc = 1000
    tpos.profile.dec = 1000
    tpos.trigger.triggerAxis = 0
    tpos.trigger.triggerType = TriggerType.CompletedTime
    tpos.trigger.triggerValue = 1000
    tpos.target = 180

    # Set wait condition parameters
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 0)

    # Execute motion to move axis forward 20
    pos.profile.velocity = 20

    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to change axis velocity
    tpos.profile.velocity = 40

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
    if ret != 0:
        print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to change axis velocity
    tpos.profile.velocity = 60

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
    if ret != 0:
        print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to change axis velocity
    tpos.profile.velocity = 40

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
    if ret != 0:
        print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until trigger motion executes
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion to change axis velocity
    tpos.profile.velocity = 20
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
    if ret != 0:
        print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
