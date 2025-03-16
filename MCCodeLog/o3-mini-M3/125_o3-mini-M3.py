
# Axes = [0]
# IOInputs = []
# IOOutputs = []

def move_axis0_to_10():
    # Create a position command for Axis 0
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimited
    posCommand.axis = 0
    posCommand.target = 10
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis stops moving.
    Wmx3Lib_cm.motion.Wait(0)

# Call the function to perform the motion.
move_axis0_to_10()
