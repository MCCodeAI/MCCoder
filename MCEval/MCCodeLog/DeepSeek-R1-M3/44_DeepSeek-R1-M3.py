
# Axes = [4, 5, 8]
# IOInputs = []
# IOOutputs = []

lin = Motion_LinearIntplCommand()

# Execute linear interpolation for Axis 4 and 5
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

sleep(0.001)

# Monitor remaining distance of Axis 4 (CORRECTED SECTION)
while True:
    ret, axis_status = Wmx3Lib_cm.axisControl.GetAxisStatus(4)  # Changed from motion to axisControl
    if ret != 0:
        print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    if axis_status.DistanceToGo <= 20:
        break
    sleep(0.1)

# Trigger Axis 8 motion
posCommand = Motion_PosCommand()
posCommand.axis = 8
posCommand.target = 200
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for all axes to complete
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
axisSel.SetAxis(2, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
