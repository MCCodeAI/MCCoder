
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

import time

# 1. Move Axis 5 to the position -55 at a speed of 1000 using an S-curve profile.
posCommand = Motion_PosCommand()
posCommand.axis = 5
posCommand.target = -55
# Using the TimeAccSCurve type as an example S-curve profile.
posCommand.profile.type = ProfileType.TimeAccSCurve
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code (Axis 5) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
# Wait until Axis 5 stops moving.
Wmx3Lib_cm.motion.Wait(5)

# 2. Set the variables: a = 6, b = a + 1, c = a * 10, d = c - b.
a = 6
b = a + 1
c = a * 10
d = c - b

# 3. Start an absolute linear interpolation for Axes 5 and 2 
#    to position (a, c) with a velocity of 1000.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
# Assign axes in sorted order: the first index corresponds to Axis 2, the second to Axis 5.
lin.SetAxis(0, 2)
lin.SetAxis(1, 5)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, a)  # Axis 2 moves to position a (6)
lin.SetTarget(1, c)  # Axis 5 moves to position c (60)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# 4. Sleep for 1.1 seconds, then start a counterclockwise circular interpolation for Axes 5 and 2,
#    with a center position of (50, 50), an arc length of d, and a velocity of c.
time.sleep(1.1)

circularCommand = Motion_CenterAndLengthCircularIntplCommand()
circularCommand.axisCount = 2
# Assign axes in sorted order: first Axis 2, then Axis 5.
circularCommand.SetAxis(0, 2)
circularCommand.SetAxis(1, 5)
circularCommand.SetCenterPos(0, 50)
circularCommand.SetCenterPos(1, 50)
circularCommand.arcLengthDegree = d
# For counterclockwise motion, set clockwise flag to 0.
circularCommand.clockwise = 0
circularCommand.profile.type = ProfileType.Trapezoidal
circularCommand.profile.velocity = c
circularCommand.profile.acc = 10000
circularCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
