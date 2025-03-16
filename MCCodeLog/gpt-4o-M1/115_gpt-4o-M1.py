
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Step 1: Move Axis 5 to position -55 at a speed of 1000 using an s-curve profile.
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

# Step 2: Set variables a, b, c, and d.
a = 6
b = a + 1
c = a * 10
d = c - b

# Step 3: Start an absolute linear interpolation for Axes 5 and 2 to position (a, c) with a velocity of 1000.
linIntplCommand = Motion_LinearIntplCommand()
linIntplCommand.axisCount = 2
linIntplCommand.SetAxis(0, 5)
linIntplCommand.SetAxis(1, 2)

linIntplCommand.profile.type = ProfileType.Trapezoidal
linIntplCommand.profile.velocity = 1000
linIntplCommand.profile.acc = 10000
linIntplCommand.profile.dec = 10000

linIntplCommand.SetTarget(0, a)
linIntplCommand.SetTarget(1, c)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(linIntplCommand)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait_AxisSel(AxisSelection([5, 2]))

# Step 4: Start a counterclockwise circular interpolation motion command for Axis 5 and 2.
import time
time.sleep(1.1)

circIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circIntplCommand.SetAxis(0, 5)
circIntplCommand.SetAxis(1, 2)
circIntplCommand.SetCenterPos(0, 50)
circIntplCommand.SetCenterPos(1, 50)
circIntplCommand.clockwise = 0  # 0 for counterclockwise
circIntplCommand.arcLength = d
circIntplCommand.profile.type = ProfileType.Trapezoidal
circIntplCommand.profile.velocity = c
circIntplCommand.profile.acc = 10000
circIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait_AxisSel(AxisSelection([5, 2]))
