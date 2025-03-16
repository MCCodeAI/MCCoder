
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Move Axis 9 to multiple positions using TimeAccParabolic profile
target_positions = [-911, 911, 168, 0]

for target in target_positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccParabolic
    posCommand.axis = 9
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50  # Reduced to a reasonable value
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0
    posCommand.profile.jerkAccRatio = 1.0  # Added jerk ratio to ensure smooth motion

    # Execute command to move to target position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(9)
