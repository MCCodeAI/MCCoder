
# Axes = [1, 2, 3, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 1 to position 101 at a speed of 1000 using TimeAccJerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.decTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.jerkAccRatio = 0.5  # Example value, adjust as needed
posCommand.profile.jerkDecRatio = 0.5  # Example value, adjust as needed
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 1 stops moving
Wmx3Lib_cm.motion.Wait(1)

# Move Axis 2 to position 202 using JerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 2
posCommand.target = 202
posCommand.profile.velocity = 1000  # Example value, adjust as needed
posCommand.profile.acc = 10000  # Example value, adjust as needed
posCommand.profile.dec = 10000  # Example value, adjust as needed
posCommand.profile.jerkAccRatio = 0.5  # Example value, adjust as needed
posCommand.profile.jerkDecRatio = 0.5  # Example value, adjust as needed
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 2 stops moving
Wmx3Lib_cm.motion.Wait(2)

# Move Axis 3 to position 303 using TrapezoidalMAT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 3
posCommand.target = 303
posCommand.profile.velocity = 1000  # Example value, adjust as needed
posCommand.profile.acc = 10000  # Example value, adjust as needed
posCommand.profile.dec = 10000  # Example value, adjust as needed

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 3 stops moving
Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 to position 404 using ParabolicVelocity profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.axis = 4
posCommand.target = 404
posCommand.profile.velocity = 1000  # Example value, adjust as needed
posCommand.profile.accTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.decTimeMilliseconds = 150  # Example value, adjust as needed
posCommand.profile.jerkAccRatio = 0.5  # Example value, adjust as needed
posCommand.profile.jerkDecRatio = 1.5  # Example value, adjust as needed
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 stops moving
Wmx3Lib_cm.motion.Wait(4)
