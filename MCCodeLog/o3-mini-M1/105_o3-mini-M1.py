
# Axes = [5]
# IOInputs = []
# IOOutputs = []

def main():
    # First, move Axis 5 to an absolute position of 180 with a velocity of 1100.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 180
    posCommand.profile.velocity = 1100
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code:', ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 reaches 180 and comes to a complete stop.
    Wmx3Lib_cm.motion.Wait(5)

    # Next, move Axis 5 by a relative distance of -10 for 5 times.
    for i in range(5):
        # Create a relative move command for Axis 5.
        relCommand = Motion_PosCommand()
        relCommand.profile.type = ProfileType.Trapezoidal
        relCommand.axis = 5
        relCommand.target = -10  # This value indicates the distance to move relative to current position.
        relCommand.profile.velocity = 1100
        relCommand.profile.acc = 10000
        relCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartMov(relCommand)
        if ret != 0:
            print('StartMov error on iteration', i+1, ':', ret, Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until Axis 5 completes the move.
        Wmx3Lib_cm.motion.Wait(5)

if __name__ == '__main__':
    main()
