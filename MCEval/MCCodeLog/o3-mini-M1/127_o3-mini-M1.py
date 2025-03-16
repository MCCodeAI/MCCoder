
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 0 to the position 130 at a speed of 1000 using a JerkLimitedFixedVelocityT profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 0
posCommand.target = 130
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to move from the current position to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until the axis stops moving.
Wmx3Lib_cm.motion.Wait(0)
