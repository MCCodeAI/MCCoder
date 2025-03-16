
# Axes = [4, 6, 8, 9]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # Assume that Wmx3Lib, Wmx3Lib_cm, and the necessary motion API classes
    # (e.g., AdvancedMotion, AdvMotion_PathIntplLookaheadCommand,
    # AdvMotion_PathIntplLookaheadConfiguration, AdvMotion_PathIntplLookaheadCommandPoint,
    # AdvMotion_PathIntplLookaheadSegmentType, and AxisSelection)
    # are already defined and available in the environment.

    # Create an advanced motion object
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free any existing look ahead buffer on channel 0 and then create a new one with composite velocity 1000.
    path = AdvMotion_PathIntplLookaheadCommand()
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
    if ret != 0:
        print("CreatePathIntplLookaheadBuffer error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

    # Configure the look ahead channel:
    # Motion axes: 4, 6, 8 and auxiliary axis: 9.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 4
    conf.SetAxis(0, 4)
    conf.SetAxis(1, 6)
    conf.SetAxis(2, 8)
    conf.SetAxis(3, 9)
    conf.compositeVel = 1000
    conf.compositeAcc = 4000
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print("SetPathIntplLookaheadConfiguration error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

    # Define two segments for the path interpolation with look ahead
    path.numPoints = 2

    # -------------------------------------------------------------------------
    # Segment 1:
    # Circular interpolation defined by a THROUGH point.
    # Interpolate to end position (100, 100, 0) with a through point at (80, 30, 10)
    # and set the auxiliary target (on axis 9) to 50.
    point1 = AdvMotion_PathIntplLookaheadCommandPoint()
    point1.type = AdvMotion_PathIntplLookaheadSegmentType.ThroughAndEnd3DCircular
    point1.throughAndEnd3DCircular.axisCount = 3
    point1.throughAndEnd3DCircular.SetAxis(0, 4)
    point1.throughAndEnd3DCircular.SetAxis(1, 6)
    point1.throughAndEnd3DCircular.SetAxis(2, 8)
    # Set the THROUGH point along the arc
    point1.throughAndEnd3DCircular.SetThroughPos(0, 80)
    point1.throughAndEnd3DCircular.SetThroughPos(1, 30)
    point1.throughAndEnd3DCircular.SetThroughPos(2, 10)
    # Set the END point of the arc
    point1.throughAndEnd3DCircular.SetEndPos(0, 100)
    point1.throughAndEnd3DCircular.SetEndPos(1, 100)
    point1.throughAndEnd3DCircular.SetEndPos(2, 0)
    # Configure the auxiliary axis and target value
    point1.throughAndEnd3DCircular.auxiliaryAxisCount = 1
    point1.throughAndEnd3DCircular.SetAuxiliaryAxis(0, 9)
    point1.throughAndEnd3DCircular.SetAuxiliaryTarget(0, 50)
    path.SetPoint(0, point1)

    # -------------------------------------------------------------------------
    # Segment 2:
    # Circular interpolation defined by a CENTER point.
    # Interpolate to end position (0, 0, 0) with the circle defined by center (30, 80, 10)
    # and set the auxiliary target (on axis 9) to -50.
    # (Note: Here we assume the existence of a center-based circular type for look ahead commands.)
    point2 = AdvMotion_PathIntplLookaheadCommandPoint()
    point2.type = AdvMotion_PathIntplLookaheadSegmentType.CenterAndEnd3DCircular
    point2.centerAndEnd3DCircular.axisCount = 3
    point2.centerAndEnd3DCircular.SetAxis(0, 4)
    point2.centerAndEnd3DCircular.SetAxis(1, 6)
    point2.centerAndEnd3DCircular.SetAxis(2, 8)
    # Set the CENTER of the circle
    point2.centerAndEnd3DCircular.SetCenterPos(0, 30)
    point2.centerAndEnd3DCircular.SetCenterPos(1, 80)
    point2.centerAndEnd3DCircular.SetCenterPos(2, 10)
    # Set the END point of the arc
    point2.centerAndEnd3DCircular.SetEndPos(0, 0)
    point2.centerAndEnd3DCircular.SetEndPos(1, 0)
    point2.centerAndEnd3DCircular.SetEndPos(2, 0)
    # Configure the auxiliary axis and target value
    point2.centerAndEnd3DCircular.auxiliaryAxisCount = 1
    point2.centerAndEnd3DCircular.SetAuxiliaryAxis(0, 9)
    point2.centerAndEnd3DCircular.SetAuxiliaryTarget(0, -50)
    path.SetPoint(1, point2)

    # -------------------------------------------------------------------------
    # Add the configured path to the look ahead buffer
    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
    if ret != 0:
        print("AddPathIntplLookaheadCommand error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

    # Start the path interpolation with look ahead execution
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print("StartPathIntplLookahead error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

    # Wait for the motion on all axes (4, 6, 8, and auxiliary 9) to complete.
    axes = AxisSelection()
    axes.axisCount = 4
    axes.SetAxis(0, 4)
    axes.SetAxis(1, 6)
    axes.SetAxis(2, 8)
    axes.SetAxis(3, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

    # Free the look ahead buffer (typically freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print("FreePathIntplLookaheadBuffer error code is {}: {}".format(ret, Wmx3Lib_adv.ErrorToString(ret)))
        return

if __name__ == '__main__':
    main()
