
# Axes = [6]
# Inputs = []
# Outputs = []

# Define a function to move Axis 6 to a specified position with blocking wait
def move_axis_6_to_position(target_position):
    pos_command = Motion_PosCommand()
    pos_command.axis = 6
    pos_command.target = target_position
    pos_command.profile.type = ProfileType.Trapezoidal
    pos_command.profile.velocity = 1000
    pos_command.profile.acc = 10000
    pos_command.profile.dec = 10000

    # Start the motion command
    ret = Wmx3Lib_cm.motion.StartPos(pos_command)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the axis to reach the target position and stop
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Move Axis 6 to the specified positions with blocking waits
move_axis_6_to_position(50)
move_axis_6_to_position(-50)
move_axis_6_to_position(100)
move_axis_6_to_position(-100)
