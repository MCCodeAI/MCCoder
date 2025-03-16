
# Axes = [1]
# Inputs = []
# Outputs = []

# Function to get the status of Axis 1
def get_axis_status(axis):
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return None
    return CmStatus.GetAxesStatus(axis)

# Function to move an axis to a specified position
def move_axis_to_position(axis, target_position, velocity=1000, acc=10000, dec=10000):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = target_position
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = acc
    posCommand.profile.dec = dec

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(axis)
    return True

# Get the status of Axis 1
axis_status = get_axis_status(1)
if axis_status is None:
    print("Failed to get axis status.")
else:
    # Move Axis 1 to position 101
    if move_axis_to_position(1, 101):
        # Get the status of position command and actual position
        pos_cmd = axis_status.posCmd
        actual_pos = axis_status.actualPos

        # Check if position command and actual position are the same
        if pos_cmd == actual_pos:
            # Move Axis 1 to 201
            move_axis_to_position(1, 201)
        else:
            # Move Axis 1 to -201
            move_axis_to_position(1, -201)
