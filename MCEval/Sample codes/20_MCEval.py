# Write python code to Execute an absolute triggered position command.Start an absolute postion command of Axis 0 to position 124 with velocity 1000, when the remaining time is 0, triggers Axis 0 to move to the absolute position of 70 with velocity 2000.
    # Axes = [0]

    pos = Motion_PosCommand()
    trigPos = Motion_TriggerPosCommand()

    # Execute normal motion command
    pos.axis = 0
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.velocity = 1000
    pos.profile.acc = 10000
    pos.profile.dec = 10000
    pos.profile.endVelocity = 1000
    pos.target = 124

    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute trigger motion command
    trigPos.axis = 0
    trigPos.profile.type = ProfileType.Trapezoidal
    trigPos.profile.velocity = 2000
    trigPos.profile.acc = 10000
    trigPos.profile.dec = 10000
    trigPos.target = 70
    trigPos.trigger.triggerType = TriggerType.RemainingTime
    trigPos.trigger.triggerAxis = 0
    trigPos.trigger.triggerValue = 0

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
    if ret != 0:
        print('StarttrigPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

