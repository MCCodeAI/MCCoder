
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get system status
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if Engine State is Communicating
if CmStatus.engineState == EngineState.Communicating:
    target_pos = 111.1
else:
    target_pos = 0.1

# Create position command
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = target_pos
posCommand.profile.velocity = 1000  # Example velocity value
posCommand.profile.acc = 10000     # Example acceleration value
posCommand.profile.dec = 10000     # Example deceleration value

# Start motion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for motion to complete
Wmx3Lib_cm.motion.Wait(1)
