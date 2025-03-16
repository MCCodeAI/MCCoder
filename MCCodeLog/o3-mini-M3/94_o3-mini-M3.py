
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# In this example we use the hypothetical API functions from Wmx3Lib_cm.config and Wmx3Lib_cm.motion.
# The code sets the soft limit positive and negative positions for Axis 2 to 133 and -133,
# then reads back the settings. If they match the expected values, it moves Axis 2 to position 132;
# otherwise, it moves Axis 2 to position -132.
#
# Note: Each motion command waits until the axis stops moving (using Wait after each move).

import time

def set_soft_limits(axis, pos_val, neg_val):
    # Obtain the current limit parameters for the axis.
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    if ret != 0:
        print("Error reading limit parameters for Axis", axis)
        return False

    # Set the soft limit positions.
    limitParam.softLimitPositivePos = pos_val
    limitParam.softLimitNegativePos = neg_val

    # Write back the updated limit parameters.
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if ret != 0:
        print("Error setting soft limit parameters for Axis", axis, "Error:", Wmx3Lib_cm.ErrorToString(ret))
        return False

    return True

def check_soft_limits(axis, pos_val, neg_val):
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    if ret != 0:
        print("Error reading limit parameters for Axis", axis)
        return False

    # Check if both soft limit positive and negative positions are equal to the desired values.
    return (limitParam.softLimitPositivePos == pos_val) and (limitParam.softLimitNegativePos == neg_val)

def move_axis_to(axis, target, velocity):
    # Create a motion command structure for an absolute move.
    posCommand = Motion_PosCommand()
    posCommand.axis = axis
    posCommand.target = target
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = 10000  # chosen acceleration value
    posCommand.profile.dec = 10000  # chosen deceleration value

    # Start the position command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("Error moving Axis", axis, "to position", target, "Error:", Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait until the axis stops moving.
    Wmx3Lib_cm.motion.Wait(axis)
    return True


#==== Main Execution for Axis 2 ====#
axis = 2

# Set soft limit positive and negative positions to 133 and -133.
if not set_soft_limits(axis, 133, -133):
    print("Failed to set soft limits for Axis", axis)
else:
    # Optionally add a brief pause to allow the parameters to update.
    time.sleep(0.1)

    # Check if the soft limits were successfully set.
    if check_soft_limits(axis, 133, -133):
        # If the soft limits are as expected, move Axis 2 to position 132.
        print("Soft limits verified. Moving Axis", axis, "to position 132.")
        move_axis_to(axis, 132, 1000)
    else:
        # Otherwise, move Axis 2 to position -132.
        print("Soft limits not verified. Moving Axis", axis, "to position -132.")
        move_axis_to(axis, -132, 1000)
