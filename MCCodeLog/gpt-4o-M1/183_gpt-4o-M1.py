
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 0 to the position -200 using a JerkLimited profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimited
posCommand.axis = 0
posCommand.target = -200
posCommand.profile.velocity = -1000
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
Wmx3Lib_cm.motion.Wait(0)
