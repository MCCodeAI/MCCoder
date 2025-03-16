
# Axes = [12, 1]
# IOInputs = []
# IOOutputs = []

# Move Axis 12 to 101
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = 101
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000      # Assuming default acceleration
posCommand.profile.dec = 10000      # Assuming default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 12 to finish moving
Wmx3Lib_cm.motion.Wait(12)

# Get the status of Actual Torque and Pos Cmd for Axis 12
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

actualTorque = CmStatus.GetAxesStatus(12).actualTorque
posCmd = CmStatus.GetAxesStatus(12).posCmd

# Move Axis 1 based on the comparison
if actualTorque == posCmd:
    target = 201
else:
    target = -201

# Create command for Axis 1
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = target
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000      # Assuming default acceleration
posCommand.profile.dec = 10000      # Assuming default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 1 to finish moving
Wmx3Lib_cm.motion.Wait(1)
