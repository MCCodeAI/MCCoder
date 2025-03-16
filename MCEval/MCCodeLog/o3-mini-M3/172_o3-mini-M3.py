
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Define the sequence of target positions for Axis 1.
positions = [10, -10, 10, -10, 10, -10, 10, -10, 0]

for target in positions:
    # Create a position command using the TimeAccSCurve profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 1 has moved to the target position and stopped.
    Wmx3Lib_cm.motion.Wait(1)
