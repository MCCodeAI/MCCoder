# Write python code to Execute path interpolation with look ahead of Axis 2 and Axis 1 with velocity 1000, with a sample distance 50, and with the velocityLimit of axis 1 set to 500, consisting of four circular interpolations defined as (throughPos0,throughPos1,endPos0,endPos1): (50,50,100,0),(50,-50,0,0),(-50,50,-100,0),(-50,-50,0,0).
# Axes = [2, 1]

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
    conf.SetAxis(0, 2)
    conf.SetAxis(1, 1)
    conf.compositeVel = 1000
    conf.compositeAcc = 4000
    conf.sampleDistance = 50
    conf.stopOnEmptyBuffer = True
    conf.SetVelocityLimit(1, 500)

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    point = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = 4

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEndCircular
    point.throughAndEndCircular.SetAxis(0, 2)
    point.throughAndEndCircular.SetAxis(1, 1)
    point.throughAndEndCircular.SetThroughPos(0, 50)
    point.throughAndEndCircular.SetThroughPos(1, 50)
    point.throughAndEndCircular.SetEndPos(0, 100)
    point.throughAndEndCircular.SetEndPos(1, 0)
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEndCircular
    point.throughAndEndCircular.SetAxis(0, 2)
    point.throughAndEndCircular.SetAxis(1, 1)
    point.throughAndEndCircular.SetThroughPos(0, 50)
    point.throughAndEndCircular.SetThroughPos(1, -50)
    point.throughAndEndCircular.SetEndPos(0, 0)
    point.throughAndEndCircular.SetEndPos(1, 0)
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEndCircular
    point.throughAndEndCircular.SetAxis(0, 2)
    point.throughAndEndCircular.SetAxis(1, 1)
    point.throughAndEndCircular.SetThroughPos(0, -50)
    point.throughAndEndCircular.SetThroughPos(1, 50)
    point.throughAndEndCircular.SetEndPos(0, -100)
    point.throughAndEndCircular.SetEndPos(1, 0)
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEndCircular
    point.throughAndEndCircular.SetAxis(0, 2)
    point.throughAndEndCircular.SetAxis(1, 1)
    point.throughAndEndCircular.SetThroughPos(0, -50)
    point.throughAndEndCircular.SetThroughPos(1, -50)
    point.throughAndEndCircular.SetEndPos(0, 0)
    point.throughAndEndCircular.SetEndPos(1, 0)
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
    Wmx3Lib_cm.motion.Wait(2)
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
