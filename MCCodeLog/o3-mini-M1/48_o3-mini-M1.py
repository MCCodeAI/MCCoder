
# Axes = [8]
# IOInputs = []
# IOOutputs = []

def main():
    # Move Axis 8 by a distance of 30 at a velocity of 1000.
    pos = Motion_PosCommand()
    pos.axis = 8
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.velocity = 1000
    pos.profile.acc = 10000
    pos.profile.dec = 10000
    pos.target = 30

    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Trigger Axis 8 to move a distance of -30 when the remaining time equals 10.
    tpos = Motion_TriggerPosCommand()
    tpos.axis = 8
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.velocity = 1000
    tpos.profile.acc = 10000
    tpos.profile.dec = 10000
    tpos.target = -30
    tpos.trigger.triggerAxis = 8
    tpos.trigger.triggerType = TriggerType.RemainingTime
    tpos.trigger.triggerValue = 10

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the triggered motion to start (waiting for the axis to be overridable)
    wait = Motion_WaitCondition()
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 8)

    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving after the trigger motion.
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Move Axis 8 by a distance of 60 after waiting for it to be overridable.
    pos = Motion_PosCommand()
    pos.axis = 8
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.velocity = 1000
    pos.profile.acc = 10000
    pos.profile.dec = 10000
    pos.target = 60

    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code (60) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving.
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code (60) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Trigger Axis 8 to move a distance of -60 after waiting for it to be overridable.
    tpos = Motion_TriggerPosCommand()
    tpos.axis = 8
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.velocity = 1000
    tpos.profile.acc = 10000
    tpos.profile.dec = 10000
    tpos.target = -60
    tpos.trigger.triggerAxis = 8
    tpos.trigger.triggerType = TriggerType.RemainingTime
    tpos.trigger.triggerValue = 10

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code (-60) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the triggered motion to start.
    wait.SetAxis(0, 8)
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code (-60) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving.
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Final Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
