
# Axes = [12, 1]
# IOInputs = []
# IOOutputs = []

# Import required modules
import time

# Create position command for Axis 12
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 500
posCommand.profile.acc = 5000
posCommand.profile.dec = 5000

# Execute command to move Axis 12 to target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 12 moves to target position and stops
Wmx3Lib_cm.motion.Wait(12)

# Get Actual Torque and Position Command status
actualTorque = Wmx3Lib_cm.status.GetActualTorque(12)
posCmd = Wmx3Lib_cm.status.GetPosCommand(12)

# Create position command for Axis 1
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.profile.velocity = 500
posCommand.profile.acc = 5000
posCommand.profile.dec = 5000

# Check if Actual Torque and Position Command are the same
if actualTorque == posCmd:
    posCommand.target = 201
else:
    posCommand.target = -201

# Execute command to move Axis 1 to target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 1 moves to target position and stops
Wmx3Lib_cm.motion.Wait(1)
