
# Axes = [8]
# IOInputs = []
# IOOutputs = []

def move_axis_8():
    # Create a position command for Axis 8 using the JerkRatioFixedVelocityT profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatioFixedVelocityT
    posCommand.axis = 8
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move Axis 8 from its current position to the target absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(8)

if __name__ == "__main__":
    move_axis_8()
