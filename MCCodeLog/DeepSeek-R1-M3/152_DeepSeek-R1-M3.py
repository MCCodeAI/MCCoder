
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# List of target positions to move to
target_positions = [10, -10, 100, -100, 0]

for target in target_positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move to target position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(1)
