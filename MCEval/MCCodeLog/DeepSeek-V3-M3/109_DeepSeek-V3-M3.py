
# Axes = [2, 9]
# IOInputs = []
# IOOutputs = []

# Start an absolute linear interpolation for Axes 9 and 2 to position (100, 200) with a velocity of 1000
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 9)
lin.SetAxis(1, 2)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)  # Set target of Axis 9 to be 100
lin.SetTarget(1, 200)  # Set target of Axis 2 to be 200

# Start an absolute position linear interpolation motion command.
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 9 and Axis 2 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 9)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
