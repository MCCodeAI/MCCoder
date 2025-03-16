
# Axes = [8, 9]
# IOInputs = []
# IOOutputs = []

def cubic_spline_motion():
    # Instantiate the advanced motion handler.
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    
    # Free existing spline buffer (channel 0) if allocated.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    
    # Allocate buffer memory for a spline execution channel with capacity for 100 points.
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Set up the cubic spline command options for a total motion time of 1000ms.
    splineCommand = AdvMotion_TotalTimeSplineCommand()
    splineCommand.dimensionCount = 2
    # Map first dimension to Axis 8 and the second dimension to Axis 9.
    splineCommand.SetAxis(0, 8)
    splineCommand.SetAxis(1, 9)
    splineCommand.totalTimeMilliseconds = 1000

    # Define the 9 spline points.
    # Points: (0,0), (10,-10), (-20,20), (30,-30), (-40,40),
    #         (50,-50), (-60,60), (70,-70), (0,0)
    points = [(0, 0), (10, -10), (-20, 20), (30, -30), (-40, 40),
              (50, -50), (-60, 60), (70, -70), (0, 0)]
    
    splinePoints = []
    for pt in points:
        point = AdvMotion_SplinePoint()
        point.SetPos(0, pt[0])
        point.SetPos(1, pt[1])
        splinePoints.append(point)

    # Execute the cubic spline command on channel 0.
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, splineCommand, len(splinePoints), splinePoints)
    if ret != 0:
        print('StartCSplinePos_TotalTime error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for Axes 8 and 9 to complete the motion.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 8)
    axes.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Free the spline buffer (typically done at the end of the application).
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

if __name__ == '__main__':
    cubic_spline_motion()
