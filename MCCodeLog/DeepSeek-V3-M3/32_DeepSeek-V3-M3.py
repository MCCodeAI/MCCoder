
# Axes = [2, 3]
# IOInputs = []
# IOOutputs = []

# Execute counterclockwise circular interpolation for Axis 2 and 3 with center position (50, 0), arc length 180, and velocity 1000.
circularIntplCommand1 = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand1.SetAxis(0, 2)
circularIntplCommand1.SetAxis(1, 3)
circularIntplCommand1.SetCenterPos(0, 50)
circularIntplCommand1.SetCenterPos(1, 0)
circularIntplCommand1.clockwise = 0  # 0 for counterclockwise
circularIntplCommand1.arcLengthDegree = 180
circularIntplCommand1.profile.type = ProfileType.Trapezoidal
circularIntplCommand1.profile.velocity = 1000
circularIntplCommand1.profile.acc = 10000
circularIntplCommand1.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand1)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel1 = AxisSelection()
axisSel1.axisCount = 2
axisSel1.SetAxis(0, 2)
axisSel1.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel1)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute counterclockwise circular interpolation for Axis 2 and 3 with center position (75, 0), arc length 180, and velocity 1000.
circularIntplCommand2 = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand2.SetAxis(0, 2)
circularIntplCommand2.SetAxis(1, 3)
circularIntplCommand2.SetCenterPos(0, 75)
circularIntplCommand2.SetCenterPos(1, 0)
circularIntplCommand2.clockwise = 0  # 0 for counterclockwise
circularIntplCommand2.arcLengthDegree = 180
circularIntplCommand2.profile.type = ProfileType.Trapezoidal
circularIntplCommand2.profile.velocity = 1000
circularIntplCommand2.profile.acc = 10000
circularIntplCommand2.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand2)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel2 = AxisSelection()
axisSel2.axisCount = 2
axisSel2.SetAxis(0, 2)
axisSel2.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel2)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute clockwise circular interpolation for Axis 2 and 3 with center position (25, 0), arc length 180, and velocity 1000.
circularIntplCommand3 = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand3.SetAxis(0, 2)
circularIntplCommand3.SetAxis(1, 3)
circularIntplCommand3.SetCenterPos(0, 25)
circularIntplCommand3.SetCenterPos(1, 0)
circularIntplCommand3.clockwise = 1  # 1 for clockwise
circularIntplCommand3.arcLengthDegree = 180
circularIntplCommand3.profile.type = ProfileType.Trapezoidal
circularIntplCommand3.profile.velocity = 1000
circularIntplCommand3.profile.acc = 10000
circularIntplCommand3.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand3)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel3 = AxisSelection()
axisSel3.axisCount = 2
axisSel3.SetAxis(0, 2)
axisSel3.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel3)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute clockwise circular interpolation for Axis 2 and 3 with center position (50, 0), arc length 180, and velocity 1000.
circularIntplCommand4 = Motion_CenterAndLengthCircularIntplCommand()
circularIntplCommand4.SetAxis(0, 2)
circularIntplCommand4.SetAxis(1, 3)
circularIntplCommand4.SetCenterPos(0, 50)
circularIntplCommand4.SetCenterPos(1, 0)
circularIntplCommand4.clockwise = 1  # 1 for clockwise
circularIntplCommand4.arcLengthDegree = 180
circularIntplCommand4.profile.type = ProfileType.Trapezoidal
circularIntplCommand4.profile.velocity = 1000
circularIntplCommand4.profile.acc = 10000
circularIntplCommand4.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand4)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete.
axisSel4 = AxisSelection()
axisSel4.axisCount = 2
axisSel4.SetAxis(0, 2)
axisSel4.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel4)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
