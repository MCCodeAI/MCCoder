
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Define motion commands and triggers
posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Set up the event to trigger Axis 12 to start moving to position 80 when Axis 10 reaches position 400
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Configure the motion for Axis 12
posCommand.axis = 12
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000  # Assuming a velocity for Axis 12
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 80

# Start the motion for Axis 12 when the event is triggered
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up the absolute position command for Axis 10 to move to position 800 with velocity 600
posCommand.axis = 10
posCommand.profile.velocity = 600
posCommand.target = 800

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up the trigger for Axis 10 to move to position 300 with velocity 1000 when the distance to target is 200
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 200

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to stop moving
Wmx3Lib_cm.motion.Wait(10)
