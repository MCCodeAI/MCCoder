
# Axes = [0]
# IOInputs = []
# IOOutputs = []

def main():
    # Create and configure the absolute position command for Axis 0
    pos = Motion_PosCommand()
    pos.axis = 0
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.velocity = 600
    pos.profile.acc = 10000
    pos.profile.dec = 10000
    pos.profile.endVelocity = 600
    pos.target = -66.6

    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartPos error code {}: {}'.format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until Axis 0 stops moving
    Wmx3Lib_cm.motion.Wait(0)

    # Create and configure the trigger position command for Axis 0:
    # When the remaining time of Axis 0 is 100 ms, move to position 66.6 at velocity 1000.
    trigPos = Motion_TriggerPosCommand()
    trigPos.axis = 0
    trigPos.profile.type = ProfileType.Trapezoidal
    trigPos.profile.velocity = 1000
    trigPos.profile.acc = 10000
    trigPos.profile.dec = 10000
    trigPos.target = 66.6

    trigPos.trigger.triggerType = TriggerType.RemainingTime
    trigPos.trigger.triggerAxis = 0
    trigPos.trigger.triggerValue = 100  # Trigger when remaining time is 100 ms

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
    if ret != 0:
        print('StartPos_Trigger error code {}: {}'.format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until Axis 0 completes the triggered motion
    Wmx3Lib_cm.motion.Wait(0)

if __name__ == '__main__':
    main()
