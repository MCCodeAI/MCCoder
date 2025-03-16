
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to multiple positions using Advanced-S profile
positions = [-20, 30, -40, 0]

for target_pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.AdvancedS
    posCommand.axis = 3
    posCommand.target = target_pos
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error code is {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        break

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(3)
