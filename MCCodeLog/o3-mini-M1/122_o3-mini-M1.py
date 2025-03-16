
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Create a motion position command for moving Axis 1 using Tixing profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Tixing
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 10
posCommand.profile.endVelocity = 0

# Execute the absolute position command for Axis 1.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 1 finishes moving.
    Wmx3Lib_cm.motion.Wait(1)
