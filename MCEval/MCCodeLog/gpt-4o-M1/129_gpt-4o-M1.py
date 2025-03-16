
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Move Axis 9 to the specified positions with the given profile parameters.
positions = [-911, 911, 168, 0]
velocity = 1000
accTimeMilliseconds = 50
decTimeMilliseconds = 50000000000

for position in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccParabolic
    posCommand.axis = 9
    posCommand.target = position
    posCommand.profile.velocity = velocity
    posCommand.profile.accTimeMilliseconds = accTimeMilliseconds
    posCommand.profile.decTimeMilliseconds = decTimeMilliseconds
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(9)
