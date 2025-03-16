
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Create a relative position command for Axis 6 with a distance of 199.9 and a velocity of 2000,
# using the JerkRatio profile with a jerkAccRatio of 0.3.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.3
posCommand.profile.jerkDecRatio = 0.3
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to start a relative position move.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # In actual implementation, you might want to handle the error here.
    
# Wait until Axis 6 stops moving.
Wmx3Lib_cm.motion.Wait(6)
