# Write python code to Execute a PT (Position-Time) command of Axis 0 of 6 points: (0,0),(100,500),(160,1000),(200,1500),(260,2000),(300,2500)
    # Axes = [0]

    pt = Motion_PTCommand()
    ptparameter = Motion_PTPoint()

    pt.axis = 0
    pt.pointCount = 6

    # Define point data
    ptparameter.pos = 0
    ptparameter.timeMilliseconds = 0
    pt.SetPoints(0, ptparameter)

    ptparameter.pos = 100
    ptparameter.timeMilliseconds = 500
    pt.SetPoints(1, ptparameter)

    ptparameter.pos = 160
    ptparameter.timeMilliseconds = 1000
    pt.SetPoints(2, ptparameter)

    ptparameter.pos = 200
    ptparameter.timeMilliseconds = 1500
    pt.SetPoints(3, ptparameter)

    ptparameter.pos = 260
    ptparameter.timeMilliseconds = 2000
    pt.SetPoints(4, ptparameter)

    ptparameter.pos = 300
    ptparameter.timeMilliseconds = 2500
    pt.SetPoints(5, ptparameter)

    ret = Wmx3Lib_cm.motion.StartPT(pt)
    if ret != 0:
        print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    

