
# Axes = [7]
# IOInputs = []
# IOOutputs = []

def move_axis_7():
    # Create and configure the absolute position command for Axis 7
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
    posCommand.axis = 7
    posCommand.target = -99
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000      # Default acceleration value
    posCommand.profile.dec = 10000      # Default deceleration value
    posCommand.profile.jerkAccRatio = 0.5 # Example acceleration jerk ratio (value between 0 and 1)
    posCommand.profile.jerkDecRatio = 0.5 # Example deceleration jerk ratio (value between 0 and 1)
    posCommand.profile.startingVelocity = 0
    posCommand.profile.secondVelocity = 5000  # A second velocity greater than the starting velocity
    posCommand.profile.endVelocity = 0

    # Execute the absolute position command for Axis 7
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code: ' + str(ret) + ' - ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 7 stops moving
    Wmx3Lib_cm.motion.Wait(7)

# Call the function to move Axis 7
move_axis_7()
