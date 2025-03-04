# Write python code to Execute path interpolation with look ahead of Axis 8, 1 and 2 with velocity 1000, and Axis 3 as the auxiliary axis, consisting of two circular interpolations defined as (throughPos0,throughPos1,throughPos2,endPos0,endPos1,endPos2,auxiliaryTarget): (70.71,29.29,0,100,100,0,50),(29.29,70.71,0,0,0,0,100).
# Axes = [8, 1, 2, 3]

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

    conf.axisCount = 4
    conf.SetAxis(0, 8)
    conf.SetAxis(1, 1)
    conf.SetAxis(2, 2)
    conf.SetAxis(3, 3)
    conf.compositeVel = 1000
    conf.compositeAcc = 4000
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    path.numPoints = 2

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEnd3DCircular
    point.throughAndEnd3DCircular.axisCount = 3
    point.throughAndEnd3DCircular.SetAxis(0, 8)
    point.throughAndEnd3DCircular.SetAxis(1, 1)
    point.throughAndEnd3DCircular.SetAxis(2, 2)
    point.throughAndEnd3DCircular.SetThroughPos(0, 70.71)
    point.throughAndEnd3DCircular.SetThroughPos(1, 29.29)
    point.throughAndEnd3DCircular.SetThroughPos(2, 0)
    point.throughAndEnd3DCircular.SetEndPos(0, 100)
    point.throughAndEnd3DCircular.SetEndPos(1, 100)
    point.throughAndEnd3DCircular.SetEndPos(2, 0)
    point.throughAndEnd3DCircular.auxiliaryAxisCount = 1
    point.throughAndEnd3DCircular.SetAuxiliaryAxis(0, 3)
    point.throughAndEnd3DCircular.SetAuxiliaryTarget(0, 50)
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEnd3DCircular
    point.throughAndEnd3DCircular.axisCount = 3
    point.throughAndEnd3DCircular.SetAxis(0, 8)
    point.throughAndEnd3DCircular.SetAxis(1, 1)
    point.throughAndEnd3DCircular.SetAxis(2, 2)
    point.throughAndEnd3DCircular.SetThroughPos(0, 29.29)
    point.throughAndEnd3DCircular.SetThroughPos(1, 70.71)
    point.throughAndEnd3DCircular.SetThroughPos(2, 0)
    point.throughAndEnd3DCircular.SetEndPos(0, 0)
    point.throughAndEnd3DCircular.SetEndPos(1, 0)
    point.throughAndEnd3DCircular.SetEndPos(2, 0)
    point.throughAndEnd3DCircular.auxiliaryAxisCount = 1
    point.throughAndEnd3DCircular.SetAuxiliaryAxis(0, 3)
    point.throughAndEnd3DCircular.SetAuxiliaryTarget(0, 100)
    path.SetPoint(1, point)

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
    Wmx3Lib_cm.motion.Wait(8)
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
