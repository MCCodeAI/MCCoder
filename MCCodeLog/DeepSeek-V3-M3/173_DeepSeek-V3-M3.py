
# Axes = [1, 12]
# IOInputs = []
# IOOutputs = []

# Move Axis 12 to position 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000      # Example acceleration
posCommand.profile.dec = 10000      # Example deceleration

# Execute command to move Axis 12 to position 101
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 12 stops moving
Wmx3Lib_cm.motion.Wait(12)

# Get the status of Actual Torque and Pos Cmd for Axis 12
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

actualTorque = CmStatus.GetAxesStatus(12).actualTorque
posCmd = CmStatus.GetAxesStatus(12).posCmd

# Check if Actual Torque and Pos Cmd are the same
if actualTorque == posCmd:
    # Move Axis 1 to position 201
    posCommand.axis = 1
    posCommand.target = 201
else:
    # Move Axis 1 to position -201
    posCommand.axis = 1
    posCommand.target = -201

# Execute command to move Axis 1
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 stops moving
Wmx3Lib_cm.motion.Wait(1)
