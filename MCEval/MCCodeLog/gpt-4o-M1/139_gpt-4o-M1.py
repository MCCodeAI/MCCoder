
# Axes = [30]
# IOInputs = []
# IOOutputs = []

# Move Axis 30 to multiple positions using a TrapezoidalMAT profile with specified parameters.
positions = [-310, 100, -40, 0]
velocity = 10020
acceleration = 10000
deceleration = 10000
moving_average_time_ms = 50

for position in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT
    posCommand.axis = 30
    posCommand.target = position
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = acceleration
    posCommand.profile.dec = deceleration
    posCommand.profile.movingAverageTimeMilliseconds = moving_average_time_ms
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(30)
