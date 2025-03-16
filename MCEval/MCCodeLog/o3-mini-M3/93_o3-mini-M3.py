
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Define the axis we are working on.
axis = 3

# -------------------------------------------------------------------------
# Step 1: Set the Home Position parameter of Axis 3 to 8.8
# -------------------------------------------------------------------------
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 8.8
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print("Error setting Home Position to 8.8: " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# -------------------------------------------------------------------------
# Step 2: Execute homing for Axis 3
# -------------------------------------------------------------------------
# Note: The 'Home' method does not exist. Use the available 'StartHome' function.
ret = Wmx3Lib_cm.home.StartHome(axis)
if ret != 0:
    print("Error starting homing for Axis 3: " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 3 has completed the homing motion.
Wmx3Lib_cm.motion.Wait(axis)

# -------------------------------------------------------------------------
# Step 3: Change the Home Position parameter for Axis 3 back to 0
# -------------------------------------------------------------------------
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 0
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print("Error resetting Home Position to 0: " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
