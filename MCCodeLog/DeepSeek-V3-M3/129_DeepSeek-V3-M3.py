
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Move Axis 9 to the position -911, 911, 168, and 0 at a speed of 1000, accTimeMilliseconds of 50ms, decTimeMilliseconds of 500ms, using a TimeAcc with Parabolic profile.

# Define the positions to move to
positions = [-911, 911, 168, 0]

# Loop through each position and move Axis 9
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccParabolic
    posCommand.axis = 9
    posCommand.target = pos
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 500  # Adjusted to a reasonable value
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(9)
