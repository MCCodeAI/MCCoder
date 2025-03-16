
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Create a position command object
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.velocity = 1000  # Set a default velocity
posCommand.profile.acc = 10000      # Set a default acceleration
posCommand.profile.dec = 10000      # Set a default deceleration

# Move Axis 5 by a distance of 50
posCommand.target = 50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by a distance of -50
posCommand.target = -50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by a distance of 100
posCommand.target = 100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by a distance of -100
posCommand.target = -100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)
