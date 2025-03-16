
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Create a linear interpolation motion command for Axis 2 and Axis 5.
lin = Motion_LinearIntplCommand()

# There are two axes involved.
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 5)

# Set the motion profile parameters:
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# Set the target positions for Axis 2 and Axis 5
lin.SetTarget(0, 111)
lin.SetTarget(1, 222)

# Set the maximum velocity limits for each axis.
lin.SetMaxVelocity(0, 555)  # For Axis 2
lin.SetMaxVelocity(1, 666)  # For Axis 5

# Set the maximum acceleration and deceleration limits for each axis.
lin.SetMaxAcc(0, 8888)      # For Axis 2
lin.SetMaxDec(0, 8888)      # For Axis 2

lin.SetMaxAcc(1, 9999)      # For Axis 5
lin.SetMaxDec(1, 9999)      # For Axis 5

# Start the linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete for both Axis 2 and Axis 5.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
