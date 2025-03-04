# Write python code to Execute path interpolation with look ahead of Axis 5 and Axis 1 with velocity 1000, consisting of four linear interpolations: (100,0),(100,100),(0,100),(0,0). First start executing it for 0.5s, then stop and sleep for 1s, and then resume it.
# Axes = [5, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplLookaheadCommand()
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(5)
    # Create the path interpolation with look ahead buffer
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(5, 1000)
    if ret != 0:
        print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with look ahead channel
    conf = AdvMotion_PathIntplLookaheadConfiguration()

    conf.axisCount = 2
    conf.SetAxis(0, 5)
    conf.SetAxis(1, 1)
    conf.compositeVel = 1000
    conf.compositeAcc = 2000
    #  The commanded axes will automatically change to Idle operation state after all interpolation commands in the path have been executed.
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(5, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    path.numPoints = 4

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 5)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 0)
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 5)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 100)
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 5)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 100)
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 5)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(5, path)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Execute path interpolation with look ahead
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(5)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(0.5)
    # Stop path interpolation with look ahead
    ret = Wmx3Lib_adv.advMotion.StopPathIntplLookahead(5)
    if ret != 0:
        print('StopPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
    
    sleep(1)
    # Execute path interpolation with look ahead (Resume execution)
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(5)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the path interpolation with look ahead to complete
    Wmx3Lib_cm.motion.Wait(5)
    timeoutCounter = 0
    # Wait until the path interpolation with look ahead is in Stopped state
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(5)
    while True:
        if (pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped):
            break
        sleep(0.1)
        timeoutCounter = timeoutCounter + 1
        if (timeoutCounter > 500):
            break
        ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(5)
    if (timeoutCounter > 500):
        print('PathIntplLookahead Running timeout.!')
        return
    
    # Free the path interpolation with look ahead buffer (normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(5)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
