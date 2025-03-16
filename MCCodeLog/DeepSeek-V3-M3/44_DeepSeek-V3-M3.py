
# Axes = [4, 5, 8]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
trigPos = Motion_TriggerPosCommand()

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

# Trigger Axis 8 to move to 200 when the DistanceToTarget is 20
trigPos.axis = 8
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = 200

trigPos.trigger.triggerAxis = 4
trigPos.trigger.triggerType = TriggerType.DistanceToTarget
trigPos.trigger.triggerValue = 20

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4, Axis 5, and Axis 8 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
axisSel.SetAxis(2, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
