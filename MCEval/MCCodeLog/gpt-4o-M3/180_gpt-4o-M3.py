
# Axes = [3]
# Inputs = []
# Outputs = []

# Create a position command for Axis 3 using a ConstantDec profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Define the sequence of target positions.
target_positions = [30, 0, 30, 0]

# Move Axis 3 to each target position in sequence.
for target in target_positions:
    posCommand.target = target

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(3)
