
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

helicalCommand = Motion_HelicalIntplCommand()

# Execute Helical Motion with Axis 3 and 6 (circular) and Axis 4 (linear)
helicalCommand.SetAxis(0, 3)
helicalCommand.SetAxis(1, 6)
helicalCommand.zAxis = 4
helicalCommand.SetCenterPos(0, 50)
helicalCommand.SetCenterPos(1, 50)
helicalCommand.zEndPos = 200
helicalCommand.clockwise = 0  # 0 for counterclockwise
helicalCommand.arcLengthDegree = 1080
helicalCommand.profile.type = ProfileType.Trapezoidal
helicalCommand.profile.velocity = 2048
helicalCommand.profile.acc = 10000
helicalCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartHelicalIntplPos(helicalCommand)
if ret != 0:
    print('StartHelicalIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for all axes to complete motion
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 4)
axisSel.SetAxis(2, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
