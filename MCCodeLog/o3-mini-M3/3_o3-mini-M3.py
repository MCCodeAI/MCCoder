
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create an instance of the position command
posCommand = Motion_PosCommand()
# Set the profile type to TrapezoidalMAT (trapezoidal with moving average filter)
posCommand.profile.type = ProfileType.TrapezoidalMAT
# Specify the axis number
posCommand.axis = 3
# Set the target position and velocity
posCommand.target = 88.8
posCommand.profile.velocity = 1200
# Set typical acceleration and deceleration values
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
# Set the moving average time to 50ms
posCommand.profile.movingAverageTimeMilliseconds = 50
# Set starting and end velocities to 0 (default)
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to move Axis 3 to the target position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 3 stops moving after the motion is completed.
    Wmx3Lib_cm.motion.Wait(3)
