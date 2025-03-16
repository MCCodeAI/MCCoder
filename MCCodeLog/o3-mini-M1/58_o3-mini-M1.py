
# Axes = [8, 9]
# IOInputs = []
# IOOutputs = []

def main():
    # Initialize the advanced motion library (assumes Wmx3Lib is already defined)
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free any existing spline buffer on channel 0
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print("FreeSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Create the spline channel buffer with capacity for 100 points on channel 0
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print("CreateSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Set the spline command options for a total time cubic spline motion
    spl = AdvMotion_TotalTimeSplineCommand()
    spl.dimensionCount = 2
    spl.SetAxis(0, 8)
    spl.SetAxis(1, 9)
    spl.totalTimeMilliseconds = 1500  # 1.5 seconds

    # Define control points for the cubic spline
    pt = []

    # 1st point: (0, 0)
    pt.append(AdvMotion_SplinePoint())
    pt[0].SetPos(0, 0)
    pt[0].SetPos(1, 0)

    # 2nd point: (25, 50)
    pt.append(AdvMotion_SplinePoint())
    pt[1].SetPos(0, 25)
    pt[1].SetPos(1, 50)

    # 3rd point: (50, 0)
    pt.append(AdvMotion_SplinePoint())
    pt[2].SetPos(0, 50)
    pt[2].SetPos(1, 0)

    # 4th point: (75, -50)
    pt.append(AdvMotion_SplinePoint())
    pt[3].SetPos(0, 75)
    pt[3].SetPos(1, -50)

    # 5th point: (100, 0)
    pt.append(AdvMotion_SplinePoint())
    pt[4].SetPos(0, 100)
    pt[4].SetPos(1, 0)

    # Execute the cubic spline motion command
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spl, 5, pt)
    if ret != 0:
        print("StartCSplinePos_TotalTime error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 8)
    axes.SetAxis(1, 9)

    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Free the spline buffer (typically freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print("FreeSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
