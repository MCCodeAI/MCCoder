
# Axes = [4, 5, 8]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()
trig = Trigger()

# Execute normal motion command
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

# Wait until the axes start moving
while True:
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (CmStatus.GetAxesStatus(4).motionState == MotionState.Running) and (CmStatus.GetAxesStatus(5).motionState == MotionState.Running):
        break
    sleep(0.1)

# Set up trigger for Axis 8
lin8 = Motion_LinearIntplCommand()
lin8.axisCount = 1
lin8.SetAxis(0, 8)
lin8.profile.type = ProfileType.Trapezoidal
lin8.profile.velocity = 1000
lin8.profile.acc = 10000
lin8.profile.dec = 10000
lin8.SetTarget(0, 200)

trig.triggerAxis = 4
trig.triggerType = TriggerType.DistanceToTarget
trig.triggerValue = 20

ret = Wmx3Lib_cm.motion.StartLinearIntplPos_Trigger(lin8, trig)
if ret != 0:
    print('StartLinearIntplPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for all motions to complete
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
axisSel.SetAxis(2, 8)

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
