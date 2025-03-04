# Write python code to Start an absolute position path interpolation motion command of Axis 0 and 1 with velocity 1000. The 1st segment is a linear interpolation to position (-200, -200), the 2nd segment is a counterclockwise circular interpolation to position (-150, -200) with center point (0, 0), the 3rd segment is a linear interpolation to position (-180, -10), and the 4th segment is a clockwise circular interpolation to position (-10, -150) with center point (0, 0).
# clockwise: If 0, the arc will rotate in the counterclockwise direction. If 1, the arc will rotate in the clockwise direction.

    # Axes = [0, 1]

    adv = AdvancedMotion(Wmx3Lib)
    path = AdvMotion_PathIntplCommand()

    path.SetAxis(0, 0)
    path.SetAxis(1, 1)

    path.enableConstProfile = 1

    path.profile = Profile()
    path.profile.type = ProfileType.Trapezoidal
    path.profile.velocity = 1000
    path.profile.acc = 10000
    path.profile.dec = 10000

    path.numPoints = 4

    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)

    path.SetTarget(0, 0, -200)
    path.SetTarget(1, 0, -200)

    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, -150)
    path.SetTarget(1, 1, -200)
    path.SetCenterPos(0, 1, 0)
    path.SetCenterPos(1, 1, 0)
    path.SetDirection(1, 1)  # 1 for counterclockwise    -1 clockwise

    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, -180)
    path.SetTarget(1, 2, -10)

    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, -10)
    path.SetTarget(1, 3, -150)
    path.SetCenterPos(0, 3, 0)
    path.SetCenterPos(1, 3, 0)
    path.SetDirection(3, -1)   # 1 for counterclockwise    -1 clockwise

    ret = adv.advMotion.StartPathIntplPos(path)
    if ret!=0:
            print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
            return

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
