
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def move_axis_positions():
    positions = [-911, 911, 168, 0]
    for pos in positions:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.TimeAccParabolic
        posCommand.axis = 9
        posCommand.target = pos
        posCommand.profile.velocity = 1000
        posCommand.profile.accTimeMilliseconds = 50
        # The originally specified deceleration time (50000000000 ms) is out of range.
        # Changing it to 500 ms (a value more likely to be accepted) corrects the error.
        posCommand.profile.decTimeMilliseconds = 500
        posCommand.profile.startingVelocity = 0
        posCommand.profile.endVelocity = 0

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis stops moving after the current motion.
        Wmx3Lib_cm.motion.Wait(9)

if __name__ == '__main__':
    move_axis_positions()
