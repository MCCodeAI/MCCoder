
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Define the motion command for Axis 10
posCommandAxis10 = Motion_PosCommand()
posCommandAxis10.axis = 10
posCommandAxis10.profile.type = ProfileType.Trapezoidal
posCommandAxis10.profile.velocity = 600
posCommandAxis10.profile.acc = 10000
posCommandAxis10.profile.dec = 10000
posCommandAxis10.target = -800

# Start the absolute position command for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommandAxis10)
if ret != 0:
    print('StartPos error code for Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach the target position
Wmx3Lib_cm.motion.Wait(10)

# Define the trigger motion command for Axis 10
trigPosCommandAxis10 = Motion_TriggerPosCommand()
trigPosCommandAxis10.axis = 10
trigPosCommandAxis10.profile.type = ProfileType.Trapezoidal
trigPosCommandAxis10.profile.velocity = 1000
trigPosCommandAxis10.profile.acc = 10000
trigPosCommandAxis10.profile.dec = 10000
trigPosCommandAxis10.target = 300
trigPosCommandAxis10.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommandAxis10.trigger.triggerAxis = 10
trigPosCommandAxis10.trigger.triggerValue = 200

# Start the triggered position command for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommandAxis10)
if ret != 0:
    print('StartPos_Trigger error code for Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach the position of 100
Wmx3Lib_cm.motion.Wait(10)

# Define the motion command for Axis 12
posCommandAxis12 = Motion_PosCommand()
posCommandAxis12.axis = 12
posCommandAxis12.profile.type = ProfileType.Trapezoidal
posCommandAxis12.profile.velocity = 500
posCommandAxis12.profile.acc = 5000
posCommandAxis12.profile.dec = 5000
posCommandAxis12.target = -50

# Set an event to trigger the movement of Axis 12 when Axis 10 reaches position 100
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Start the motion command for Axis 12
ret = Wmx3Lib_cm.motion.StartPos(posCommandAxis12)
if ret != 0:
    print('StartPos error code for Axis 12: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to complete its motion
Wmx3Lib_cm.motion.Wait(12)
