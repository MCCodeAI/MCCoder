
# Axes = [5]
# Inputs = []
# Outputs = []

# Define the motion command for Axis 5
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000     # Example acceleration
posCommand.profile.dec = 10000     # Example deceleration

# Move Axis 5 by 50
posCommand.target = 50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by -50
posCommand.target = -50
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by 100
posCommand.target = 100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 5 by -100
posCommand.target = -100
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)
