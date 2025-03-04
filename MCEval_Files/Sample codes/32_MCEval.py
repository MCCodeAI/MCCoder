# Write python code to Execute a PVT interpolation command of Axis 0 and Axis 1 of 4 points as a format of (Position0, Velocity0, Time0, Position1, Velocity1, Time1): (0,0,0,0,0,0),(50,1000,100,100,2000,100),(100,2000,200,250,1000,200),(200,0,300,300,0,300)
    # Axes = [0, 1]

    pvti = Motion_PVTIntplCommand()

    pvtparameter0 = Motion_PVTPoint()
    pvtparameter1 = Motion_PVTPoint()

    pvti.axisCount = 2
    pvti.SetAxis(0, 0)
    pvti.SetAxis(1, 1)
    pvti.SetPointCount(0, 4)
    pvti.SetPointCount(1, 4)

    # Define point data
    pvtparameter0.pos = 0
    pvtparameter0.velocity = 0
    pvtparameter0.timeMilliseconds = 0
    pvtparameter1.pos = 0
    pvtparameter1.velocity = 0
    pvtparameter1.timeMilliseconds = 0
    pvti.SetPoints(0, 0, pvtparameter0)
    pvti.SetPoints(1, 0, pvtparameter1)

    pvtparameter0.pos = 50
    pvtparameter0.velocity = 1000
    pvtparameter0.timeMilliseconds = 100
    pvtparameter1.pos = 100
    pvtparameter1.velocity = 2000
    pvtparameter1.timeMilliseconds = 100
    pvti.SetPoints(0, 1, pvtparameter0)
    pvti.SetPoints(1, 1, pvtparameter1)

    pvtparameter0.pos = 100
    pvtparameter0.velocity = 2000
    pvtparameter0.timeMilliseconds = 200
    pvtparameter1.pos = 250
    pvtparameter1.velocity = 1000
    pvtparameter1.timeMilliseconds = 200
    pvti.SetPoints(0, 2, pvtparameter0)
    pvti.SetPoints(1, 2, pvtparameter1)

    pvtparameter0.pos = 200
    pvtparameter0.velocity = 0
    pvtparameter0.timeMilliseconds = 300
    pvtparameter1.pos = 300
    pvtparameter1.velocity = 0
    pvtparameter1.timeMilliseconds = 300
    pvti.SetPoints(0, 3, pvtparameter0)
    pvti.SetPoints(1, 3, pvtparameter1)


    ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
    if ret != 0:
        print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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
    