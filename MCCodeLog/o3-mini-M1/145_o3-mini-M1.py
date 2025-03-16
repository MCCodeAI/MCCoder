
# Axes = [8]
# IOInputs = []
# IOOutputs = []

def main():
    # Create the position command for the motion.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccTrapezoidal
    posCommand.axis = 8
    posCommand.target = -99
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = -50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move Axis 8 from its current position to the target (-99).
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving.
    Wmx3Lib_cm.motion.Wait(8)

if __name__ == "__main__":
    main()
