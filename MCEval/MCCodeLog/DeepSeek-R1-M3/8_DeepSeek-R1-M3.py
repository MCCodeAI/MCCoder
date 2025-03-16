
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 8 with velocity 1400
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.profile.velocity = 1400
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# First relative move of 60
posCommand.target = 60
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 8 stops moving
Wmx3Lib_cm.motion.Wait(8)

# Subsequent relative moves
distances = [-30, 20, -30, 20, -30, 20, -30]
for distance in distances:
    posCommand.target = distance
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    Wmx3Lib_cm.motion.Wait(8)
