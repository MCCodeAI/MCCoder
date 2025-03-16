
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def move_axis_9():
    # Create and configure the motion position command for Axis 9 using the JerkRatio profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatio
    posCommand.axis = 9
    posCommand.target = 90
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000      # using default acceleration as per context example
    posCommand.profile.dec = 10000      # using default deceleration as per context example
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the absolute position command for Axis 9.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 9 stops moving.
    Wmx3Lib_cm.motion.Wait(9)

if __name__ == "__main__":
    move_axis_9()
