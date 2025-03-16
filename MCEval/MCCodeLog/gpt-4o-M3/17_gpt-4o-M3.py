
# Axes = [7, 5]
# Inputs = []
# Outputs = []

# Initialize the motion command for Axes 7 and 5
velocity = 1000

# Loop through the path points
for j in range(5):
    # Calculate the target positions for the current step
    target_x = 10 * j
    target_y = -10 * j

    # Create a linear interpolation command for the current step
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    lin.SetAxis(0, 7)
    lin.SetAxis(1, 5)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = velocity
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    lin.SetTarget(0, target_x)
    lin.SetTarget(1, target_y)

    # Execute the interpolation command
    ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
    if ret != 0:
        print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the axes to stop moving before proceeding to the next step
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 7)
    axisSel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
