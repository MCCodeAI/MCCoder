
# Axes = [1, 12]
# IOInputs = []
# IOOutputs = []

# Move Axis 12 to position 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 500  # Assuming a default velocity
posCommand.profile.acc = 5000  # Assuming a default acceleration
posCommand.profile.dec = 5000  # Assuming a default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(12)

# Get the status of Actual Torque and pos cmd
actualTorque = Wmx3Lib_cm.motion.GetActualTorque(12)
posCmd = Wmx3Lib_cm.motion.GetPosCmd(12)

# Compare Actual Torque and pos cmd
if actualTorque == posCmd:
    # Move Axis 1 to position 201
    posCommand.axis = 1
    posCommand.target = 201
else:
    # Move Axis 1 to position -201
    posCommand.axis = 1
    posCommand.target = -201

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(1)
