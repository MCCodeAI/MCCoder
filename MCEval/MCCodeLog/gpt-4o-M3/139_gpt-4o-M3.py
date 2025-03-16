
# Axes = [30]
# Inputs = []
# Outputs = []

# Define a function to move Axis 30 to specified positions using a T-MAT profile
def move_axis_30():
    positions = [-310, 100, -40, 0]
    velocity = 10020
    acceleration = 10000
    deceleration = 10000
    moving_average_time = 50

    for position in positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.TrapezoidalMAT
        posCommand.axis = 30
        posCommand.target = position
        posCommand.profile.velocity = velocity
        posCommand.profile.acc = acceleration
        posCommand.profile.dec = deceleration
        posCommand.profile.movingAverageTimeMilliseconds = moving_average_time
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = 0

        # Execute command to move from current position to specified absolute position.
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis moves to the target position and stops.
        Wmx3Lib_cm.motion.Wait(30)

# Call the function to execute the movement
move_axis_30()
