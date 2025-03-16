
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

# Create a command value for a relative linear interpolation motion.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 6)

# Configure the Advanced S profile parameters.
lin.profile.type = ProfileType.AdvancedS
lin.profile.velocity = 1000
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAccRatio = 0.8
lin.profile.jerkDecRatio = 0.8

# Set the relative target distances for each axis.
lin.SetTarget(0, 200)
lin.SetTarget(1, 20)

# Start the relative linear interpolation motion.
ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axes 5 and 6 to stop moving before proceeding further.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
