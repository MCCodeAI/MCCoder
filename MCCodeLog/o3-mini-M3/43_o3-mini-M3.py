
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
trig = Trigger()

# Set up the motion command for Axis 3 and Axis 6
lin.axisCount = 2
lin.SetAxis(0, 3)
lin.SetAxis(1, 6)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000

# First interpolation: move to (200, 100)
lin.SetTarget(0, 200)
lin.SetTarget(1, 100)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 and Axis 6 to stop moving before proceeding
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Prepare the triggered motion command: when completed distance of Axis 3 reaches 100,
# trigger a new interpolation to (-50, -100)
lin.SetTarget(0, -50)
lin.SetTarget(1, -100)

trig.triggerAxis = 0  # Corresponds to Axis 3 (first axis in the command)
trig.triggerType = TriggerType.CompletedDistance
trig.triggerValue = 100

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the triggered motion is complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
