
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

def main():
    # ---------------------------
    # Part 1:
    # Set an event so that when Axis 10 reaches the position 400,
    # Axis 12 will execute an absolute position command to move to 80.
    #
    # Create a triggered position command for Axis 12.
    trigCmdAxis12 = Motion_TriggerPosCommand()
    trigCmdAxis12.axis = 12
    trigCmdAxis12.profile.type = ProfileType.Trapezoidal
    trigCmdAxis12.profile.velocity = 1000
    trigCmdAxis12.profile.acc = 10000
    trigCmdAxis12.profile.dec = 10000
    trigCmdAxis12.target = 80

    # Configure the trigger event:
    # When Axis 10 equals position 400, trigger the command.
    # (Assuming TriggerType.EqualPos is supported)
    trigCmdAxis12.trigger.triggerAxis = 10
    trigCmdAxis12.trigger.triggerType = TriggerType.EqualPos
    trigCmdAxis12.trigger.triggerValue = 400

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCmdAxis12)
    if ret != 0:
        print('StartPos_Trigger for Axis 12 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 12 to complete its motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 1
    axisSel.SetAxis(0, 12)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel for Axis 12 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # ---------------------------
    # Part 2:
    # Start an absolute position command for Axis 10:
    # Move Axis 10 to 800 with a velocity of 600.
    # When the remaining distance is 200, trigger Axis 10 to move to 300 with a velocity of 1000.
    #
    # Start the first absolute motion command for Axis 10.
    posCmdAxis10 = Motion_PosCommand()
    posCmdAxis10.axis = 10
    posCmdAxis10.profile.type = ProfileType.Trapezoidal
    posCmdAxis10.profile.velocity = 600
    posCmdAxis10.profile.acc = 10000
    posCmdAxis10.profile.dec = 10000
    posCmdAxis10.target = 800

    ret = Wmx3Lib_cm.motion.StartPos(posCmdAxis10)
    if ret != 0:
        print('StartPos for Axis 10 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Immediately set the triggered command for Axis 10.
    trigPosCmdAxis10 = Motion_TriggerPosCommand()
    trigPosCmdAxis10.axis = 10
    trigPosCmdAxis10.profile.type = ProfileType.Trapezoidal
    trigPosCmdAxis10.profile.velocity = 1000
    trigPosCmdAxis10.profile.acc = 10000
    trigPosCmdAxis10.profile.dec = 10000
    trigPosCmdAxis10.target = 300

    # Configure the trigger so that when the distance remaining for Axis 10 is 200,
    # the trigger command will be activated.
    trigPosCmdAxis10.trigger.triggerAxis = 10
    trigPosCmdAxis10.trigger.triggerType = TriggerType.DistanceToTarget
    trigPosCmdAxis10.trigger.triggerValue = 200

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCmdAxis10)
    if ret != 0:
        print('StartPos_Trigger for Axis 10 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 10 to complete its motion.
    axisSel2 = AxisSelection()
    axisSel2.axisCount = 1
    axisSel2.SetAxis(0, 10)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel2)
    if ret != 0:
        print('Wait_AxisSel for Axis 10 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
