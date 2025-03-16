
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Create the position command for Axis 9 using a TimeAccParabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccParabolic
posCommand.axis = 9
posCommand.target = -910
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 9 has reached the target position and stopped moving.
Wmx3Lib_cm.motion.Wait(9)
