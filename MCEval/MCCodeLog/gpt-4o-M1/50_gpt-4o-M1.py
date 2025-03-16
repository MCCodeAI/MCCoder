
# Axes = [0, 3]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
trig = Trigger()
wait = Motion_WaitCondition()

# Set interpolation command parameters
lin.axisCount = 2
lin.SetAxis(0, 0)
lin.SetAxis(1, 3)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1500
lin.profile.acc = 10000
lin.profile.dec = 10000

# Execute linear interpolation to position (80, 0)
lin.SetTarget(0, 80)
lin.SetTarget(1, 0)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set trigger parameters (trigger at 10 remaining distance)
trig.triggerAxis = 0
trig.triggerType = TriggerType.RemainingDistance
trig.triggerValue = 10

# Execute trigger linear interpolation to position (80, 80)
lin.SetTarget(0, 80)
lin.SetTarget(1, 80)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger linear interpolation to position (0, 80)
lin.SetTarget(0, 0)
lin.SetTarget(1, 80)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger linear interpolation to position (0, 0)
lin.SetTarget(0, 0)
lin.SetTarget(1, 0)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
