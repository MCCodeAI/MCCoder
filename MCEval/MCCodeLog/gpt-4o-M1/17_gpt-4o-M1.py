
# Axes = [5, 7]
# IOInputs = []
# IOOutputs = []

# Initialize the motion command for relative path interpolation
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 5)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Execute the path interpolation
for j in range(5):
    lin.SetTarget(0, 10 * j)  # Set target for Axis 7
    lin.SetTarget(1, -10 * j)  # Set target for Axis 5

    # Start the relative position linear interpolation motion command
    ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
    if ret != 0:
        print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete for each segment
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 7)
    axisSel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
