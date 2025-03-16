# Write python code to Execute path interpolation with look ahead of Axis 7, 1 and 2 with velocity 100, composite acceleration 1000, and the acceleration limit for Axis 7, 1 and 2 is 300, 600 and 900, with a sample distance 100, consisting of three linear interpolations: (40,60,70),(30,20,120),(0,0,0), while the smoothRadius is 5.
# Axes = [7, 1, 2]

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

    conf.axisCount = 3
    conf.SetAxis(0, 7)
    conf.SetAxis(1, 1)
    conf.SetAxis(2, 2)
    conf.compositeVel = 100
    conf.compositeAcc = 1000
    conf.sampleDistance = 100
    conf.stopOnEmptyBuffer = True
    conf.SetAccLimit(0, 300)
    conf.SetAccLimit(1, 600)
    conf.SetAccLimit(2, 900)

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    path.numPoints = 3

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 3
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetAxis(2, 2)
    point.linear.SetTarget(0, 40)
    point.linear.SetTarget(1, 60)
    point.linear.SetTarget(2, 70)
    point.linear.smoothRadius = 5
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 3
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetAxis(2, 2)
    point.linear.SetTarget(0, 30)
    point.linear.SetTarget(1, 20)
    point.linear.SetTarget(2, 120)
    point.linear.smoothRadius = 5
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 3
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetAxis(2, 2)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    point.linear.SetTarget(2, 0)
    path.SetPoint(2, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Start path interpolation with look ahead
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the path interpolation with look ahead to complete
    Wmx3Lib_cm.motion.Wait(7)
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
        print('PathIntplLookahead Running timeout.!')
        return
    # Free the path interpolation with look ahead buffer (normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
