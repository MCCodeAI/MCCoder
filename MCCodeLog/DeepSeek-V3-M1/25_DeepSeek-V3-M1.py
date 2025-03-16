
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

# Create a command value of relative distance
lin = Motion_LinearIntplCommand()
lin.axisCount = 2 
lin.SetAxis(0, 5)
lin.SetAxis(1, 6)

# Set the profile type to Advanced S profile
lin.profile.type = ProfileType.AdvancedS
lin.profile.velocity = 1000
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAccRatio = 0.8
lin.profile.jerkDecRatio = 0.8

# Set the relative distance targets
lin.SetTarget(0, 200)  # Set target of Axis 5 to be 200
lin.SetTarget(1, 20)   # Set target of Axis 6 to be 20

# Start a relative position linear interpolation motion command.
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
