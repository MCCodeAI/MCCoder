
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Create a command value for relative linear interpolation motion
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 4)
lin.SetAxis(1, 6)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 900
lin.profile.acc = 10000
lin.profile.dec = 10000

# Start relative linear interpolation motion with distance (100, -100)
lin.SetTarget(0, 100)
lin.SetTarget(1, -100)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start relative linear interpolation motion with distance (-100, 0)
lin.SetTarget(0, -100)
lin.SetTarget(1, 0)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4 and Axis 6 become idle.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start relative linear interpolation motion with distance (0, 100)
lin.SetTarget(0, 0)
lin.SetTarget(1, 100)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4 and Axis 6 become idle.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
