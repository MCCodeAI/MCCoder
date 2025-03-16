
# Axes = [6, 7, 8]
# IOInputs = []
# IOOutputs = [6.7]

# Move Axis 6 to 20 with a velocity of 900 using a trapezoid profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0
Wmx3Lib_cm.io.SetOutput(6, 7, 1)
sleep(0.1)
Wmx3Lib_cm.io.SetOutput(6, 7, 0)

# Move Axis 7 to 30
posCommand.axis = 7
posCommand.target = 30
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)

# Linearly interpolate Axis 7 and 8 to (40, 50)
linearCommand = Motion_LinearIntplCommand()
linearCommand.SetAxis(0, 7)
linearCommand.SetAxis(1, 8)
linearCommand.SetTargetPos(0, 40)
linearCommand.SetTargetPos(1, 50)
linearCommand.profile.type = ProfileType.Trapezoidal
linearCommand.profile.velocity = 900
linearCommand.profile.acc = 1000
linearCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(linearCommand)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 7 and 8 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion command for Axis 6 and 7, with a center position of (50, 50), an arc length of 360
circularCommand = Motion_CircularIntplCommand()
circularCommand.SetAxis(0, 6)
circularCommand.SetAxis(1, 7)
circularCommand.SetCenterPos(0, 50)
circularCommand.SetCenterPos(1, 50)
circularCommand.arcLengthDegree = 360
circularCommand.clockwise = 1
circularCommand.profile.type = ProfileType.Trapezoidal
circularCommand.profile.velocity = 900
circularCommand.profile.acc = 1000
circularCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circularCommand)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 6 and 7 become idle.
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Establish synchronous control between master axis 6 and slave axis 7, then move Axis 6 to position 60
syncControl = AdvSync_SyncControl()
syncControl.masterAxis = 6
syncControl.slaveAxis = 7
syncControl.type = AdvSync_SyncType.Synchronous

ret = Wmx3Lib_adv.advSync.StartSyncControl(syncControl)
if ret != 0:
    print('StartSyncControl error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

posCommand.axis = 6
posCommand.target = 60
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
