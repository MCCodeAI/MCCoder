
# Axes = [3]
# Inputs = []
# Outputs = []

# Define a function to move Axis 3 to specified positions using an Advanced-S profile
def move_axis_3():
    positions = [-20, 30, -40, 0]
    for target_position in positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.AdvancedS
        posCommand.axis = 3
        posCommand.target = target_position
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000
        posCommand.profile.jerkAccRatio = 0.5
        posCommand.profile.jerkDecRatio = 0.5
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = 0

        # Execute command to move from current position to specified absolute position.
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis moves to the target position and stops.
        Wmx3Lib_cm.motion.Wait(3)

# Call the function to execute the movement
move_axis_3()
