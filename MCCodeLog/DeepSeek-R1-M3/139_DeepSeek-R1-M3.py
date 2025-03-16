
# Axes = [30]
# IOInputs = []
# IOOutputs = []

# Move Axis 30 to the position -0310, 100, -40, and 0 using T-MAT profile
positions = [-310, 100, -40, 0]

for target_pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT
    posCommand.axis = 30
    posCommand.target = target_pos
    posCommand.profile.velocity = 10020
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.movingAverageTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move to target position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(30)
