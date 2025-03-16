
# Determine the target distance based on the variable x
x = False  # Define the variable x with appropriate value
if x == False:
    target_distance = -70
else:
    target_distance = 70

# Create a relative position command for Axis 9
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.target = target_distance
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 9 by the specified distance
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 9 completes the motion and stops
Wmx3Lib_cm.motion.Wait(9)
