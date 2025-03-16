
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 3 to position 30, 0, 30, and 0 using ConstantDec profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3

# List of target positions to move to
target_positions = [30, 0, 30, 0]

for target in target_positions:
    posCommand.target = target
    posCommand.profile.startingVelocity = 100
    posCommand.profile.endVelocity = 0

    # Execute the motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(3)
