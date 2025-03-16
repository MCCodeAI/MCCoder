
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Define the motion command for Axis 10
posCommand_Axis10 = Motion_PosCommand()
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000
posCommand_Axis10.target = -1000

# Start the absolute position command for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define the trigger motion command for Axis 10
trigPosCommand_Axis10 = Motion_TriggerPosCommand()
trigPosCommand_Axis10.axis = 10
trigPosCommand_Axis10.profile.type = ProfileType.Trapezoidal
trigPosCommand_Axis10.profile.velocity = 1000
trigPosCommand_Axis10.profile.acc = 10000
trigPosCommand_Axis10.profile.dec = 10000
trigPosCommand_Axis10.target = -300
trigPosCommand_Axis10.trigger.triggerType = TriggerType.RemainingDistance
trigPosCommand_Axis10.trigger.triggerAxis = 10
trigPosCommand_Axis10.trigger.triggerValue = 500

# Start the trigger motion command for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define the event input for Axis 10 to trigger Axis 2
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Define the motion command for Axis 2
posCommand_Axis2 = Motion_PosCommand()
posCommand_Axis2.axis = 2
posCommand_Axis2.profile.type = ProfileType.Trapezoidal
posCommand_Axis2.profile.velocity = 600
posCommand_Axis2.profile.acc = 10000
posCommand_Axis2.profile.dec = 10000
posCommand_Axis2.target = -200

# Set the event to trigger the movement of Axis 2
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, posCommand_Axis2, 0)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(0, 1)

# Wait for Axis 10 to reach the target position and stop
Wmx3Lib_cm.motion.Wait(10)

# Wait for Axis 2 to reach the target position and stop
Wmx3Lib_cm.motion.Wait(2)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(0)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return
