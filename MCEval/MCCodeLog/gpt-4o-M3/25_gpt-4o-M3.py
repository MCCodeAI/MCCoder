
# Axes = [5, 6]
# Inputs = []
# Outputs = []

# Create a command value for relative linear interpolation motion
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 6)

# Set the motion profile to Advanced S
lin.profile.type = ProfileType.AdvancedS
lin.profile.velocity = 1000
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAccRatio = 0.8
lin.profile.jerkDecRatio = 0.8

# Set the relative target distances for each axis
lin.SetTarget(0, 200)  # Set target distance for Axis 5
lin.SetTarget(1, 20)   # Set target distance for Axis 6

# Start the relative linear interpolation motion command
ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 5 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
