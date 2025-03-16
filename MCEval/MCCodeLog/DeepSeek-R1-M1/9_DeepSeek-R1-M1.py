
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Determine the target distance based on the variable x
if x == False:
    target_distance = -70
else:
    target_distance = 70

# Create and configure the position command for Axis 9
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.target = target_distance
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute relative position command
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 9 completes the motion
Wmx3Lib_cm.motion.Wait(9)
