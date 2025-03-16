
# Axes = [1, 5]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Move Axis 1 to absolute position -110
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = -110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up triggered absolute command for Axis 5
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 5
tgrPosCommand.target = -100  # Absolute target position
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Configure trigger condition (Axis 1 remaining distance = 30)
trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 30
tgrPosCommand.trigger = trigger

# Execute triggered command
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to complete motion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
