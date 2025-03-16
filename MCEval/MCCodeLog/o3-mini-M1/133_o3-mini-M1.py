
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def move_axis_3():
    # Create a command to move Axis 3 to position 310 with the specified ParabolicVelocity profile parameters.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.ParabolicVelocity
    posCommand.axis = 3
    posCommand.target = 310
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the absolute position command for Axis 3.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 3 stops moving.
    Wmx3Lib_cm.motion.Wait(3)

if __name__ == "__main__":
    move_axis_3()
