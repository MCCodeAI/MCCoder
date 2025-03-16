
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def move_axis(target_position):
    # Create the absolute position command for Axis 9 using the TimeAccParabolic profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccParabolic
    posCommand.axis = 9
    posCommand.target = target_position
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50000000000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Start the motion.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 9 stops moving.
    Wmx3Lib_cm.motion.Wait(9)

# Sequentially move Axis 9 to the positions in the given order.
move_axis(-911)
move_axis(911)
move_axis(168)
move_axis(0)
