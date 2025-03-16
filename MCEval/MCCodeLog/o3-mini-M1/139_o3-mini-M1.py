
# Axes = [30]
# IOInputs = []
# IOOutputs = []

# List of target positions for Axis 30
positions = [-310, 100, -40, 0]

for target_pos in positions:
    # Create a new position command for each target position
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT  # T-MAT profile
    posCommand.axis = 30
    posCommand.target = target_pos
    posCommand.profile.velocity = 10020
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.movingAverageTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the absolute position command for Axis 30
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis reaches the target position and stops
    Wmx3Lib_cm.motion.Wait(30)
