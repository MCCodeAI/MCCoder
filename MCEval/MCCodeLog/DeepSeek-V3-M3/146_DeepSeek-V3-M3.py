
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to position 144 using an S-curve profile
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.SCurve
posCommand1.axis = 4
posCommand1.target = 144
posCommand1.profile.velocity = 1000
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000
posCommand1.profile.startingVelocity = 30
posCommand1.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 4 to position 0 using an S-curve profile
posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.SCurve
posCommand2.axis = 4
posCommand2.target = 0
posCommand2.profile.velocity = 1000
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000
posCommand2.profile.startingVelocity = 30
posCommand2.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand2)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
