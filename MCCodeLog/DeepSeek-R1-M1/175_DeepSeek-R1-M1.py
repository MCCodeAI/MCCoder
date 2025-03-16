
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Move Axis 10 to 800 with velocity 600
posCommand = Motion_PosCommand()
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 800

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create trigger for Axis 10 when distance to target is 200
trigger = Trigger()
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerAxis = 10
trigger.triggerValue = 200

# Create triggered position command for Axis 10 to move to 300 with velocity 1000
trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create event input for Axis 10 position equal to 400
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Create position command for Axis 12 to move to 80
posCommand12 = Motion_PosCommand()
posCommand12.axis = 12
posCommand12.profile.type = ProfileType.Trapezoidal
posCommand12.profile.velocity = 1000  # Default velocity
posCommand12.profile.acc = 10000
posCommand12.profile.dec = 10000
posCommand12.target = 80

# Set event input and execute command
ret = Wmx3Lib_EventCtl.SetEventInput(0, eventIN_Motion)
if ret != 0:
    print('SetEventInput error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.StartPos(posCommand12)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for all motions to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 10)
axisSel.SetAxis(1, 12)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
