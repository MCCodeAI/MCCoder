
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get the system status (Engine State) for the entire system.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

print('Engine State : ' + str(CmStatus.engineState))

# Prepare a motion command for Axis 1 based on the Engine State.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.profile.velocity = 1000      # Set a default velocity
posCommand.profile.acc = 10000            # Set acceleration
posCommand.profile.dec = 10000            # Set deceleration

# If the engine is in a communicating state, move to 111.1, otherwise, move to 0.1.
if str(CmStatus.engineState).lower() == "communicating":
    posCommand.target = 111.1
    print("Engine is communicating. Moving Axis 1 to 111.1.")
else:
    posCommand.target = 0.1
    print("Engine is not communicating. Moving Axis 1 to 0.1.")

# Start the motion command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 1 to stop moving.
ret = Wmx3Lib_cm.motion.Wait(1)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
