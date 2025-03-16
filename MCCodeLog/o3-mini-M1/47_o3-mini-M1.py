
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 7 to the absolute positions 50, -50, 100, and -100, one after the other.
# After each motion command is started, the code waits until Axis 7 stops moving before issuing the next command.

def move_axis(axis, target, velocity=1000, acc=10000, dec=10000):
    # Create a position command for the given axis and target position.
    posCommand = Motion_PosCommand()
    posCommand.axis = axis
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = acc
    posCommand.profile.dec = dec
    posCommand.target = target

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error for Axis {} moving to {}: {}: {}".format(
            axis, target, ret, Wmx3Lib_cm.ErrorToString(ret)))
        return False
    return True

def main():
    # Define the target positions for Axis 7 in order.
    targets = [50, -50, 100, -100]

    for target in targets:
        if not move_axis(7, target):
            print("Motion command aborted at target:", target)
            break

        # Wait for Axis 7 to finish moving before starting the next motion.
        ret = Wmx3Lib_cm.motion.Wait(7)
        if ret != 0:
            print("Wait error for Axis 7 at target {}: {}: {}".format(
                target, ret, Wmx3Lib_cm.ErrorToString(ret)))
            break

if __name__ == "__main__":
    main()
