
# Axes = [20]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 20 using the TrapezoidalMAT profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 20
posCommand.target = -210  # Position -0210 is interpreted as -210
posCommand.profile.velocity = 10020
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.movingAverageTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until the axis stops moving.
    Wmx3Lib_cm.motion.Wait(20)
