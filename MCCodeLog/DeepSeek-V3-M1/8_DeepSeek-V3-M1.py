
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 by a distance of 60 with a velocity of 1400
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 60
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to a specified distance relatively.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(8)

# Move Axis 8 by a distance of -30, 20, -30, 20, -30, 20, -30 respectively
distances = [-30, 20, -30, 20, -30, 20, -30]

for distance in distances:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = distance
    posCommand.profile.velocity = 1400
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to a specified distance relatively.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(8)
