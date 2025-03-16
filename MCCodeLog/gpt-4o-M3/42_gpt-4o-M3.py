
# Axes = [2, 5]
# Inputs = []
# Outputs = []

lin = Motion_LinearIntplCommand()

# Execute absolute position linear interpolation motion command
lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 5)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 111)
lin.SetTarget(1, 222)

lin.SetMaxVelocity(0, 555)
lin.SetMaxVelocity(1, 666)

lin.SetMaxAcc(0, 8888)
lin.SetMaxAcc(1, 9999)

lin.SetMaxDec(0, 8888)
lin.SetMaxDec(1, 9999)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 2 and Axis 5 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
