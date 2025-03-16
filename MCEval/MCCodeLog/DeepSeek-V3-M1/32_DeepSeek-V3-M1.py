
# Axes = [2, 3]
# IOInputs = []
# IOOutputs = []

# Execute counterclockwise circular interpolation for Axis 2 and 3 with center position (50, 0), arc length 180, and velocity 1000.
circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand.SetAxis(0, 2)
circularIntplCommand.SetAxis(1, 3)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 0)
circularIntplCommand.clockwise = 0  # 0 for counterclockwise
circularIntplCommand.arcLengthDegree = 180
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1000
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute counterclockwise circular interpolation for Axis 2 and 3 with center position (75, 0), arc length 180, and velocity 1000.
circularIntplCommand.SetCenterPos(0, 75)
circularIntplCommand.SetCenterPos(1, 0)
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute clockwise circular interpolation for Axis 2 and 3 with center position (25, 0), arc length 180, and velocity 1000.
circularIntplCommand.SetCenterPos(0, 25)
circularIntplCommand.SetCenterPos(1, 0)
circularIntplCommand.clockwise = 1  # 1 for clockwise
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute clockwise circular interpolation for Axis 2 and 3 with center position (50, 0), arc length 180, and velocity 1000.
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 0)
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
