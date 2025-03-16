
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Start an absolute position command for Axis 10 to move to position -1000 with a velocity of 600
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = -1000
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to start moving
Wmx3Lib_cm.motion.Wait(10)

# Set a trigger to move Axis 10 to -500 with a velocity of 1000 when the remaining distance is 500
tgrPosCommand = Motion_TriggerPosCommand()
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 10
tgrPosCommand.target = -500
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

trigger = Trigger()
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 500

tgrPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to complete the motion
Wmx3Lib_cm.motion.Wait(10)

# Set an event that triggers to start the movement of Axis 2 to -200 when Axis 10 moves to the position of 100
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 0

# Set the event input
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Set the event output to move Axis 2 to -200
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 2
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -200
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and let the system assign an event ID
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(Event_ID, 1)

# Wait for the event to trigger and complete
Wmx3Lib_cm.motion.Wait(2)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(Event_ID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
