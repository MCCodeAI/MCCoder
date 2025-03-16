
# Axes = [3]
# IOInputs = []
# IOOutputs = []

def move_axis_3():
    # Create a position command for Axis 3
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT
    posCommand.axis = 3
    posCommand.target = 88.8
    posCommand.profile.velocity = 1200
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.movingAverageTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move Axis 3 to the target position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 3 completes its motion before ending the function
    Wmx3Lib_cm.motion.Wait(3)

if __name__ == "__main__":
    move_axis_3()
