
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Define the axis number
axis = 2

# Set the Soft Limit Positive Position and Soft Limit Negative Position
soft_limit_positive = 133
soft_limit_negative = -133

# Function to set soft limits
def set_soft_limits(axis, positive_limit, negative_limit):
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.softLimitPositivePos = positive_limit
    limitParam.softLimitNegativePos = negative_limit
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if ret != 0:
        print('Set soft limits error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False
    return True

# Function to check if soft limits are set correctly
def check_soft_limits(axis, positive_limit, negative_limit):
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    if ret != 0:
        print('Get soft limits error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False
    return (limitParam.softLimitPositivePos == positive_limit and 
            limitParam.softLimitNegativePos == negative_limit)

# Function to move the axis to a specified position
def move_axis_to_position(axis, position):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = position
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
    return True

# Set the soft limits
if set_soft_limits(axis, soft_limit_positive, soft_limit_negative):
    # Check if the soft limits are set correctly
    if check_soft_limits(axis, soft_limit_positive, soft_limit_negative):
        # Move Axis 2 to 132 if limits are set correctly
        move_axis_to_position(axis, 132)
    else:
        # Move Axis 2 to -132 if limits are not set correctly
        move_axis_to_position(axis, -132)
