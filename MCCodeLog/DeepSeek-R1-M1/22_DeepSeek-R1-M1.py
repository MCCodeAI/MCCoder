
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()

lin.axisCount = 2
lin.SetAxis(0, 2)
lin.SetAxis(1, 4)

lin.profile.type = ProfileType.JerkLimited
lin.profile.velocity = 800
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAcc = 20000

lin.SetTarget(0, -100)
lin.SetTarget(1, -50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
