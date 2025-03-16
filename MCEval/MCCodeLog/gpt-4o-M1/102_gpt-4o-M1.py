
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to position 200
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

Wmx3Lib_cm.motion.Wait(2)

# Move Axis 4 to position 110
posCommand.axis = 4
posCommand.target = 110

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Check the condition: if position command of Axis 2 minus position command of Axis 4 is 90
posCmdAxis2 = Wmx3Lib_cm.motion.GetPosCommand(2)
posCmdAxis4 = Wmx3Lib_cm.motion.GetPosCommand(4)

if (posCmdAxis2 - posCmdAxis4) == 90:
    # Move Axis 2 and 4 to position 300
    posCommand.axis = 2
    posCommand.target = 300

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    posCommand.axis = 4
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

else:
    # Move Axis 2 and 4 to position 50
    posCommand.axis = 2
    posCommand.target = 50

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    posCommand.axis = 4
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait for both axes to complete motion
Wmx3Lib_cm.motion.Wait(2)
Wmx3Lib_cm.motion.Wait(4)
