# Write python code to Execute path interpolation with look ahead of Axis 3 and Axis 1 with velocity 1000, with a sample distance 10, consisting of four linear interpolations: (100,0) with velocity 900,(100,100) with velocity 700,(0,100) with velocity 500,(0,0) with velocity 300, while the smoothRadius is 30.
# Axes = [3, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplLookaheadCommand()
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    # Create the path interpolation with look ahead buffer
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
    if ret != 0:
        print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with look ahead channel
    conf = AdvMotion_PathIntplLookaheadConfiguration()

    conf.axisCount = 2
    conf.SetAxis(0, 3)
    conf.SetAxis(1, 1)
    conf.compositeVel = 1000
    conf.compositeAcc = 2000
    #  The commanded axes will automatically change to Idle operation state after all interpolation commands in the path have been executed.
    conf.stopOnEmptyBuffer = True
    # Sample the profile at every specified distance along the path, improving the granularity of the generated profile.
    conf.sampleDistance = 10

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    path.numPoints = 4

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 0)
    point.linear.smoothRadius = 30
    point.linear.setSegmentCompositeVel = 1
    point.linear.segmentCompositeVel = 900
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    point.linear.setSegmentCompositeVel = 1
    point.linear.segmentCompositeVel = 700
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    point.linear.setSegmentCompositeVel = 1
    point.linear.segmentCompositeVel = 500
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 3)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    point.linear.setSegmentCompositeVel = 1
    point.linear.segmentCompositeVel = 300
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Execute path interpolation with look ahead
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the path interpolation with look ahead to complete
    Wmx3Lib_cm.motion.Wait(3)
    timeoutCounter = 0
    # Wait until the path interpolation with look ahead is in Stopped state
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
    while True:
        if (pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped):
            break
        sleep(0.1)
        timeoutCounter = timeoutCounter + 1
        if (timeoutCounter > 500):
            break
        ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
    if (timeoutCounter > 500):
        print('PathIntplLookahead Runuing timeout.!')
        return
    # Free the path interpolation with look ahead buffer (normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
