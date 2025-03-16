
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get the status of Axis 1
axis = 1
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Get the position command and actual position of Axis 1
posCmd = CmStatus.GetAxesStatus(axis).posCmd
actualPos = CmStatus.GetAxesStatus(axis).actualPos

# Check if position command and actual position are the same
if posCmd == actualPos:
    # Move Axis 1 to 201
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = 201
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 1 to -201
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = -201
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
