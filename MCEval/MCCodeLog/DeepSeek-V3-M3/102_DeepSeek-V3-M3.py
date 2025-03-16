
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to 200 and Axis 4 to 110
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 4
posCommand.target = 110
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until both axes stop moving
Wmx3Lib_cm.motion.Wait(2)
Wmx3Lib_cm.motion.Wait(4)

# Check if the difference between Axis 2 and Axis 4 position commands is 90
axisStatus2 = Wmx3Lib_cm.motion.GetAxisStatus(2)
axisStatus4 = Wmx3Lib_cm.motion.GetAxisStatus(4)

if axisStatus2.posCommand - axisStatus4.posCommand == 90:
    # Move Axis 2 and 4 to 300
    posCommand.axis = 2
    posCommand.target = 300
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    posCommand.axis = 4
    posCommand.target = 300
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 2 and 4 to 50
    posCommand.axis = 2
    posCommand.target = 50
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    posCommand.axis = 4
    posCommand.target = 50
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait until both axes stop moving
Wmx3Lib_cm.motion.Wait(2)
Wmx3Lib_cm.motion.Wait(4)
