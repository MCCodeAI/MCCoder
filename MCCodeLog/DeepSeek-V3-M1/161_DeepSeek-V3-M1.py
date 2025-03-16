
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to position 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 stops moving
Wmx3Lib_cm.motion.Wait(4)

# Get the Axis status for Axis 4
axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(4)
actualPos = axisStatus.actualPos

# Check the actual position and move accordingly
if actualPos == 200:
    posCommand.target = 50
else:
    posCommand.target = -50

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 stops moving
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 6 to position 111 at a speed of 1000 using a TwoVelocityJerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 6
posCommand.target = 111
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 stops moving
Wmx3Lib_cm.motion.Wait(6)
