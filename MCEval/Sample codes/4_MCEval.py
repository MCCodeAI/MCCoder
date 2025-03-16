# Write python code to move Axis 0 to position 180 with 1000 velocity, and then move Axis 0 by a 200 distance and 2000 velocity.
# Write python code to Start an absolute position command of Axis 0 to position 180 with 1000 velocity, and then start a relative position command of Axis 0 by a 200 distance and 2000 velocity.


    # Axes = [0]
    # Create a command value of target as 180.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    # Create a command value of target as 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 200
    posCommand.profile.velocity = 2000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to a specified distance relatively. e.g. 'Move 100..'
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret!=0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)
