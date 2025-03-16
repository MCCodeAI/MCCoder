
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to the position -55 at a speed of 1000, using an scurve profile
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
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(5)

# Set the variable a=6, b=a+1, c=a*10, d=c-b
a = 6
b = a + 1
c = a * 10
d = c - b

# Start an absolute linear interpolation for Axes 5 and 2 to position (a, c) with a velocity of 1000
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
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 5 and Axis 2 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Sleep for 1.1 seconds
sleep(1.1)

# Start a counterclockwise circular interpolation motion command for Axis 5 and 2, with a center position of (50, 50), an arc length of d, and a velocity of c
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand.SetAxis(0, 5)
circularIntplCommand.SetAxis(1, 2)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 50)
circularIntplCommand.clockwise = 0  # Counterclockwise
circularIntplCommand.arcLengthDegree = d
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = c
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 5 and Axis 2 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 5)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
