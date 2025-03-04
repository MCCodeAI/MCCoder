# Write python code to Start the motion for a path interpolation with look ahead channel 0 for Axis 0 and 1, with velocity 500, the 1st to 4th points are (100, 0) with smoothRadius as 12.5, (100, 100) with smoothRadius as 25,(0, 100) with smoothRadius as 50, and(0, 0).
    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

    sleep(0.1)

    # Allocate buffer memory for a path interpolation with look ahead channel with 1,000 points for Channel 0.
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
    if ret != 0:
        print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Set the configuration for the path interpolation with lookahead channel, specifying Axis 0 and Axis 1, with composite velocity of 1,000, composite acceleration of 20,000, and sample distance of 100.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 0)
    conf.SetAxis(1, 1)
    conf.compositeVel = 500
    conf.compositeAcc = 10000
    conf.sampleDistance = 100
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add interpolation commands to the path interpolation with look ahead channel, with the main body being a square trajectory formed by four points, with a side length of 100. There are smooth radius of 12.5, 25, and 50 at the end of the first, second, and third segments, respectively.
    path = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = 4

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 0)
    point.linear.smoothRadius = 12.5
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 25
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 50
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Start the motion for the path interpolation with look ahead channel.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Free buffer memory for a path interpolation with lookahead channel. 
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return


