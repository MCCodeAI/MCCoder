
# Axes = [10, 12]
# Inputs = []
# Outputs = []

# Initialize motion command objects
posCommand = Motion_PosCommand()
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Start an absolute position command for Axis 10 to move to position 800 with a velocity of 600
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

# Set trigger position command for Axis 10 to move to 300 with a velocity of 1000 when the distance to target is 200
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 10
tgrPosCommand.target = 300
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create Trigger
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 200
tgrPosCommand.trigger = trigger
ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set an event that triggers the movement of Axis 12 to 80 when Axis 10 moves to the position of 400
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 0

# Set the event input
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Set the event output
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

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Wait for Axis 12 to complete its motion
Wmx3Lib_cm.motion.Wait(12)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
