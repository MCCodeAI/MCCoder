
# Axes = [6]
# IOInputs = []
# IOOutputs = []

def move_axis_6():
    # Create a new position command instance
    posCommand = Motion_PosCommand()
    
    # Set the profile type to JerkLimitedAdvancedS as specified
    posCommand.profile.type = ProfileType.JerkLimitedAdvancedS
    
    # Set the axis number and target position
    posCommand.axis = 6
    posCommand.target = -90
    
    # Set the motion parameters according to the question
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = -10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(6)

if __name__ == "__main__":
    move_axis_6()
