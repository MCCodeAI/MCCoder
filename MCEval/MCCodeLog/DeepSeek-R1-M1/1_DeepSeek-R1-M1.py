
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Create a command value of target as 130.2
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 130.2
posCommand.profile.velocity = 1060
posCommand.profile.acc = 11000
posCommand.profile.dec = 11000

# Execute command to move to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(1)
