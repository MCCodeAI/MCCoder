
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create an instance of the Motion_PosCommand for the move command.
posCommand = Motion_PosCommand()
# Set the profile type to JerkLimited.
posCommand.profile.type = ProfileType.JerkLimited
# Specify the axis to be moved.
posCommand.axis = 0
# Set the target position, speed, acceleration, deceleration, jerk acceleration, jerk deceleration,
# starting velocity, and end velocity.
posCommand.target = -200
# For an absolute move to a negative position the velocity argument should be given as a positive value.
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position move command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 0 stops moving.
    Wmx3Lib_cm.motion.Wait(0)
