
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Execute an absolute triggered position command for Axis 10
posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()

# Execute normal motion command for Axis 10
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = -800

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion command for Axis 10
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger.triggerType = TriggerType.RemainingDistance
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 400

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set an event that triggers the movement of Axis 12 when Axis 10 reaches position 100
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Set the event input for Axis 10 to equal position 100
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Set the event output to start the movement of Axis 12
eventOut_Motion.type = CoreMotionEventOutputType.StartPos
eventOut_Motion.startPos.axis = 12
eventOut_Motion.startPos.profile.type = ProfileType.Trapezoidal
eventOut_Motion.startPos.profile.velocity = 500
eventOut_Motion.startPos.profile.acc = 5000
eventOut_Motion.startPos.profile.dec = 5000
eventOut_Motion.startPos.target = -50

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, 0)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(0, 1)

# Wait for Axis 10 to stop moving
Wmx3Lib_cm.motion.Wait(10)

# Wait for Axis 12 to stop moving
Wmx3Lib_cm.motion.Wait(12)

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(0)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return
