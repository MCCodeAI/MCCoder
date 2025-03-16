
# Axes = [1, 5]
# IOInputs = []
# IOOutputs = []

# Create a command value for Axis 1 to move to an absolute position of -110 with a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = -110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 1 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up a triggered position command for Axis 5.
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Configure the triggered position command for Axis 5.
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 5
tgrPosCommand.target = -100
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create a trigger condition for Axis 1.
trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 30
tgrPosCommand.trigger = trigger

# Execute the triggered position command for Axis 5.
ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
if ret != 0:
    print('StartMov_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 and Axis 5 to complete their motions.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
