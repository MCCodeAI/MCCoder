# Write python code to move Axis 1 by a 200 distance with velocity 2000.
# Write python code to Start a relative position command of Axis 1 by a 200 distance and 2000 velocity.
    # Axes = [1]

    # Start a relative position command of Axis 1 with 200 distance and 2000 velocity.
    # Create a command value of target as 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
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
    Wmx3Lib_cm.motion.Wait(1)
