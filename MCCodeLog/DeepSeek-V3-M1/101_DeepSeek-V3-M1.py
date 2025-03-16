
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Read the current system status from the engine
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check the Engine State
engine_state = CmStatus.engineState
print('Engine State : ' + str(engine_state))

# Define target positions based on Engine State
if engine_state == 'Communicating':
    target_position = 111.1
else:
    target_position = 0.1

# Move Axis 1 to the target position
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = target_position
posCommand.profile.velocity = 1000  # Set a default velocity
posCommand.profile.acc = 10000     # Set a default acceleration
posCommand.profile.dec = 10000     # Set a default deceleration

# Execute the command to move Axis 1
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 1 to stop moving
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

print('Axis 1 has moved to the target position: ' + str(target_position))
