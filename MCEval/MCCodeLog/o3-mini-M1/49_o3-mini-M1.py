
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def main():
    # Create motion command objects
    pos = Motion_PosCommand()
    tpos = Motion_TriggerPosCommand()
    wait = Motion_WaitCondition()

    # -------------------------------
    # Set parameters for position command for Axis 9
    pos.axis = 9
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.acc = 1000
    pos.profile.dec = 1000
    pos.target = 180
    pos.profile.velocity = 30

    # Start the initial motion on Axis 9
    ret = Wmx3Lib_cm.motion.StartPos(pos)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # -------------------------------
    # Set common parameters for the triggered motion command
    tpos.axis = 9
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.acc = 1000
    tpos.profile.dec = 1000
    tpos.target = 180

    # Configure the trigger condition: when the CompletedTime equals 700ms
    tpos.trigger.triggerAxis = 9
    tpos.trigger.triggerType = TriggerType.CompletedTime
    tpos.trigger.triggerValue = 700

    # Set wait condition parameters to wait until Axis 9 is ready for override
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 9)

    # -------------------------------
    # Sequence of velocity overrides to be triggered:
    # 1st override: 60, 2nd override: 90, 3rd override: 60, 4th override: 30
    velocity_sequence = [60, 90, 60, 30]
    for velocity in velocity_sequence:
        tpos.profile.velocity = velocity
        ret = Wmx3Lib_cm.motion.StartPos_Trigger(tpos)
        if ret != 0:
            print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the triggered motion command has taken effect before continuing.
        ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
        if ret != 0:
            print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

    # -------------------------------
    # Wait until the motion on Axis 9 has fully completed.
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
