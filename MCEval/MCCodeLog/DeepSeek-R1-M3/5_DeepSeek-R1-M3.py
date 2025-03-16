
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Configure position command parameters for Axis 5
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Repeat the cycle 3 times
for _ in range(3):
    # Move to position 66.6
    posCommand.target = 66.6
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 stops moving
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Move back to position 0
    posCommand.target = 0
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 stops moving
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
