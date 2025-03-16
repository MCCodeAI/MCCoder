
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

from time import sleep

def main():
    # Instantiate the AdvancedMotion class using the library object (assumed to be available as Wmx3Lib)
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free any existing path interpolation with look-ahead buffer on channel 10
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(0.1)

    # Allocate buffer memory for a path interpolation with look-ahead channel 10, reserving capacity for 1000 points.
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
    if ret != 0:
        print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with look-ahead channel 10 for Axis 0 and Axis 1.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 0)
    conf.SetAxis(1, 1)
    conf.compositeVel = 1500
    # Set a default composite acceleration and sample distance (values chosen as example)
    conf.compositeAcc = 10000  
    conf.sampleDistance = 100  
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
    if ret != 0:
        print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Create a path command with 4 points
    path = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = 4

    # Define the 1st point: (50, 0) with a smooth radius of 2.5
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 50)
    point.linear.SetTarget(1, 0)
    point.linear.smoothRadius = 2.5
    path.SetPoint(0, point)

    # Define the 2nd point: (50, 50) with a smooth radius of 5
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 50)
    point.linear.SetTarget(1, 50)
    point.linear.smoothRadius = 5
    path.SetPoint(1, point)

    # Define the 3rd point: (0, 50) with a smooth radius of 10
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 50)
    point.linear.smoothRadius = 10
    path.SetPoint(2, point)

    # Define the 4th point: (0, 0) with no smooth radius (assumed default value 0)
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 0)
    point.linear.SetAxis(1, 1)
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    # Either leave smoothRadius unchanged or explicitly set to 0.
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
    if ret != 0:
        print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Start the motion for the path interpolation with look-ahead on channel 10.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
    if ret != 0:
        print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the motion to complete for Axis 0 and Axis 1.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Free the path interpolation with look-ahead buffer for channel 10.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
    if ret != 0:
        print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
