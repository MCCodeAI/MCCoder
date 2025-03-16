
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to 300 using a trapezoidal profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code for Axis 4 (target 300) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 4 finishes its motion.
Wmx3Lib_cm.motion.Wait(4)

# Get the status of Axis 4.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code for Axis 4 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Retrieve the Actual Position of Axis 4.
actualPos = CmStatus.GetAxesStatus(4).actualPos
print('Axis 4 Actual Pos is: ' + str(actualPos))

# Based on the Actual Pos: if it is 200, move Axis 4 to 50; otherwise move to -50.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
if actualPos == 200:
    posCommand.target = 50
    print('Actual Pos is 200: Moving Axis 4 to 50.')
else:
    posCommand.target = -50
    print('Actual Pos is not 200: Moving Axis 4 to -50.')

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code for Axis 4 (conditional move) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 4 completes the conditional move.
Wmx3Lib_cm.motion.Wait(4)

# Now move Axis 6 to position 111 using a TwoVelocityJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 6
posCommand.target = 111
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5        # Ratio of acceleration-time where jerk is nonzero
posCommand.profile.jerkDecRatio = 0.5        # Ratio of deceleration-time where jerk is nonzero
posCommand.profile.startingVelocity = 0      # Starting velocity (must be less than secondVelocity)
posCommand.profile.secondVelocity = 1000     # Second target velocity (must be greater than startingVelocity)
posCommand.profile.endVelocity = 0           # Velocity at target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code for Axis 6 (TwoVelocityJerkRatio move) is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 6 completes its motion.
Wmx3Lib_cm.motion.Wait(6)
