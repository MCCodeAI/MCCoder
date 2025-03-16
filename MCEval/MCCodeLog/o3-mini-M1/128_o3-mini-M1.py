
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to position 2, then to -2, then back to 2 using a JerkLimitedSCurve profile.
# For each move, wait until the axis stops moving.

def move_axis_2(target_position):
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedSCurve
    posCommand.axis = 2
    posCommand.target = target_position
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 2 moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(2)

def main():
    # First move: move Axis 2 to position 2.
    move_axis_2(2)

    # Second move: move Axis 2 to position -2.
    move_axis_2(-2)

    # Third move: move Axis 2 back to position 2.
    move_axis_2(2)

if __name__ == "__main__":
    main()
