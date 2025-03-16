
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Read the current system status from the engine
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check the Engine State
engine_state = CmStatus.engineState
print('Engine State : ' + str(engine_state))

# Define target positions based on Engine State
if engine_state == EngineState.Communicating:
    target_position = 111.1
else:
    target_position = 0.1

# Create a command value for Axis 1
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = target_position
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 1 to the target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 moves to the target position and stops
Wmx3Lib_cm.motion.Wait(1)
