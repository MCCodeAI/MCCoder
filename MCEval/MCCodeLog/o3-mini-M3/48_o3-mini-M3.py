
import time

# Axes = [8]
# IOInputs = []
# IOOutputs = []

def main():
    # *******************************
    # Set servo on for Axis 8 to avoid servo off errors
    # *******************************
    ret = Wmx3Lib_cm.axisControl.SetServoOn(8, 1)
    if ret != 0:
        print('SetServoOn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 servo is turned on
    counter = 1000
    while counter > 0:
        st = Wmx3Lib_cm.GetStatus()
        # Assuming st.AxesStatus is indexed such that index 8 corresponds to Axis 8.
        # Adjust the index if needed.
        if hasattr(st.AxesStatus[8], 'ServoOn') and st.AxesStatus[8].ServoOn:
            break
        time.sleep(0.01)  # wait for 10ms
        counter -= 1
    if counter == 0:
        print("Axis 8 servo did not turn on.")
        return

    # Create command objects for axis motions and waiting
    pos = Motion_PosCommand()
    tpos = Motion_TriggerPosCommand()
    wait = Motion_WaitCondition()

    # *******************************
    # 1. Move Axis 8 by +30 at velocity 1000
    # *******************************
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

    # Wait until Axis 8 stops moving (after this single motion)
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # *******************************
    # 2. Trigger motion: Move Axis 8 by -30 when remaining time is 10
    # *******************************
    tpos.axis = 8
    tpos.profile.type = ProfileType.Trapezoidal
    tpos.profile.velocity = 1000
    tpos.profile.acc = 10000
    tpos.profile.dec = 10000
    tpos.trigger.triggerAxis = 8
    tpos.trigger.triggerType = TriggerType.RemainingTime
    tpos.trigger.triggerValue = 10
    tpos.target = -30

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the trigger motion executes (do not wait in the middle of continuous motion)
    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Also wait until Axis 8 has completely stopped before starting the next motion
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # *******************************
    # 3. Move Axis 8 by +60 at velocity 1000
    # *******************************
    pos.target = 60  # reusing pos for next command; axis and profile remain the same
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # *******************************
    # 4. Trigger motion: Move Axis 8 by -60 when waiting for overridable condition
    # *******************************
    # Set the wait condition to check if the motion is ready for an override
    wait.waitConditionType = Motion_WaitConditionType.MotionStartedOverrideReady
    wait.axisCount = 1
    wait.SetAxis(0, 8)  # Wait on Axis 8

    tpos.target = -60  # update trigger command target

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tpos)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait_WaitCondition(wait)
    if ret != 0:
        print('Wait_WaitCondition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Final wait until Axis 8 stops completely
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Final Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
