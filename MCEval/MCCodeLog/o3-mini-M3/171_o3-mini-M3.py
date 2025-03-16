
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Get the status of position command and actual position for Axis 1.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# For Axis 1, retrieve the command and actual position.
axis = 1
posCmd = CmStatus.GetAxesStatus(axis).posCmd
actualPos = CmStatus.GetAxesStatus(axis).actualPos

print("Axis 1 - Pos Cmd:", posCmd, "Actual Pos:", actualPos)

# Determine the target based on whether the command and actual positions are the same.
if posCmd == actualPos:
    target = 201
else:
    target = -201

print("Moving Axis 1 to target:", target)

# Create and configure a motion command for Axis 1 (absolute position move).
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = target
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the absolute position command for Axis 1.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 1 completes its move.
Wmx3Lib_cm.motion.Wait(1)
