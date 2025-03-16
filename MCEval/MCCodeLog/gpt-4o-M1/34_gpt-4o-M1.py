
# Axes = [0, 4]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 0 by a relative distance of 110
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create a triggered position command for Axis 4
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Set trigger PosCommand for Axis 4
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 4
tgrPosCommand.target = 100
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create Trigger
# Start when the remaining distance of Axis 0 reaches 30 units
trigger.triggerAxis = 0
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 30
tgrPosCommand.trigger = trigger

# Execute the triggered position command
ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
if ret != 0:
    print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 4 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
