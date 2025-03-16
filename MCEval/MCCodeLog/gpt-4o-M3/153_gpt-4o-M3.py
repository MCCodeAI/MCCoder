
# Axes = [10, 12]
# Inputs = []
# Outputs = []

# Initialize motion commands and event control
posCommand = Motion_PosCommand()
tgrPosCommand = Motion_TriggerPosCommand()
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

# Start an absolute position command for Axis 10 to move to position -800 with a velocity of 600
posCommand.axis = 10
posCommand.target = -800
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set trigger for Axis 10 to move to 300 with a velocity of 1000 when the remaining distance is 400
tgrPosCommand.axis = 10
tgrPosCommand.target = 300
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000
tgrPosCommand.trigger.triggerType = TriggerType.RemainingDistance
tgrPosCommand.trigger.triggerAxis = 10
tgrPosCommand.trigger.triggerValue = 400

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set an event that triggers the movement of Axis 12 to -50 when Axis 10 moves to the position of 100
posEventID = 0
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -50
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Wait for Axis 10 to reach the position of 100 and trigger the event
Wmx3Lib_cm.motion.Wait(10)

# Remove the event after execution
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
