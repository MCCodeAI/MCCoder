
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def move_axis_3():
    # Create and configure the position command using a TimeAccAdvancedS profile
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccAdvancedS
    posCommand.axis = 3
    posCommand.target = 10
    posCommand.profile.velocity = 12000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from the current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is {}: {}".format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until Axis 3 stops moving after the commanded motion.
    Wmx3Lib_cm.motion.Wait(3)

if __name__ == "__main__":
    move_axis_3()
