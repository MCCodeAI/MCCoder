
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Example for Axis 10

axis = 10

# ----------------------------------------------------------------------
# Step 1: Set the Axis Polarity parameter of Axis 10 to -1.

# Read the current axis parameters.
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set the Axis Polarity to -1.
axisParam.SetAxisPolarity(axis, -1)

# Write the updated axis parameters.
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set AxisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# ----------------------------------------------------------------------
# Step 2: Check if the Axis Polarity is set correctly

# Read back the axis parameters.
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print('GetAxisParam (after setting) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Assume there is a function or method to retrieve the polarity.
currentPolarity = axisParam.GetAxisPolarity(axis)

# ----------------------------------------------------------------------
# Step 3: Move Axis 10 based on the polarity check.
# If polarity is set to -1 as desired, move Axis 10 to position 100;
# otherwise, move Axis 10 to position -10.

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis

if currentPolarity == -1:
    posCommand.target = 100
else:
    posCommand.target = -10

# Set some standard motion profile parameters.
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis finishes moving.
Wmx3Lib_cm.motion.Wait(0)
