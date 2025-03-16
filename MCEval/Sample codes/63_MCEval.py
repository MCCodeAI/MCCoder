# Write python code to Execute path interpolation with look ahead of Axis 7 and Axis 1 with velocity 1000, with a sample distance 100, consisting of eight sequences: linear interpolations to (100,0), linear interpolations to (100,100), linear interpolations to (60,100), set output 0.0 to 1, linear interpolations to (40,100),  set output 0.0 to 0, linear interpolations to (0,100), linear interpolations to (10,20), while the smoothRadius is 30.
# Axes = [7, 1]

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
    conf.SetAxis(0, 7)
    conf.SetAxis(1, 1)
    conf.compositeVel = 1000
    conf.compositeAcc = 2000
    #  The commanded axes will automatically change to Idle operation state after all interpolation commands in the path have been executed.
    conf.stopOnEmptyBuffer = True
    # Sample the profile at every specified distance along the path, improving the granularity of the generated profile.
    conf.sampleDistance = 100

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Add the path interpolation with look ahead commands
    path.numPoints = 8

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 0)
    point.linear.smoothRadius = 30
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 100)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 60)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
    point.setOutputBit.byteAddress = 0
    point.setOutputBit.bitAddress = 0
    point.setOutputBit.value = 1
    point.setOutputBit.type = AdvMotion_PathIntplOutputType.Immediate
    point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
    path.SetPoint(3, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 40)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    path.SetPoint(4, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.SetOutputBit
    point.setOutputBit.byteAddress = 0
    point.setOutputBit.bitAddress = 0
    point.setOutputBit.value = 0
    point.setOutputBit.type = AdvMotion_PathIntplOutputType.Immediate
    point.setOutputBit.source = AdvMotion_PathIntplOutputSource.IOOutput
    path.SetPoint(5, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 100)
    point.linear.smoothRadius = 30
    path.SetPoint(6, point)

    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 10)
    point.linear.SetTarget(1, 20)
    path.SetPoint(7, point)

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
