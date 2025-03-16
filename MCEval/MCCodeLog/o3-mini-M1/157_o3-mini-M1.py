
# Axes = [7]
# IOInputs = []
# IOOutputs = []

def move_axis_7():
    # Create a motion command object for axis movement
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
    posCommand.axis = 7
    posCommand.target = -99
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0
    # secondVelocity must be greater than the profile velocity
    posCommand.profile.secondVelocity = 2000

    # Execute command to move from the current position to the target position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 7 completes the motion and stops.
    Wmx3Lib_cm.motion.Wait(7)

if __name__ == "__main__":
    move_axis_7()
