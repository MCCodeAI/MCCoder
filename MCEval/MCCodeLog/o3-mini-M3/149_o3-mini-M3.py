
# Axes = [1, 2, 3, 4]
# IOInputs = []
# IOOutputs = []

def move_axis():
    # Move Axis 1 to position 101 using TimeAccJerkRatio profile with speed 1000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccJerkRatio
    posCommand.axis = 1
    posCommand.target = 101
    posCommand.profile.velocity = 1000
    # These profile parameters are chosen according to the reference example for TimeAccJerkRatio.
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 50
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 1 StartPos error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 1 has stopped moving.
    Wmx3Lib_cm.motion.Wait(1)

    # Move Axis 2 to position 202 using JerkRatio profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatio
    posCommand.axis = 2
    posCommand.target = 202
    posCommand.profile.velocity = 1000
    # Set additional profile parameters for the JerkRatio profile.
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 2 StartPos error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 2 has stopped moving.
    Wmx3Lib_cm.motion.Wait(2)

    # Move Axis 3 to position 303 using TrapezoidalMAT profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TrapezoidalMAT
    posCommand.axis = 3
    posCommand.target = 303
    posCommand.profile.velocity = 1000
    # Use typical acceleration and deceleration values.
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    # Set the moving average time to smooth acceleration.
    posCommand.profile.movingAverageTimeMilliseconds = 50
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 3 StartPos error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 3 has stopped moving.
    Wmx3Lib_cm.motion.Wait(3)

    # Move Axis 4 to position 404 using ParabolicVelocity profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.ParabolicVelocity
    posCommand.axis = 4
    posCommand.target = 404
    posCommand.profile.velocity = 1000
    # Set time-based acceleration parameters for a parabolic velocity curve.
    posCommand.profile.accTimeMilliseconds = 50
    posCommand.profile.decTimeMilliseconds = 150
    posCommand.profile.jerkAccRatio = 0.5
    posCommand.profile.jerkDecRatio = 0.5
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 4 StartPos error: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 4 has stopped moving.
    Wmx3Lib_cm.motion.Wait(4)

if __name__ == '__main__':
    move_axis()
