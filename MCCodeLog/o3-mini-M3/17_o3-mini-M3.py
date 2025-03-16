
# Axes = [5, 7]
# IOInputs = []
# IOOutputs = []

# This script starts a relative path interpolation motion command for Axes 7 and 5
# with a velocity of 1000. It adds a linear interpolation segment to (10*j, -10*j)
# while j < 5 and waits for each motion to complete (axes stop moving) before 
# issuing the next interpolation command.

# Create a relative linear interpolation command object.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
# Set axes in ascending order: Axis 5 and Axis 7
lin.SetAxis(0, 5)
lin.SetAxis(1, 7)

# Configure the motion profile parameters.
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

j = 0
while j < 5:
    # Calculate relative target positions based on the current value of j.
    dx = 10 * j
    dy = -10 * j

    lin.SetTarget(0, dx)  # Relative move for Axis 5
    lin.SetTarget(1, dy)  # Relative move for Axis 7

    # Start the relative interpolation motion command.
    ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
    if ret != 0:
        print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait for the motion on both axes to complete before proceeding.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 5)
    axisSel.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    j += 1
