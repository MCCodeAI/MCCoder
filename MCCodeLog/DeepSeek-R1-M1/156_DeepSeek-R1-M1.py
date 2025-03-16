
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Move Axis 10 to -800 with velocity 600
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

# Set trigger condition: DistanceToTarget = 200
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerAxis = 10
trigger.triggerValue = 200

# Triggered motion: Move Axis 10 to 300 with velocity 1000
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.axis = 10
trigPosCommand.target = 300
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to complete the motion
Wmx3Lib_cm.motion.Wait(10)

# Set up event for when Axis 10 reaches position 100
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# When event is triggered, start Axis 12 movement
if eventIN_Motion.inputFunction == CoreMotionEventInputType.EqualPos:
    posCommand.axis = 12
    posCommand.target = -50
    posCommand.profile.velocity = 600
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 12 to complete the motion
    Wmx3Lib_cm.motion.Wait(12)
