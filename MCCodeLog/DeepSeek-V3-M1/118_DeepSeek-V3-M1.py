
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to the position -10, 10, -10, and 0 at a speed of 1000 using a twoVelTrapezoidal profile.

# Define the positions to move to
positions = [-10, 10, -10, 0]

# Loop through each position and move Axis 4
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelTrapezoidal
    posCommand.axis = 4
    posCommand.target = pos
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(4)
