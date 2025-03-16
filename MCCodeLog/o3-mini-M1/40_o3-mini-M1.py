
# Axes = [0]
# IOInputs = []
# IOOutputs = []

def main():
    # Create the absolute position command for Axis 0 to move to -66.6 at 600 velocity.
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
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Without waiting (continuous motion) proceed to set up the triggered motion.
    # Trigger: when the remaining time of Axis 0 is 100 ms,
    # start a new absolute position command for Axis 0 to move to 66.6 at 1000 velocity.
    trigPos = Motion_TriggerPosCommand()
    trigPos.axis = 0
    trigPos.profile.type = ProfileType.Trapezoidal
    trigPos.profile.velocity = 1000
    trigPos.profile.acc = 10000
    trigPos.profile.dec = 10000
    trigPos.target = 66.6
    trigPos.trigger.triggerType = TriggerType.RemainingTime
    trigPos.trigger.triggerAxis = 0
    trigPos.trigger.triggerValue = 100  # 100 ms remaining time

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
    if ret != 0:
        print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 0 to complete all movements before ending.
    Wmx3Lib_cm.motion.Wait(0)

if __name__ == '__main__':
    main()
