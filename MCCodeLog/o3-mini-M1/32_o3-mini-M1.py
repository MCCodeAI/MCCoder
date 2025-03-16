
# Axes = [2, 3]
# IOInputs = []
# IOOutputs = []

# First Motion: Counterclockwise circular interpolation on Axis 2 and 3
cmd = Motion_CenterAndLengthCircularIntplCommand()

# Set axes for this motion
cmd.SetAxis(0, 2)
cmd.SetAxis(1, 3)

# Set center position to (50, 0)
cmd.SetCenterPos(0, 50)
cmd.SetCenterPos(1, 0)

# Set motion parameters: counterclockwise (clockwise = 0), arc length, and profile settings
cmd.clockwise = 0  # 0 for counterclockwise
cmd.arcLengthDegree = 180
cmd.profile.type = ProfileType.Trapezoidal
cmd.profile.velocity = 1000
cmd.profile.acc = 10000
cmd.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cmd)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait for Axis 2 and 3 to finish motion
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Second Motion: Counterclockwise circular interpolation on Axis 2 and 3 with new center position (75, 0)
cmd = Motion_CenterAndLengthCircularIntplCommand()

cmd.SetAxis(0, 2)
cmd.SetAxis(1, 3)

cmd.SetCenterPos(0, 75)
cmd.SetCenterPos(1, 0)

cmd.clockwise = 0  # counterclockwise
cmd.arcLengthDegree = 180
cmd.profile.type = ProfileType.Trapezoidal
cmd.profile.velocity = 1000
cmd.profile.acc = 10000
cmd.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cmd)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Third Motion: Clockwise circular interpolation on Axis 2 and 3 with center position (25, 0)
cmd = Motion_CenterAndLengthCircularIntplCommand()

cmd.SetAxis(0, 2)
cmd.SetAxis(1, 3)

cmd.SetCenterPos(0, 25)
cmd.SetCenterPos(1, 0)

cmd.clockwise = 1  # 1 for clockwise
cmd.arcLengthDegree = 180
cmd.profile.type = ProfileType.Trapezoidal
cmd.profile.velocity = 1000
cmd.profile.acc = 10000
cmd.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cmd)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Fourth Motion: Clockwise circular interpolation on Axis 2 and 3 with center position (50, 0)
cmd = Motion_CenterAndLengthCircularIntplCommand()

cmd.SetAxis(0, 2)
cmd.SetAxis(1, 3)

cmd.SetCenterPos(0, 50)
cmd.SetCenterPos(1, 0)

cmd.clockwise = 1  # clockwise
cmd.arcLengthDegree = 180
cmd.profile.type = ProfileType.Trapezoidal
cmd.profile.velocity = 1000
cmd.profile.acc = 10000
cmd.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cmd)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
