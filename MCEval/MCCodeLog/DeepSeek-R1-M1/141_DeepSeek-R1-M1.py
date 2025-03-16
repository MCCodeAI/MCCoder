
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Start an absolute position command for Axis 10
pos = Motion_PosCommand()
pos.axis = 10
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 600
pos.profile.acc = 10000
pos.profile.dec = 10000
pos.target = -1000

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 starts moving
Wmx3Lib_cm.motion.Wait(10)

# Set up trigger for when remaining distance is 500
trigPos = Motion_TriggerPosCommand()
trigPos.axis = 10
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = -500
trigPos.trigger.triggerType = TriggerType.RemainingDistance
trigPos.trigger.triggerAxis = 10
trigPos.trigger.triggerValue = 500

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StarttrigPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up event for when Axis 10 reaches position 100
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOUT_Motion = CoreMotionEventOutput()

# Configure event input
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Configure event output
eventOUT_Motion.type = CoreMotionEventOutputType.StartPos
eventOUT_Motion startPos.axis = 2
eventOUT_Motion startPos.profile.type = ProfileType.Trapezoidal
eventOUT_Motion startPos.profile.velocity = 600
eventOUT_Motion startPos.profile.acc = 10000
eventOUT_Motion startPos.profile.dec = 10000
eventOUT_Motion startPos.target = -200

# Set up and enable the event
eventID = 0
ret = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOUT_Motion, eventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Wait for all motions to complete
Wmx3Lib_cm.motion.Wait(10)
Wmx3Lib_cm.motion.Wait(2)

# Clean up the event
Wmx3Lib_EventCtl.RemoveEvent(eventID)
