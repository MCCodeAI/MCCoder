
# Axes = [1, 12]
# IOInputs = []
# IOOutputs = []

# Move Axis 12 to position 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 500
posCommand.profile.acc = 5000
posCommand.profile.dec = 5000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 12 stops moving
Wmx3Lib_cm.motion.Wait(12)

# Get the status of Actual Torque and Position Command
actualTorque = Wmx3Lib_cm.motion.GetActualTorque(12)
posCmd = Wmx3Lib_cm.motion.GetPosCommand(12)

# Check if Actual Torque and Position Command are the same
if actualTorque == posCmd:
    # Move Axis 1 to position 201
    posCommand.axis = 1
    posCommand.target = 201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move Axis 1 to position -201
    posCommand.axis = 1
    posCommand.target = -201
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

# Wait until Axis 1 stops moving
Wmx3Lib_cm.motion.Wait(1)
