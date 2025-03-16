
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

import time

# Dummy sleep function for clarity
def sleep(duration):
    time.sleep(duration)

def main():
    # Create an object to access advanced motion functions.
    # It is assumed that Wmx3Lib and AdvancedMotion are available in the environment.
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free any previously allocated spline buffer on channel 0.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    
    # Create the spline channel buffer with a capacity of 200 points.
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
    if ret != 0:
        print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(0.001)

    # Set up the S-curve spline command options.
    # This command will generate a cubic spline motion with s curve profile limits.
    spl = AdvMotion_SCurveSplineCommand()
    spl.dimensionCount = 2
    # Map axis index 0 to Axis 6 and index 1 to Axis 9.
    spl.SetAxis(0, 6)
    spl.SetAxis(1, 9)
    # Set velocity and acceleration limits for both axes.
    spl.SetVelLimit(0, 1200)
    spl.SetVelLimit(1, 1200)
    spl.SetAccLimit(0, 5000)
    spl.SetAccLimit(1, 5000)
    # Increase the sample multiplier for improved accuracy if necessary.
    spl.sampleMultiplier = 20

    # Define the spline points.
    # The points are defined in the order:
    #   axis 6 position (first coordinate) and axis 9 position (second coordinate)
    pt = []

    point = AdvMotion_SplinePoint()
    point.SetPos(0, 0)
    point.SetPos(1, 0)
    pt.append(point)

    point = AdvMotion_SplinePoint()
    point.SetPos(0, 30)
    point.SetPos(1, 50)
    pt.append(point)

    point = AdvMotion_SplinePoint()
    point.SetPos(0, 60)
    point.SetPos(1, 0)
    pt.append(point)

    point = AdvMotion_SplinePoint()
    point.SetPos(0, 90)
    point.SetPos(1, 50)
    pt.append(point)

    point = AdvMotion_SplinePoint()
    point.SetPos(0, 120)
    point.SetPos(1, 0)
    pt.append(point)

    # Execute the S-curve cubic spline motion command.
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_SCurve(0, spl, 5, pt)
    if ret != 0:
        print('StartCSplinePos_SCurve error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the motion to complete for both axes.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 6)
    axes.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Free the spline buffer; typically done at the end of the application or after the motion completes.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(0.5)

if __name__ == "__main__":
    main()
