
# Axes = [5, 6]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 6)

lin.profile.type = ProfileType.SCurve
lin.profile.velocity = 1000
lin.profile.acc = 8000
lin.profile.dec = 8000
lin.profile.jerkAccRatio = 0.8
lin.profile.jerkDecRatio = 0.8

lin.SetTarget(0, 200)  # Relative distance for Axis 5
lin.SetTarget(1, 20)   # Relative distance for Axis 6

# Start a relative position linear interpolation motion command
ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for axes to complete motion
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
