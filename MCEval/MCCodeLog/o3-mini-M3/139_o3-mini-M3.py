
# Axes = [30]
# IOInputs = []
# IOOutputs = []

# List of target positions for Axis 30.
# The motion sequence is: -310, 100, -40, and 0.
targets = [-310, 100, -40, 0]

for target in targets:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT
    posCommand.axis = 30
    posCommand.target = target
    posCommand.profile.velocity = 10020
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.movingAverageTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the absolute position command for Axis 30.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 30 stops moving.
    Wmx3Lib_cm.motion.Wait(30)
