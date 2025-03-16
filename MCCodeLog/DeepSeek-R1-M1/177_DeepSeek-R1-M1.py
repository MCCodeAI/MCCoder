
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
tgrPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Move Axis 10 to position -800 with velocity 600
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = -800
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
Wmx3Lib_cm.motion.Wait(10)

# Set up trigger for DistanceToTarget = 200
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerAxis = 10
trigger.triggerValue = 200

tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 10
tgrPosCommand.target = 300
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000
tgrPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
Wmx3Lib_cm.motion.Wait(10)

# Set up event trigger for Axis 10 reaching position 100
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Create command for Axis 12 to move to -50
posCommand12 = Motion_PosCommand()
posCommand12.profile.type = ProfileType.Trapezoidal
posCommand12.axis = 12
posCommand12.target = -50
posCommand12.profile.velocity = 1000
posCommand12.profile.acc = 10000
posCommand12.profile.dec = 10000

# Set up event
eventCtl = EventControl(Wmx3Lib)
eventCtl.CreateEvent(eventIN_Motion, posCommand12)

# Wait for the event to trigger and execute
Wmx3Lib_cm.motion.Wait(12)
