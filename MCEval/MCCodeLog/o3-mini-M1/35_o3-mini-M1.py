
# Axes = [1, 5]
# IOInputs = []
# IOOutputs = []

def main():
    # Create the trigger condition:
    # Axis 1 must have 30 units remaining to its target.
    trigger = Trigger()
    trigger.triggerAxis = 1
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 30

    # Create the triggered absolute position command for Axis 5.
    # When the trigger condition is met, Axis 5 will move to -100 at a velocity of 1000.
    tgrPosCommand = Motion_TriggerPosCommand()
    tgrPosCommand.profile.type = ProfileType.Trapezoidal
    tgrPosCommand.axis = 5
    tgrPosCommand.target = -100
    tgrPosCommand.profile.velocity = 1000
    tgrPosCommand.profile.acc = 10000
    tgrPosCommand.profile.dec = 10000
    tgrPosCommand.trigger = trigger

    # Create an absolute position command for Axis 1.
    # Axis 1 will move an absolute distance of -110 at a velocity of 1000.
    posCommandAxis1 = Motion_PosCommand()
    posCommandAxis1.profile.type = ProfileType.Trapezoidal
    posCommandAxis1.axis = 1
    posCommandAxis1.target = -110
    posCommandAxis1.profile.velocity = 1000
    posCommandAxis1.profile.acc = 10000
    posCommandAxis1.profile.dec = 10000

    # Start the movement for Axis 1.
    ret = Wmx3Lib_cm.motion.StartPos(posCommandAxis1)
    if ret != 0:
        print('StartPos error for Axis 1: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Start the triggered command for Axis 5.
    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
    if ret != 0:
        print('StartPos_Trigger error for Axis 5: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until both Axis 1 and Axis 5 finish moving.
    # This ensures we wait for axes to become idle after each complete motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)  # First monitored axis: Axis 1.
    axisSel.SetAxis(1, 5)  # Second monitored axis: Axis 5.

    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
