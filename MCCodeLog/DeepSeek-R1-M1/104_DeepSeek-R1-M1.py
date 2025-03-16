
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a command value for the first movement
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 80
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration
posCommand.profile.endVelocity = 800  # End velocity for the first movement

# Execute command to move to the first target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the first target position and stops
Wmx3Lib_cm.motion.Wait(2)

# Create a command value for the second movement
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 100
posCommand.profile.velocity = 800  # Start velocity for the second movement
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration

# Execute command to move to the second target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the second target position and stops
Wmx3Lib_cm.motion.Wait(2)
