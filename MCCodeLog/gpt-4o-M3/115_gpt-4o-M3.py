
# Axes = [2, 5]
# IOInputs = []
# IOOutputs = []

# Part 1: Move Axis 5 to the position -55 at a speed of 1000 using an S-curve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve  # Assuming SCurve exists as a profile type
posCommand.axis = 5
posCommand.target = -55
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Include acceleration
posCommand.profile.dec = 10000  # Include deceleration
posCommand.profile.jerk = 5000  # Include jerk if the profile requires it
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(5)

# Part 2: Set variables a, b, c, and d
a = 6
b = a + 1
c = a * 10
d = c - b

# Part 3: Absolute Linear Interpolation for Axes 5 and 2 to position (a, c) with a velocity of 1000
linIntplCmd = Motion_LinearIntplCommand()
linIntplCmd.axisCount = 2
linIntplCmd.SetAxis(0, 5)
linIntplCmd.SetAxis(1, 2)
linIntplCmd.profile.type = ProfileType.Trapezoidal
linIntplCmd.profile.velocity = 1000
linIntplCmd.profile.acc = 10000
linIntplCmd.profile.dec = 10000
linIntplCmd.SetTarget(0, a)  # Position for Axis 5
linIntplCmd.SetTarget(1, c)  # Position for Axis 2
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(linIntplCmd)
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

# Part 4: Counterclockwise Circular Interpolation for Axis 5 and 2
circularIntplCmd = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCmd.SetAxis(0, 5)
circularIntplCmd.SetAxis(1, 2)
circularIntplCmd.SetCenterPos(0, 50)
circularIntplCmd.SetCenterPos(1, 50)
circularIntplCmd.clockwise = 0  # Counterclockwise
circularIntplCmd.arcLengthDegree = d
circularIntplCmd.profile.type = ProfileType.Trapezoidal
circularIntplCmd.profile.velocity = c
circularIntplCmd.profile.acc = 10000
circularIntplCmd.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCmd)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
