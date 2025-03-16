
# Axes = [3, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to position 33 at a speed of 1000 using a TwoVelocitySCurve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 3
posCommand.target = 33
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 500  # Example second velocity, adjust as needed

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 3 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 to position 77 at a speed of 1000 using a TwoVelocitySCurve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 4
posCommand.target = 77
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 500  # Example second velocity, adjust as needed

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
