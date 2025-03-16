
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

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

lin.SetMaxVelocity(0, 555)  # Axis 2 max velocity
lin.SetMaxVelocity(1, 666)  # Axis 5 max velocity

lin.SetMaxAcc(0, 8888)  # Axis 2 max acceleration
lin.SetMaxAcc(1, 9999)  # Axis 5 max acceleration
lin.SetMaxDec(0, 8888)  # Axis 2 max deceleration
lin.SetMaxDec(1, 9999)  # Axis 5 max deceleration

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
