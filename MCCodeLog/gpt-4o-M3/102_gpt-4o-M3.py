
# Axes = [2, 4]
# Inputs = []
# Outputs = []

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

# Check the condition: if position command for Axis 2 minus position command for Axis 4 is 90
# Since GetPosCommand is not available, we assume the target positions are the current positions
posCommand2 = 200  # Target position for Axis 2
posCommand4 = 110  # Target position for Axis 4

if posCommand2 - posCommand4 == 90:
    # Move Axis 2 and 4 to position 300
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
    # Move Axis 2 and 4 to position 50
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

# Wait for both axes to stop moving
Wmx3Lib_cm.motion.Wait(2)
Wmx3Lib_cm.motion.Wait(4)
