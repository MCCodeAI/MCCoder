
# Axes = [4, 5, 8]
# Inputs = []
# Outputs = []

lin = Motion_LinearIntplCommand()
trig = Trigger()

# Execute normal motion command for Axis 4 and Axis 5
lin.axisCount = 2
lin.SetAxis(0, 4)
lin.SetAxis(1, 5)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 100)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4 and Axis 5 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up trigger for Axis 8
lin.SetTarget(0, 200)  # Target for Axis 8

trig.triggerAxis = 8
trig.triggerType = TriggerType.DistanceToTarget
trig.triggerValue = 20

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 8 becomes idle.
axisSel = AxisSelection()
axisSel.axisCount = 1
axisSel.SetAxis(0, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
