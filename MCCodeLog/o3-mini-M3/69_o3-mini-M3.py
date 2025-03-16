
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # Create the advanced motion object for look‐ahead path interpolation.
    advMotion = AdvancedMotion(Wmx3Lib)
    
    # Free any previous look‐ahead buffer and create a new one.
    ret = advMotion.advMotion.FreePathIntplLookaheadBuffer(0)
    ret = advMotion.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)  # Buffer size in bytes (example value)
    if ret != 0:
        print('CreatePathIntplLookaheadBuffer error code:', ret)
        return

    # Configure the path interpolation with look ahead.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 9)
    conf.SetAxis(1, 6)
    conf.compositeVel = 2000
    conf.compositeAcc = 2000  # Using an example acceleration value.
    conf.sampleDistance = 50
    conf.stopOnEmptyBuffer = True

    ret = advMotion.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code:', ret)
        return

    # Define the sequence of interpolation points.
    # Each tuple represents (target for Axis 9, target for Axis 6).
    points = [(200, 0), (200, 200), (0, 200), (0, 0), (200, 200)]
    
    # Create a look-ahead command containing the interpolation segments.
    path_cmd = AdvMotion_PathIntplLookaheadCommand()
    path_cmd.numPoints = len(points)
    
    # Populate the command with linear interpolation segments.
    for i, pt in enumerate(points):
        point = AdvMotion_PathIntplLookaheadCommandPoint()
        point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
        point.linear.axisCount = 2
        # Map the first coordinate to Axis 9 and the second to Axis 6.
        point.linear.SetAxis(0, 9)
        point.linear.SetAxis(1, 6)
        point.linear.SetTarget(0, pt[0])
        point.linear.SetTarget(1, pt[1])
        path_cmd.SetPoint(i, point)
    
    # Add the populated look-ahead command to the buffer.
    ret = advMotion.advMotion.AddPathIntplLookaheadCommand(0, path_cmd)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code:', ret)
        return

    # Start the path interpolation with look-ahead.
    ret = advMotion.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print('StartPathIntplLookahead error code:', ret)
        return

    # Wait for the overall look-ahead interpolation to complete.
    timeoutCounter = 0
    ret, pathStatus = advMotion.advMotion.GetPathIntplLookaheadStatus(0)
    while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
        time.sleep(0.1)
        timeoutCounter += 1
        if timeoutCounter > 500:
            print('Path interpolation look-ahead timeout!')
            return
        ret, pathStatus = advMotion.advMotion.GetPathIntplLookaheadStatus(0)

    # After the continuous interpolation motion finishes,
    # wait for axes to actually stop moving.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 9)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code:', ret)
        return

    # Free the look-ahead buffer resources.
    ret = advMotion.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code:', ret)
        return

if __name__ == '__main__':
    main()
