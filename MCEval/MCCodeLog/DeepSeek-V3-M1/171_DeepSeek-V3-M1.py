
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get the status of Axis 1
axis_status = Wmx3Lib_cm.motion.GetAxisStatus(1)
if axis_status != 0:
    print('GetAxisStatus error code is ' + str(axis_status) + ': ' + Wmx3Lib_cm.ErrorToString(axis_status))
    return

# Move Axis 1 to position 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 stops moving
Wmx3Lib_cm.motion.Wait(1)

# Get the status of position command and actual position
command_position = Wmx3Lib_cm.motion.GetCommandPosition(1)
actual_position = Wmx3Lib_cm.motion.GetActualPosition(1)

if command_position == actual_position:
    # Move Axis 1 to position 201
    posCommand.target = 201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 1 to position -201
    posCommand.target = -201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait until Axis 1 stops moving
Wmx3Lib_cm.motion.Wait(1)
