
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
trig = Trigger()

# Execute normal motion command
lin.axisCount = 2
lin.SetAxis(0, 3)
lin.SetAxis(1, 6)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 200)
lin.SetTarget(1, 100)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 3 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion command
lin.SetTarget(0, -50)
lin.SetTarget(1, -100)

trig.triggerAxis = 3
trig.triggerType = TriggerType.CompletedDistance
trig.triggerValue = 100

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 3 and Axis 6 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
