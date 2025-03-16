
# Axes = [7]
# Inputs = []
# Outputs = []

# Create a command value for Axis 7
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000     # Example acceleration
posCommand.profile.dec = 10000     # Example deceleration

# Define target positions
target_positions = [50, -50, 100, -100]

# Execute motion for each target position
for target in target_positions:
    posCommand.target = target
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        continue

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(7)
