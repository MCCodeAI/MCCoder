
# Axes = [3, 4]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 3)
lin.SetAxis(1, 4)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 900
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, -100)
lin.SetTarget(1, 100)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
