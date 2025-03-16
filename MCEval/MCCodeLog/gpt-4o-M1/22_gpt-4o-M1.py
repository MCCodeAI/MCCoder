
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# Define the motion command for absolute linear interpolation
lin = Motion_LinearIntplCommand()

# Set the axes involved in the motion
lin.axisCount = 2
lin.SetAxis(0, 2)  # Axis 2
lin.SetAxis(1, 4)  # Axis 4

# Configure the motion profile
lin.profile.type = ProfileType.JerkLimited
lin.profile.velocity = 800
lin.profile.acc = 8000
lin.profile.jerkAcc = 20000

# Set the target positions for the axes
lin.SetTarget(0, -100)  # Target position for Axis 2
lin.SetTarget(1, -50)   # Target position for Axis 4

# Start the linear interpolation motion
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 2 and Axis 4 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
