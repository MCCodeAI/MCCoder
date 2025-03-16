
# Axes = [5]
# IOInputs = []
# IOOutputs = []

def main():
    # Create and configure the position command using a Sine profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Sine
    posCommand.axis = 5
    posCommand.target = 550
    posCommand.profile.velocity = 100000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 stops moving.
    Wmx3Lib_cm.motion.Wait(5)

if __name__ == '__main__':
    main()
