
# Axes = [5]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

for _ in range(3):
    # Move to position 66.6 at 900 velocity
    posCommand.target = 66.6
    posCommand.profile.velocity = 900
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for axis to stop
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Move back to position 0 at 900 velocity
    posCommand.target = 0
    posCommand.profile.velocity = 900
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for axis to stop
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
