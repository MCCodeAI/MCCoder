
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 1 to position 130.2 with a speed of 1060 and acceleration/deceleration of 11000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 130.2
posCommand.profile.velocity = 1060
posCommand.profile.acc = 11000
posCommand.profile.dec = 11000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to complete the motion before any further commands.
Wmx3Lib_cm.motion.Wait(1)
