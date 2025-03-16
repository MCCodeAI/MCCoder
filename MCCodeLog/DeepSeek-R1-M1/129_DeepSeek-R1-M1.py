
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Move Axis 9 to multiple positions using TimeAccParabolic profile
positions = [-911, 911, 168, 0]

for target_pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccParabolic
    posCommand.axis = 9
    posCommand.target = target_pos
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50000000000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move to target position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis reaches the target position and stops
    Wmx3Lib_cm.motion.Wait(9)
