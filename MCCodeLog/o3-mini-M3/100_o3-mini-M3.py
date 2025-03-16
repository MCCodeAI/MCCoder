
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Define the axis to work with.
axis = 10

# -------------------------------
# Step 1: Set Axis Polarity parameter of Axis 10 to -1.
# -------------------------------
# Read the current axis parameters.
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print("Error reading AxisParam: " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set the Axis Polarity to -1.
axisParam.SetAxisPolarity(axis, -1)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print("Error setting Axis Polarity: " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# -------------------------------
# Step 2: Verify the Axis Polarity parameter.
# -------------------------------
# Read back the axis parameters to verify.
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print("Error reading AxisParam for verification: " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Assuming a GetAxisPolarity method exists to obtain the current polarity value.
currentPolarity = axisParam.GetAxisPolarity(axis)
# Check if the polarity is set correctly.
if currentPolarity == -1:
    targetPosition = 100
    print("Axis Polarity verified as -1. Moving Axis", axis, "to position", targetPosition)
else:
    targetPosition = -10
    print("Axis Polarity not verified. Moving Axis", axis, "to position", targetPosition)

# -------------------------------
# Step 3: Move Axis 10 based on the verification result.
# -------------------------------
# Create a position command.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = targetPosition
# Here we use reasonable values for velocity, acceleration, and deceleration.
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error moving Axis", axis, ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 10 reaches the target position and stops.
Wmx3Lib_cm.motion.Wait(0)
