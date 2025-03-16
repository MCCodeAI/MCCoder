
# Axes = [1]
# IOInputs = []
# IOOutputs = []

import time

# Get Axis status
axisStatus = Wmx3Lib_cm.axis.GetStatus(1)
print("Axis 1 status:", axisStatus)

# Create a command value of target as 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(1)

# Get the current status of Axis 1
axisStatus = Wmx3Lib_cm.axis.GetStatus(1)
commandPos = axisStatus.posCommand
actualPos = axisStatus.actualPos

print(f"Command Position: {commandPos}, Actual Position: {actualPos}")

if commandPos == actualPos:
    # Move to 201 if positions match
    posCommand.target = 201
else:
    # Move to -201 if positions do not match
    posCommand.target = -201

# Execute command to move to new target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the axis moves to the new target position and stops
Wmx3Lib_cm.motion.Wait(1)
