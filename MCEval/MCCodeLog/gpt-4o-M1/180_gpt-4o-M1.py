
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to the position 30 and 0 and 30 and 0 at starting Velocity of 100, and end Velocity of 0, using a ConstantDec profile.

# Define a function to move the axis to a specified position using the ConstantDec profile
def move_axis(axis, positions, starting_velocity, end_velocity):
    for position in positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.ConstantDec
        posCommand.axis = axis
        posCommand.target = position
        posCommand.profile.startingVelocity = starting_velocity
        posCommand.profile.endVelocity = end_velocity

        # Execute command to move from current position to specified absolute position.
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis moves to the target position and stops.
        Wmx3Lib_cm.motion.Wait(axis)

# Define the parameters for the motion
axis_number = 3
positions = [30, 0, 30, 0]
starting_velocity = 100
end_velocity = 0

# Execute the motion
move_axis(axis_number, positions, starting_velocity, end_velocity)
