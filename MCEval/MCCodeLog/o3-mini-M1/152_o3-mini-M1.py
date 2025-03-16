
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# List of target positions for Axis 1.
positions = [10, -10, 100, -100, 0]

for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = pos
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from the current position to the desired absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 1 stops moving before issuing the next motion.
    Wmx3Lib_cm.motion.Wait(1)
