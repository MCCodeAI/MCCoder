# Write python code to Execute an absolute position path interpolation motion command of Axis 0 and 1 specifying the Motion Profile for Each Segment. The 1st segment is a linear interpolation to position (100, 0) with velocity and endvelocity 1000, the 2nd segment is a clockwise circular interpolation to position (150, 50) with center point (100, 50) with velocity and endvelocity 900, the 3rd segment is a linear interpolation to position (150, 100) with velocity and endvelocity 800, the 4th segment is a clockwise circular interpolation to position (100, 150) with center point (100, 100) with velocity and endvelocity 700, the 5th segment is a linear interpolation to position (0, 150) with velocity and endvelocity 600, the 6th segment is a clockwise circular interpolation to position (-50, 100) with center point (0, 100) with velocity and endvelocity 700, the 7th segment is a linear interpolation to position (-50, 50) with velocity and endvelocity 800, the 8th segment is a clockwise circular interpolation to position (0, 0) with center point (0, 50) with velocity 900. 
    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplCommand()

    path.SetAxis(0, 0)
    path.SetAxis(1, 1)

    # Specify motion profile for each segment
    path.enableConstProfile = 0

    # Define linear and circular segments
    path.numPoints = 8

    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 100)
    path.SetTarget(1, 0, 0)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 1000
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 1000
    path.SetProfile(0, profile)

    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, 150)
    path.SetTarget(1, 1, 50)
    path.SetCenterPos(0, 1, 100)
    path.SetCenterPos(1, 1, 50)
    path.SetDirection(1, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 900
    path.SetProfile(1, profile)

    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 150)
    path.SetTarget(1, 2, 100)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(2, profile)

    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, 100)
    path.SetTarget(1, 3, 150)
    path.SetCenterPos(0, 3, 100)
    path.SetCenterPos(1, 3, 100)
    path.SetDirection(3, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(3, profile)

    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 0)
    path.SetTarget(1, 4, 150)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 600
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 600
    path.SetProfile(4, profile)

    path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 5, -50)
    path.SetTarget(1, 5, 100)
    path.SetCenterPos(0, 5, 0)
    path.SetCenterPos(1, 5, 100)
    path.SetDirection(5, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(5, profile)

    path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 6, -50)
    path.SetTarget(1, 6, 50)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(6, profile)

    path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 7, 0)
    path.SetTarget(1, 7, 0)
    path.SetCenterPos(0, 7, 0)
    path.SetCenterPos(1, 7, 50)
    path.SetDirection(5, 1)

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    path.SetProfile(7, profile)

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


