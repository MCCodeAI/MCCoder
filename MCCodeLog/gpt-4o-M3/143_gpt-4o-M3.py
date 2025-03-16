
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Initialize motion commands and triggers
posCommand = Motion_PosCommand()
triggerPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Start an absolute motion command for Axis 10 to position -1000 with velocity 600
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.target = -1000
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up a trigger for when the remaining distance is 500
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 500

# Trigger Axis 10 to move to -300 with velocity 1000 when previous trigger is met
triggerPosCommand.axis = 10
triggerPosCommand.profile.type = ProfileType.Trapezoidal
triggerPosCommand.target = -300
triggerPosCommand.profile.velocity = 1000
triggerPosCommand.profile.acc = 10000
triggerPosCommand.profile.dec = 10000
triggerPosCommand.trigger = trigger
ret = Wmx3Lib_cm.motion.StartPos_Trigger(triggerPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the first set of motions to complete on Axis 10
Wmx3Lib_cm.motion.Wait(10)

# Set an event to trigger Axis 2 move to -200 when Axis 10 reaches position 100
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
eventID = 0

# Set event input
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Set event output
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 2
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -200
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input and output events with event ID
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Wait for the triggered movements to complete on Axis 2
Wmx3Lib_cm.motion.Wait(2)

# Remove the event after execution
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
