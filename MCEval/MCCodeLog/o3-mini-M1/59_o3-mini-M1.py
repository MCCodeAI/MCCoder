
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # Create an instance of the advanced motion controller.
    # Assumes that Wmx3Lib, Wmx3Lib_cm and all related classes and methods
    # (such as AdvancedMotion, AdvMotion_ProfileSplineCommand, Profile, 
    # AdvMotion_SplinePoint, AxisSelection, etc.) are already defined in the environment.
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free any previously allocated spline buffer on channel 0.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error: ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Create the spline channel buffer with a buffer size of 100.
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print('CreateSplineBuffer error code: ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    time.sleep(0.001)
    
    # Set the spline command options - using a trapezoidal profile.
    spl = AdvMotion_ProfileSplineCommand()
    spl.dimensionCount = 2
    # Set axis mapping: dimension 0 is Axis 6 and dimension 1 is Axis 9.
    spl.SetAxis(0, 6)
    spl.SetAxis(1, 9)
    
    spl.profile = Profile()
    spl.profile.type = ProfileType.Trapezoidal
    spl.profile.velocity = 1600
    spl.profile.acc = 10000
    spl.profile.dec = 10000

    # Define the spline points.
    # Points: (0, 0), (25, -50), (50, 0), (75, 50), (100, 0)
    # The first coordinate corresponds to Axis 6 and the second to Axis 9.
    pointData = [
        (0, 0),
        (25, -50),
        (50, 0),
        (75, 50),
        (100, 0)
    ]

    pt = []
    for (pos_axis6, pos_axis9) in pointData:
        point = AdvMotion_SplinePoint()
        point.SetPos(0, pos_axis6)
        point.SetPos(1, pos_axis9)
        pt.append(point)
    numPoints = len(pt)

    # Execute the cubic spline command.
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, numPoints, pt)
    if ret != 0:
        print('StartCSplinePos_Profile error code: ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait until the spline motion on both axes has completed.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 6)
    axes.SetAxis(1, 9)

    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code: ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Free the spline buffer once the motion is complete.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error code: ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    time.sleep(0.5)

if __name__ == '__main__':
    main()
