
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def move_axis(target_position):
    # Create a motion position command for Axis 3 using the AdvancedS profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.AdvancedS
    posCommand.axis = 3
    posCommand.target = target_position
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(3)
    return True

def main():
    # Define the sequence of target positions for Axis 3.
    targets = [-20, 30, -40, 0]
    
    # Execute each move sequentially.
    for position in targets:
        if not move_axis(position):
            # If an error occurs, break out of the sequence.
            break

if __name__ == "__main__":
    main()
