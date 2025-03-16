
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

# Create a command value for moving Axis 3 and 4 to their respective positions.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 36
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 3 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Modify the command for Axis 4.
posCommand.axis = 4
posCommand.target = 45

# Execute command to move Axis 4 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until both axes (3 and 4) move to their target positions and stop.
Wmx3Lib_cm.motion.Wait(3)
Wmx3Lib_cm.motion.Wait(4)

# Create a command value for moving Axis 6 to its position.
posCommand.axis = 6
posCommand.target = 108

# Execute command to move Axis 6 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
