
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Initialize motion commands for Axis 10
posCommand_Axis10 = Motion_PosCommand()
triggerCommand_Axis10 = Motion_TriggerPosCommand()

# Set initial motion parameters for Axis 10
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000
posCommand_Axis10.target = -800

# Start the initial motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Configure trigger motion for Axis 10 when remaining distance is 400
triggerCommand_Axis10.axis = 10
triggerCommand_Axis10.profile.type = ProfileType.Trapezoidal
triggerCommand_Axis10.profile.velocity = 1000
triggerCommand_Axis10.profile.acc = 10000
triggerCommand_Axis10.profile.dec = 10000
triggerCommand_Axis10.target = 300
triggerCommand_Axis10.trigger.triggerType = TriggerType.RemainingDistance
triggerCommand_Axis10.trigger.triggerAxis = 10
triggerCommand_Axis10.trigger.triggerValue = 400

# Start the trigger motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(triggerCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach position 100
Wmx3Lib_cm.motion.Wait(10)

# Initialize motion command for Axis 12
posCommand_Axis12 = Motion_PosCommand()

# Set motion parameters for Axis 12
posCommand_Axis12.axis = 12
posCommand_Axis12.profile.type = ProfileType.Trapezoidal
posCommand_Axis12.profile.velocity = 500
posCommand_Axis12.profile.acc = 5000
posCommand_Axis12.profile.dec = 5000
posCommand_Axis12.target = -50

# Start the motion for Axis 12
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis12)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to complete its motion
Wmx3Lib_cm.motion.Wait(12)
