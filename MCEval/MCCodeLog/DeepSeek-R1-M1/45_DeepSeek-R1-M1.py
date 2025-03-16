
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 5
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.velocity = 1000  # Default velocity
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Move Axis 5 by 50
posCommand.target = 50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by -50
posCommand.target = -50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by 100
posCommand.target = 100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by -100
posCommand.target = -100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops
Wmx3Lib_cm.motion.Wait(5)
