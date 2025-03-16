
# Axes = [1]
# Inputs = []
# Outputs = []

# Define a function to move the axis to a specified position using the TimeAccSCurve profile
def move_axis_to_position(axis, positions, velocity, acc_time_ms, dec_time_ms, start_velocity, end_velocity):
    for position in positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.TimeAccSCurve
        posCommand.axis = axis
        posCommand.target = position
        posCommand.profile.velocity = velocity
        posCommand.profile.accTimeMilliseconds = acc_time_ms
        posCommand.profile.decTimeMilliseconds = dec_time_ms
        posCommand.profile.startingVelocity = start_velocity
        posCommand.profile.endVelocity = end_velocity

        # Execute command to move from current position to specified absolute position.
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis moves to the target position and stops.
        Wmx3Lib_cm.motion.Wait(axis)

# Define the parameters for the motion
axis_number = 1
positions = [10, -10, 10, -10, 10, -10, 10, -10, 0]
velocity = 1000
acc_time_ms = 50
dec_time_ms = 50
start_velocity = 0
end_velocity = 0

# Call the function to move the axis
move_axis_to_position(axis_number, positions, velocity, acc_time_ms, dec_time_ms, start_velocity, end_velocity)
