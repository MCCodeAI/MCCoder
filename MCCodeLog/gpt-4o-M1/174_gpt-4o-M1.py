
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to the position -20, 30, -40, and 0 with specified motion profile parameters.
positions = [-20, 30, -40, 0]
for position in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.AdvancedS
    posCommand.axis = 3
    posCommand.target = position
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(3)
