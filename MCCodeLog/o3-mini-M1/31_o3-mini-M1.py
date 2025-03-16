
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

def main():
    # Create the circular interpolation motion command object
    circularIntplCommand = Motion_CenterAndLengthCircularIntplCommand()

    # Configure axes for the motion (Axis 1 and Axis 4)
    circularIntplCommand.SetAxis(0, 1)
    circularIntplCommand.SetAxis(1, 4)

    # Set the center position for the circular interpolation motion to (50, 50)
    circularIntplCommand.SetCenterPos(0, 50)  # Center X position
    circularIntplCommand.SetCenterPos(1, 50)  # Center Y position

    # Set the motion parameters:
    # Set counterclockwise rotation (clockwise flag = 0) according to instruction guidance
    circularIntplCommand.clockwise = 0  
    circularIntplCommand.arcLengthDegree = 270
    circularIntplCommand.profile.type = ProfileType.Trapezoidal
    circularIntplCommand.profile.velocity = 1000
    circularIntplCommand.profile.acc = 10000
    circularIntplCommand.profile.dec = 10000

    # Start the circular interpolation motion command
    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularIntplCommand)
    if ret != 0:
        print('StartCircularIntplPos_CenterAndLength error code is ' + str(ret) + ': ' +
              Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the motion to complete on Axis 1 and Axis 4
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 4)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' +
              Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
