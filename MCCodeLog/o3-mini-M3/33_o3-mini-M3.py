
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

# Create and configure the helical interpolation command.
# This command performs a counterclockwise circular interpolation on Axis 3 and 6,
# with a center position of (50, 50) and a rotation degree of 1080,
# while concurrently moving Axis 4 linearly to position 200.
helicalCommand = Motion_HelicalIntplCommand()

# Set the circular interpolation axes.
helicalCommand.SetAxis(0, 3)
helicalCommand.SetAxis(1, 6)

# Set the linear axis.
helicalCommand.zAxis = 4

# Set the center position for the circular part.
helicalCommand.SetCenterPos(0, 50)
helicalCommand.SetCenterPos(1, 50)

# Set the final linear position for the helical motion.
helicalCommand.zEndPos = 200

# For counterclockwise circular interpolation, set clockwise flag to 0.
helicalCommand.clockwise = 0

# Set the rotation arc in degrees.
helicalCommand.arcLengthDegree = 1080

# Configure the motion profile.
helicalCommand.profile.type = ProfileType.Trapezoidal
helicalCommand.profile.velocity = 2048
helicalCommand.profile.acc = 10000
helicalCommand.profile.dec = 10000

# Start the helical interpolation motion.
ret = Wmx3Lib_cm.motion.StartHelicalIntplPos(helicalCommand)
if ret != 0:
    print('StartHelicalIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Depending on the application, you may want to exit or handle the error here.
    
# Wait for the motion to complete for all involved axes (3, 6, and 4).
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 6)
axisSel.SetAxis(2, 4)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Error handling can be implemented here.
