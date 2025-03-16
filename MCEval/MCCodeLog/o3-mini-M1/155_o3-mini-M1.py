
# Axes = [5]
# IOInputs = []
# IOOutputs = []

def move_axis_5():
    # Create position command using the JerkRatio profile for Axis 5.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatio
    posCommand.axis = 5
    posCommand.target = 50
    posCommand.profile.velocity = 1000
    # Use default acceleration and deceleration values as shown in the example.
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from the current position to the target position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 reaches the target position and stops.
    Wmx3Lib_cm.motion.Wait(5)

if __name__ == "__main__":
    move_axis_5()
