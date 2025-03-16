
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Set Soft Limit Positive Position and Soft Limit Negative Position parameters for Axis 2
axis = 2

# Read current limit parameters
limitParam = Config_LimitParam()
ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
if ret != 0:
    print('GetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set Soft Limit Positive Position to 133
limitParam.softLimitPositivePos = 133
# Set Soft Limit Negative Position to -133
limitParam.softLimitNegativePos = -133

# Set updated limit parameters
ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
if ret != 0:
    print('SetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Verify the Soft Limit positions
ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
if ret != 0:
    print('GetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if Soft Limit positions are set correctly
soft_limit_positive = limitParam.softLimitPositivePos
soft_limit_negative = limitParam.softLimitNegativePos

if soft_limit_positive == 133 and soft_limit_negative == -133:
    print("Soft Limit positions are correctly set. Moving to 132...")
    target_position = 132
else:
    print("Soft Limit positions are incorrect. Moving to -132...")
    target_position = -132

# Create position command
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = target_position
posCommand.profile.velocity = 1000  # Example velocity value
posCommand.profile.acc = 10000     # Example acceleration value
posCommand.profile.dec = 10000     # Example deceleration value

# Start motion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for motion to complete
Wmx3Lib_cm.motion.Wait(axis)
