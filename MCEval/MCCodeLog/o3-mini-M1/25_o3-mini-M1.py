
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

# This script starts a relative linear interpolation motion for Axes 5 and 6.
# The motion is defined with a relative distance of (200, 20), a velocity of 1000,
# and uses an Advanced S profile with acceleration and deceleration set to 8000,
# along with jerkAccRatio and jerkDecRatio set to 0.8.

lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 6)

# Configure the advanced S motion profile.
lin.profile.type = ProfileType.AdvancedS  # Use Advanced S profile
lin.profile.velocity = 1000
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAccRatio = 0.8
lin.profile.jerkDecRatio = 0.8

# Set the relative target distances for each axis.
lin.SetTarget(0, 200)  # Relative distance for Axis 5
lin.SetTarget(1, 20)   # Relative distance for Axis 6

# Start the relative linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for Axes 5 and 6 to stop moving after the command completes.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
