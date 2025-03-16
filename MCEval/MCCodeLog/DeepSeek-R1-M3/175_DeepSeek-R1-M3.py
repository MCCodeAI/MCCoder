
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use a different Event ID to avoid conflict
posEventID = 2  # Changed from 1 to avoid ID conflict

# Set the event input for Axis 10 to equal position 400
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Start a position command for Axis 12 to move to 80
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 80
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Wait for the event to be properly set
# Using a proper wait function instead of sleep
ret = Wmx3Lib_cm.motion.Wait(0.1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start absolute position command for Axis 10 to 800 with velocity 600
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = 800
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach position 400 (this will trigger Axis 12 movement)
axisSel = AxisSelection()
axisSel.axisCount = 1
axisSel.SetAxis(0, 10)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger command for Axis 10 when distance to target is 200
# Using a separate event for this trigger
trigEventID = 3  # Different ID for the trigger event

trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 10
trigPosCommand.target = 300  # Target position
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000

trigger = Trigger()
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerAxis = 10
trigger.triggerValue = 200  # Distance to target
trigPosCommand.trigger = trigger

# Set up a new event for the trigger
eventIN_Trigger = CoreMotionEventInput()
eventOUT_Trigger = CoreMotionEventOutput()

eventIN_Trigger.inputFunction = CoreMotionEventInputType.Trigger
eventIN_Trigger.trigger.triggerType = TriggerType.DistanceToTarget
eventIN_Trigger.trigger.triggerAxis = 10
eventIN_Trigger.trigger.triggerValue = 200

eventOUT_Trigger.type = CoreMotionEventOutputType.StartSinglePos
eventOUT_Trigger.startSinglePos.axis = 10
eventOUT_Trigger.startSinglePos.type = ProfileType.Trapezoidal
eventOUT_Trigger.startSinglePos.target = 300
eventOUT_Trigger.startSinglePos.velocity = 1000
eventOUT_Trigger.startSinglePos.acc = 10000
eventOUT_Trigger.startSinglePos.dec = 10000

ret, trigEvent_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Trigger, eventOUT_Trigger, trigEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(trigEventID, 1)

# Wait for all motions to complete
ret = Wmx3Lib_cm.motion.Wait(10)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Remove events
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return

ret = Wmx3Lib_EventCtl.RemoveEvent(trigEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
