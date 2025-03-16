
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to -55 with S-curve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 5
posCommand.target = -55
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(5)

# Set variables
a = 6
b = a + 1
c = a * 10
d = c - b

# Absolute linear interpolation for Axes 5 and 2
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 5)
lin.SetAxis(1, 2)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, a)
lin.SetTarget(1, c)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Sleep for 1.1 seconds
sleep(1.1)

# Counterclockwise circular interpolation
circularCommand = Motion_CenterAndLengthCircularIntplCommand()
circularCommand.SetAxis(0, 5)
circularCommand.SetAxis(1, 2)
circularCommand.SetCenterPos(0, 50)
circularCommand.SetCenterPos(1, 50)
circularCommand.clockwise = 0
circularCommand.arcLengthDegree = d
circularCommand.profile.type = ProfileType.Trapezoidal
circularCommand.profile.velocity = c
circularCommand.profile.acc = 10000
circularCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
