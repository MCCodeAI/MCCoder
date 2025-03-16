
# Axes = [1, 12]
# IOInputs = []
# IOOutputs = []

# Move axis 12 to position 101.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move axis 12 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until axis 12 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(12)

# Get the status of actual torque and position command.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

actualTorque = CmStatus.GetAxesStatus(12).actualTorque
posCmd = CmStatus.GetAxesStatus(12).posCmd

# If actual torque and position command are the same, move axis 1 to 201.
# Otherwise, move axis 1 to -201.
if actualTorque == posCmd:
    posCommand.axis = 1
    posCommand.target = 201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    posCommand.axis = 1
    posCommand.target = -201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait until axis 1 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
