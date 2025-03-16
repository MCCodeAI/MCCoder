
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Motion command for Axis 10
posCommand_Axis10 = Motion_PosCommand()
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.target = -1000
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000

# Start initial motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code for Axis 10 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to initially start moving
Wmx3Lib_cm.motion.Wait(10)

# Trigger condition for Axis 10 when remaining distance is 500
trigger_Axis10 = Trigger()
trigger_Axis10.triggerAxis = 10
trigger_Axis10.triggerType = TriggerType.RemainingDistance
trigger_Axis10.triggerValue = 500

# New command for Axis 10
trigPosCommand_Axis10 = Motion_TriggerPosCommand()
trigPosCommand_Axis10.axis = 10
trigPosCommand_Axis10.profile.type = ProfileType.Trapezoidal
trigPosCommand_Axis10.target = -500
trigPosCommand_Axis10.profile.velocity = 1000
trigPosCommand_Axis10.profile.acc = 10000
trigPosCommand_Axis10.profile.dec = 10000
trigPosCommand_Axis10.trigger = trigger_Axis10

# Start triggered motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code for Axis 10 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Event to trigger Axis 2 movement when Axis 10 reaches position 100
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID_Axis10_Axis2 = 0

# Set the event input
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Set the event output for starting Axis 2 motion
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 2
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -200
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID_Axis10_Axis2)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable event
Wmx3Lib_EventCtl.EnableEvent(posEventID_Axis10_Axis2, 1)

# Wait for Axis 10 to complete its motion to position -500
Wmx3Lib_cm.motion.Wait(10)

# Additional wait for Axis 2 to complete its movement
Wmx3Lib_cm.motion.Wait(2)

# Remove the event after execution
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID_Axis10_Axis2)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
