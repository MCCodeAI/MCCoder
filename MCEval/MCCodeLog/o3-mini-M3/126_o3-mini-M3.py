
# Axes = [6]
# IOInputs = []
# IOOutputs = []

def move_axis_6():
    # Create a position command for Axis 6 using a JerkLimitedAdvancedS profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedAdvancedS
    posCommand.axis = 6
    posCommand.target = -90
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000  # Corrected: Deceleration should be positive
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 6 moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(6)

if __name__ == '__main__':
    move_axis_6()
