
# Axes = [3, 4]
# IOInputs = []
# IOOutputs = []

def move_axis(axis, target, velocity):
    # Create a command value to move the axis to an absolute target position
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocitySCurve
    posCommand.axis = axis
    posCommand.target = target
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0
    posCommand.profile.secondVelocity = 5000  # second velocity must be higher than the first velocity

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis reaches the target position and stops.
    Wmx3Lib_cm.motion.Wait(axis)


def main():
    # Move Axis 3 to position 33 with a speed of 1000 using a TwoVelocitySCurve profile.
    move_axis(3, 33, 1000)
    
    # After Axis 3 stops, move Axis 4 to position 77 with the same profile and speed.
    move_axis(4, 77, 1000)


if __name__ == '__main__':
    main()
