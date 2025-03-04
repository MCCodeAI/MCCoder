# Write python code to Jog Axis 2 for 1.5s with 160 velocity, then start an absolute position command to position 10 with 1000 velocity.
# Jog Axis 2 for 1.5s with 160 velocity, then move to 10 with velocity 1000.
    # Axes = [2]

    jogCommand = Motion_JogCommand()
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.axis = 2
    jogCommand.profile.velocity = 160
    jogCommand.profile.acc = 10000
    jogCommand.profile.dec = 10000

    # Rotate the motor at the specified speed.
    ret =Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret!=0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Jogging for 1.5 seconds
    sleep(1.5)
    
    Wmx3Lib_cm.motion.Stop(2)

    Wmx3Lib_cm.motion.Wait(2)
    
    # Create a command value of target as 10.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 2
    posCommand.target = 10
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(2)

