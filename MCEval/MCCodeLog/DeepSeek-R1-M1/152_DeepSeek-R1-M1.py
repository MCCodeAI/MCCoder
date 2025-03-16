
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Move Axis 1 to positions 10, -10, 100, -100, and 0 using TimeAccSCurve profile
positions = [10, -10, 100, -100, 0]

for target_pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = target_pos
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(1)
