
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

# Create a Motion_LinearIntplCommand instance for absolute linear interpolation
lin = Motion_LinearIntplCommand()

# Set the number of axes and assign the physical axis numbers (axes 1 and 2)
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 2)

# Configure the motion profile for the linear interpolation
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the target positions for each axis: Axis 1 to 100, and Axis 2 to 150
lin.SetTarget(0, 100)
lin.SetTarget(1, 150)

# Start the absolute linear interpolation motion
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait for axes 1 and 2 to stop moving after the motion is complete
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
