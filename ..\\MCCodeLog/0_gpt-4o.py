
# Axes = [1]
# Write Python code to Move axis 1 to position 2001.5 at a speed of 13000.

# Create a command value for the target position and speed.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 2001.5
posCommand.profile.velocity = 13000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
