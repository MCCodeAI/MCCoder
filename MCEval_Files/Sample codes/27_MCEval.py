# Write python code to Execute a sequence of moving position command with blocking wait command.The moving distance of Axis 0 is 100, -100 and 100 with blocking wait.
    # Axes = [0]

    pos = Motion_PosCommand()

    # Set position command parameters
    pos.axis = 0
    pos.profile.type = ProfileType.Trapezoidal
    pos.profile.velocity = 1000
    pos.profile.acc = 10000
    pos.profile.dec = 10000

    # Execute motion to move axis forward 100
    pos.target = 100

    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finishedmoving 
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute motion to move axis backward 100
    pos.target = -100
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute motion to move axis forward 100
    pos.target = 100
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    