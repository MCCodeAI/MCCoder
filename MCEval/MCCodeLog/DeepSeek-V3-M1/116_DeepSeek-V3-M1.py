
# Axes = [6, 7, 8]
# IOInputs = []
# IOOutputs = [6.7]

# Move Axis 6 to 20 with a velocity of 900 using a trapezoid profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 stops moving
Wmx3Lib_cm.motion.Wait(6)

# Set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0
Wmx3Lib_io.SetOutputBit(6, 7, 1)
sleep(0.1)
Wmx3Lib_io.SetOutputBit(6, 7, 0)

# Move Axis 7 to 30
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 30
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 7 stops moving
Wmx3Lib_cm.motion.Wait(7)

# Linearly interpolate Axis 7 and 8 to (40, 50)
linIntplCommand = Motion_LinIntplCommand()
linIntplCommand.SetAxis(0, 7)
linIntplCommand.SetAxis(1, 8)
linIntplCommand.SetTargetPos(0, 40)
linIntplCommand.SetTargetPos(1, 50)
linIntplCommand.profile.type = ProfileType.Trapezoidal
linIntplCommand.profile.velocity = 1000
linIntplCommand.profile.acc = 10000
linIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartLinIntplPos(linIntplCommand)
if ret != 0:
    print('StartLinIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 7 and 8 stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a clockwise circular interpolation motion command for Axis 6 and 7, with a center position of (50, 50), an arc length of 360
circIntplCommand = Motion_CircIntplCommand()
circIntplCommand.SetAxis(0, 6)
circIntplCommand.SetAxis(1, 7)
circIntplCommand.SetCenterPos(0, 50)
circIntplCommand.SetCenterPos(1, 50)
circIntplCommand.clockwise = 1
circIntplCommand.arcLengthDegree = 360
circIntplCommand.profile.type = ProfileType.Trapezoidal
circIntplCommand.profile.velocity = 1000
circIntplCommand.profile.acc = 10000
circIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircIntplPos(circIntplCommand)
if ret != 0:
    print('StartCircIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 and 7 stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Establish synchronous control between master axis 6 and slave axis 7, then move Axis 6 to position 60
syncCommand = Motion_SyncCommand()
syncCommand.masterAxis = 6
syncCommand.slaveAxis = 7
syncCommand.ratio = 1.0
syncCommand.profile.type = ProfileType.Trapezoidal
syncCommand.profile.velocity = 1000
syncCommand.profile.acc = 10000
syncCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartSync(syncCommand)
if ret != 0:
    print('StartSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 stops moving
Wmx3Lib_cm.motion.Wait(6)

# Stop synchronous control
ret = Wmx3Lib_cm.motion.StopSync(syncCommand)
if ret != 0:
    print('StopSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
