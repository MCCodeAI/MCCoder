
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Assume x is defined somewhere before this code.
# If x is False, move Axis 9 by -70 with velocity 1200; otherwise, move it by 70 with velocity 1200.

# Create a motion command for a relative move on Axis 9.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9

if not x:
    posCommand.target = -70
else:
    posCommand.target = 70

posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the relative motion command.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 9 moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(9)
