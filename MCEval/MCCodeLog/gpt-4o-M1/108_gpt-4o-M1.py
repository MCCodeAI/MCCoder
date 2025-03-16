
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
Wmx3Lib_cm.motion.Wait(7)

# Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0
Wmx3Lib_cm.io.SetOutputBit(0, 7, 1)
time.sleep(0.2)
Wmx3Lib_cm.io.SetOutputBit(0, 7, 0)

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
Wmx3Lib_cm.motion.Wait_AxisSel(AxisSelection([7, 9]))

# Start a relative linear interpolation for Axes 7 and 9 to position (-100, 50)
lin.SetTarget(0, -100)
lin.SetTarget(1, 50)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait_AxisSel(AxisSelection([7, 9]))

# Start a counterclockwise circular interpolation motion command for Axis 7 and 9, with a center position of (50, 50), an arc length of 270, and a velocity of 1000
circ = Motion_CircularIntplCommand()
circ.axisCount = 2
circ.SetAxis(0, 7)
circ.SetAxis(1, 9)

circ.SetCenterPos(0, 50)
circ.SetCenterPos(1, 50)
circ.arcLength = 270
circ.profile.type = ProfileType.Trapezoidal
circ.profile.velocity = 1000
circ.profile.acc = 10000
circ.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circ)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait_AxisSel(AxisSelection([7, 9]))
