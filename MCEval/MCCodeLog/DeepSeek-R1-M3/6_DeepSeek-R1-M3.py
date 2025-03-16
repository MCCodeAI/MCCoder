
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Start a relative position command of Axis 6 with 199.9 distance and 2000 velocity.
# Create a command value of target as 199.9.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to a specified distance relatively.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
