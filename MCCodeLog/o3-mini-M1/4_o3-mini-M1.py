
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 4 to a specified position.
# If the variable XYZ equals 0, it will move Axis 4 to position 88 with a velocity of 1100.
# Otherwise, it will move Axis 4 to position 90 (using the same velocity here for consistency).
#
# It waits for Axis 4 to finish moving before completing the function call.

def move_axis4(XYZ):
    # Create a position command for the motion.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4

    # Set target and speed based on the condition.
    if XYZ == 0:
        posCommand.target = 88
        posCommand.profile.velocity = 1100
    else:
        posCommand.target = 90
        posCommand.profile.velocity = 1100

    # Set acceleration and deceleration values.
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Start the absolute position command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 4 finishes moving.
    ret = Wmx3Lib_cm.motion.Wait(4)
    if ret != 0:
        print('Wait error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

# Example usage:
XYZ = 0  # Set XYZ to 0 or any other value to test the branch.
move_axis4(XYZ)
