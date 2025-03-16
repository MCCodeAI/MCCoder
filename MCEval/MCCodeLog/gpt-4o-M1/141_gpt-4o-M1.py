
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Initialize motion command for Axis 10
posCommand_Axis10 = Motion_PosCommand()
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000
posCommand_Axis10.target = -1000

# Start the motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code for Axis 10 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up a trigger for Axis 10 to move to -500 when remaining distance is 500
trigPosCommand_Axis10 = Motion_TriggerPosCommand()
trigPosCommand_Axis10.axis = 10
trigPosCommand_Axis10.profile.type = ProfileType.Trapezoidal
trigPosCommand_Axis10.profile.velocity = 1000
trigPosCommand_Axis10.profile.acc = 10000
trigPosCommand_Axis10.profile.dec = 10000
trigPosCommand_Axis10.target = -500
trigPosCommand_Axis10.trigger.triggerType = TriggerType.RemainingDistance
trigPosCommand_Axis10.trigger.triggerAxis = 10
trigPosCommand_Axis10.trigger.triggerValue = 500

# Start the trigger motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code for Axis 10 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up an event to trigger Axis 2 to move to -200 when Axis 10 reaches position 100
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

eventOut_Motion_Axis2 = CoreMotionEventOutput()
eventOut_Motion_Axis2.type = CoreMotionEventOutputType.StartMov
eventOut_Motion_Axis2.startMov.axis = 2
eventOut_Motion_Axis2.startMov.profile.type = ProfileType.Trapezoidal
eventOut_Motion_Axis2.startMov.profile.velocity = 1000
eventOut_Motion_Axis2.startMov.profile.acc = 10000
eventOut_Motion_Axis2.startMov.profile.dec = 10000
eventOut_Motion_Axis2.startMov.target = -200

# Set the event
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
ret, eventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion_Axis2, 0)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Wait for Axis 10 to complete its motion
Wmx3Lib_cm.motion.Wait(10)

# Wait for Axis 2 to complete its motion
Wmx3Lib_cm.motion.Wait(2)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return
