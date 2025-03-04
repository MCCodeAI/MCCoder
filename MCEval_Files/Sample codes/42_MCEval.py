# Write python code to Execute an absolute position path interpolation motion command of Axis 0 and 1 with auto smoothing and the velocity is 1000. The 1st segment is a linear interpolation to position (40, 100) with autoSmoothRadius 10, and the 2nd segment is a linear interpolation to position (80, 0) with autoSmoothRadius 20, and the 3rd segment is a linear interpolation to position (120, 100) with autoSmoothRadius 30, and the 4th segment is a linear interpolation to position (160, 0) with autoSmoothRadius 40, and the 5th segment is a linear interpolation to position (200, 100) with autoSmoothRadius 50, and the 6th segment is a linear interpolation to position (240, 0).
    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplCommand()

    path.SetAxis(0, 0)
    path.SetAxis(1, 1)

    # Use single motion profile for entire path
    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 1000
    profile.acc = 10000
    profile.dec = 10000
    path.SetProfile(0, profile)

    # Auto smoothing
    path.enableAutoSmooth = 1

    # Define linear segments
    path.numPoints = 6

    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 40)
    path.SetTarget(1, 0, 100)
    path.SetAutoSmoothRadius(0, 10)

    path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 1, 80)
    path.SetTarget(1, 1, 0)
    path.SetAutoSmoothRadius(1, 20)

    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 120)
    path.SetTarget(1, 2, 100)
    path.SetAutoSmoothRadius(2, 30)

    path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 3, 160)
    path.SetTarget(1, 3, 0)
    path.SetAutoSmoothRadius(3, 40)

    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 200)
    path.SetTarget(1, 4, 100)
    path.SetAutoSmoothRadius(4, 50)

    path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 5, 240)
    path.SetTarget(1, 5, 0)

    ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
    if ret != 0:
        print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 0)
    axes.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

