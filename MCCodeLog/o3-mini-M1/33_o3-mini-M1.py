
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

# Create a helical interpolation command instance.
helicalCommand = Motion_HelicalIntplCommand()

# Configure the helical motion command:
# - Circular interpolation on Axis 3 and Axis 6
# - Concurrent linear motion on Axis 4 (z axis)
helicalCommand.SetAxis(0, 3)
helicalCommand.SetAxis(1, 6)
helicalCommand.zAxis = 4

# Set the center position for the circular interpolation.
helicalCommand.SetCenterPos(0, 50)
helicalCommand.SetCenterPos(1, 50)

# Set the linear end position for Axis 4.
helicalCommand.zEndPos = 200

# Set the rotation and direction: 1080° rotation,
# with a counterclockwise rotation (clockwise flag = 0 for counterclockwise).
helicalCommand.arcLengthDegree = 1080
helicalCommand.clockwise = 0  # 0 indicates counterclockwise motion

# Configure the motion profile.
helicalCommand.profile.type = ProfileType.Trapezoidal
helicalCommand.profile.velocity = 2048
helicalCommand.profile.acc = 10000
helicalCommand.profile.dec = 10000

# Start the helical interpolation motion command.
ret = Wmx3Lib_cm.motion.StartHelicalIntplPos(helicalCommand)
if ret != 0:
    print('StartHelicalIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Depending on the application, add return or exit here.

# Wait for the motion to complete on Axis 3, Axis 6 and Axis 4.
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
axisSel.SetAxis(2, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Depending on the application, add return or exit here.
