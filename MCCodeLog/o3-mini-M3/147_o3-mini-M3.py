
# Axes = [22]
# IOInputs = []
# IOOutputs = []

def move_axis_22():
    # Create and configure a position command to move Axis 22.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
    posCommand.axis = 22
    posCommand.target = 120
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the position command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 22 stops moving.
    Wmx3Lib_cm.motion.Wait(22)

if __name__ == "__main__":
    move_axis_22()
