
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 6 to 50, -50, 100, and -100 sequentially.
# After each motion command, it waits for the axis to stop moving before starting the next motion.

# Assume that the following objects and methods are available from the motion library:
#   - Motion_PosCommand
#   - ProfileType
#   - Wmx3Lib_cm.motion.StartMov(pos)
#   - Wmx3Lib_cm.motion.Wait(axis)
#   - Wmx3Lib_cm.ErrorToString(ret)
#
# No external motion libraries are imported, as per guidelines.

# Create a Motion_PosCommand instance for Axis 6
pos = Motion_PosCommand()
pos.axis = 6
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Define a helper function to execute a move and wait for the axis to stop.
def move_and_wait(target_position):
    pos.target = target_position
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return ret
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return ret

# Move Axis 6 to position 50
if move_and_wait(50) != 0:
    exit(1)

# Move Axis 6 to position -50
if move_and_wait(-50) != 0:
    exit(1)

# Move Axis 6 to position 100
if move_and_wait(100) != 0:
    exit(1)

# Move Axis 6 to position -100
if move_and_wait(-100) != 0:
    exit(1)
