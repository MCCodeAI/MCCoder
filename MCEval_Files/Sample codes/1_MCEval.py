# Write python code to move Axis 0 to 180 with velocity 1000.
# Write python code to start an absolute position command of Axis 0 to position 180 with 1000 velocity.

    # Axes = [0]
    # Start an absolute position command of Axis 0 to position 180 with 1000 velocity.
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

