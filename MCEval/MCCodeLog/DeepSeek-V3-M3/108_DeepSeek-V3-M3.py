
# Axes = [7, 9]
# IOInputs = []
# IOOutputs = [0.7]

# Move Axis 7 to position 220 with a speed of 1500
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 220
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 7 stops moving
Wmx3Lib_cm.motion.Wait(7)

# Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

sleep(0.2)

ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Start an absolute linear interpolation for Axes 7 and 9 to position (200, 50) with a velocity of 1200
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1200
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 200)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axes 7 and 9 stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a relative linear interpolation for Axes 7 and 9 to position (-100, 50)
lin.SetTarget(0, -100)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axes 7 and 9 stop moving
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start a counterclockwise circular interpolation motion command for Axis 7 and 9, with a center position of (50, 50), an arc length of 270, and a velocity of 1000
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand.SetAxis(0, 7)
circularIntplCommand.SetAxis(1, 9)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 50)
circularIntplCommand.clockwise = 0  # Counterclockwise
circularIntplCommand.arcLengthDegree = 270
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1000
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axes 7 and 9 stop moving
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
