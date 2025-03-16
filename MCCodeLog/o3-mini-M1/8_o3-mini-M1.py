
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 by a distance of 60 with a velocity of 1400.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 60
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov (60) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 8 stops moving.
Wmx3Lib_cm.motion.Wait(8)

# Define the series of relative moves: -30, 20, -30, 20, -30, 20, -30.
movements = [-30, 20, -30, 20, -30, 20, -30]

# Execute each movement command sequentially.
for move in movements:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = move
    posCommand.profile.velocity = 1400
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov (move ' + str(move) + ') error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis completes the current move.
    Wmx3Lib_cm.motion.Wait(8)
