
# Axes = [6, 8]
# IOInputs = []
# IOOutputs = []

# Create a linear interpolation motion command
lin = Motion_LinearIntplCommand()
lin.axisCount = 2

# Map the interpolation targets to the correct axes:
# The first axis in the command corresponds to Axis 6, and the second to Axis 8.
lin.SetAxis(0, 6)
lin.SetAxis(1, 8)

# Configure the motion profile with a trapezoidal profile and the specified velocity.
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1100
# Set default acceleration and deceleration values (adjust as required).
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the target positions: Axis 6 to 200 and Axis 8 to 50.
lin.SetTarget(0, 200)
lin.SetTarget(1, 50)

# Start the absolute linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes (6 and 8) to complete the motion before proceeding.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
