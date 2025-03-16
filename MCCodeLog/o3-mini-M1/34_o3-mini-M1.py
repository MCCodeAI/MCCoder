
# Axes = [0, 4]
# IOInputs = []
# IOOutputs = []

def main():
    # Start a relative move command on Axis 0 with a distance of 110 and velocity 1000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 110
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Create a triggered relative move command on Axis 4 with a distance of 100 and velocity 1000.
    # The trigger is activated when Axis 0 has 30 units remaining to its target.
    tgrPosCommand = Motion_TriggerPosCommand()
    tgrPosCommand.profile.type = ProfileType.Trapezoidal
    tgrPosCommand.axis = 4
    tgrPosCommand.target = 100
    tgrPosCommand.profile.velocity = 1000
    tgrPosCommand.profile.acc = 10000
    tgrPosCommand.profile.dec = 10000

    trigger = Trigger()
    trigger.triggerAxis = 0
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 30
    tgrPosCommand.trigger = trigger

    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait a little while for the trigger condition to be evaluated (do not interrupt the continuous motion).
    Wmx3Lib_cm.motion.Wait(1)

    # Block until both the motion of Axis 0 (the trigger source) and Axis 4 (the triggered command) are completed.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 4)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
