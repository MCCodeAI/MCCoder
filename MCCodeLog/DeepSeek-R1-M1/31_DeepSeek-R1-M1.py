
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()

# Execute Counterclockwise Circular Interpolation of Axis 1 and 4 with center position (50, 50), arc length 270, velocity 1000.
circularIntplCommand.SetAxis(0, 1)
circularIntplCommand.SetAxis(1, 4)
circularIntplCommand.SetCenterPos(0, 50)
circularIntplCommand.SetCenterPos(1, 50)
circularIntplCommand.clockwise = 0  # 0 for counterclockwise direction
circularIntplCommand.arcLengthDegree = 270
circularIntplCommand.profile.type = ProfileType.Trapezoidal
circularIntplCommand.profile.velocity = 1000
circularIntplCommand.profile.acc = 10000
circularIntplCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
if ret != 0:
    print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 1 and 4 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
