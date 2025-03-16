
# Axes = [15]
# IOInputs = []
# IOOutputs = []

def move_axis_15():
    # Create a position command to move Axis 15 using a Parabolic profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Parabolic
    posCommand.axis = 15
    posCommand.target = -410
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to the specified target position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 15 reaches the target position and stops moving.
    Wmx3Lib_cm.motion.Wait(15)

# Initiate the move command.
move_axis_15()
