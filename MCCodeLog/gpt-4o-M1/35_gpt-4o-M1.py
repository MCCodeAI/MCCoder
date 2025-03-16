
# Axes = [1, 5]

posCommand = Motion_PosCommand()
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Move Axis 1 to the specified position.
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = -110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set trigger PosCommand for Axis 5.
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 5
tgrPosCommand.target = -100
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create Trigger
# Start when the remaining distance of Axis 1 reaches 30 units.
trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 30
tgrPosCommand.trigger = trigger
ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
if ret != 0:
    print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 1 and Axis 5 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
