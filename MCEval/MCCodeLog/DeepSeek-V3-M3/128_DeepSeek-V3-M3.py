
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to the position 2, -2, and 2 using JerkLimitedSCurve profile
positions = [2, -2, 2]
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedSCurve
    posCommand.axis = 2
    posCommand.target = pos
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(2)
