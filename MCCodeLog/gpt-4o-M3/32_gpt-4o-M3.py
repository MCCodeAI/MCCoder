
# Axes = [2, 3]
# Inputs = []
# Outputs = []

# Define a function to execute a circular interpolation motion
def execute_circular_interpolation(axis1, axis2, center_x, center_y, arc_length, velocity, clockwise):
    circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()
    circularIntplCommand.SetAxis(0, axis1)
    circularIntplCommand.SetAxis(1, axis2)
    circularIntplCommand.SetCenterPos(0, center_x)
    circularIntplCommand.SetCenterPos(1, center_y)
    circularIntplCommand.clockwise = clockwise
    circularIntplCommand.arcLengthDegree = arc_length
    circularIntplCommand.profile.type = ProfileType.Trapezoidal
    circularIntplCommand.profile.velocity = velocity
    circularIntplCommand.profile.acc = 10000
    circularIntplCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
    if ret != 0:
        print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, axis1)
    axisSel.SetAxis(1, axis2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Execute the series of circular interpolations
execute_circular_interpolation(2, 3, 50, 0, 180, 1000, 0)  # Counterclockwise
execute_circular_interpolation(2, 3, 75, 0, 180, 1000, 0)  # Counterclockwise
execute_circular_interpolation(2, 3, 25, 0, 180, 1000, 1)  # Clockwise
execute_circular_interpolation(2, 3, 50, 0, 180, 1000, 1)  # Clockwise
