
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 5 by distances of 50, -50, 100, and -100 sequentially with blocking waits.

# List of move distances
move_distances = [50, -50, 100, -100]

for distance in move_distances:
    # Create a motion command for a relative move on Axis 5.
    posCommand = Motion_PosCommand()
    posCommand.axis = 5
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 1000   # Default velocity (modify if needed)
    posCommand.profile.acc = 10000       # Default acceleration
    posCommand.profile.dec = 10000       # Default deceleration
    posCommand.target = distance         # Set the relative move distance

    # Execute the relative move command on Axis 5.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 has completed its movement.
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
