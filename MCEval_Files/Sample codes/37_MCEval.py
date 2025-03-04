# Write python code to Execute a trapezoidal profile type cubic spline of Axis 0 and Axis 1 with 9 points and the velocity is 1000: (0,0),(100,0),(50,50),(100,100),(100,150),(0,150),(0,100),(50,50),(0,0).
    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
        
    # Create the spline channel buffer
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print('CreateSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(0.001)
    # Set the spline command options
    spl = AdvMotion_ProfileSplineCommand()
    spl.dimensionCount = 2
    spl.SetAxis(0, 0)
    spl.SetAxis(1, 1)
    spl.profile = Profile()
    spl.profile.type = ProfileType.Trapezoidal
    spl.profile.velocity = 1000
    spl.profile.acc = 10000
    spl.profile.dec = 10000

    pt = []

    pt.append(AdvMotion_SplinePoint())
    pt[0].SetPos(0, 0)
    pt[0].SetPos(1, 0)

    pt.append(AdvMotion_SplinePoint())
    pt[1].SetPos(0, 100)
    pt[1].SetPos(1, 0)

    pt.append(AdvMotion_SplinePoint())
    pt[2].SetPos(0, 50)
    pt[2].SetPos(1, 50)

    pt.append(AdvMotion_SplinePoint())
    pt[3].SetPos(0, 100)
    pt[3].SetPos(1, 100)

    pt.append(AdvMotion_SplinePoint())
    pt[4].SetPos(0, 100)
    pt[4].SetPos(1, 150)

    pt.append(AdvMotion_SplinePoint())
    pt[5].SetPos(0, 0)
    pt[5].SetPos(1, 150)

    pt.append(AdvMotion_SplinePoint())
    pt[6].SetPos(0, 0)
    pt[6].SetPos(1, 100)

    pt.append(AdvMotion_SplinePoint())
    pt[7].SetPos(0, 50)
    pt[7].SetPos(1, 50)

    pt.append(AdvMotion_SplinePoint())
    pt[8].SetPos(0, 0)
    pt[8].SetPos(1, 0)

    # Execute the spline command
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, 9, pt)
    if ret != 0:
        print('StartCSplinePos_Profile error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
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

    # Free the spline buffer (normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0:
        print('FreeSplineBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
    
    sleep(0.5)
