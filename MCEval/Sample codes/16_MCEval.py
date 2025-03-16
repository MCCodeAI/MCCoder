# Write python code to Start a relative triggered position command of Axis 1 with 180 distance and velocity of 1000, and the triggered condition is the remaining distance for Axis 0 to the target position is 30 while it moves a relative 100 distance.
    # Axes = [0, 1]

    posCommand = Motion_PosCommand()
    tgrPosCommand = Motion_TriggerPosCommand()
    trigger = Trigger()

    # Move the motor to the specified position.
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Set trigger PosCommand.
    tgrPosCommand.profile.type = ProfileType.Trapezoidal
    tgrPosCommand.axis = 1
    tgrPosCommand.target = 180
    tgrPosCommand.profile.velocity = 1000
    tgrPosCommand.profile.acc = 10000
    tgrPosCommand.profile.dec = 10000

    # Create Trigger
    # Start when the remaining distance of 0 axis reaches 30 pulse.
    trigger.triggerAxis = 0
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 30
    tgrPosCommand.trigger = trigger
    ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
    if ret != 0:
        print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    Wmx3Lib_cm.motion.Wait(1)

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
        
