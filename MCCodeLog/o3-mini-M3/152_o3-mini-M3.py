
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 1 sequentially to the positions:
# 10, -10, 100, -100, and 0.
# Each move is executed with a TimeAccSCurve profile using:
#   velocity = 1000
#   accTimeMilliseconds = 50
#   decTimeMilliseconds = 50
#   startingVelocity = 0
#   endVelocity = 0
# The script waits for the axis to stop after each motion.

def move_axis(target):
    # Create a position command for the motion.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccSCurve
    posCommand.axis = 1
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute the absolute position move command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return False

    # Wait until Axis 1 reaches the target position and stops.
    Wmx3Lib_cm.motion.Wait(1)
    return True

def main():
    # List of target positions (interpreting "1o0" as 100 and "-1p0" as -100)
    targets = [10, -10, 100, -100, 0]
    for pos in targets:
        print("Moving Axis 1 to position:", pos)
        if not move_axis(pos):
            print("Motion failed at target position:", pos)
            break

if __name__ == '__main__':
    main()
