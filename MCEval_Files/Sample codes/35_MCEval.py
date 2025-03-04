# Write python code to Execute anw AT (Acceleration-Time) command of Axis 0 of 7 points: (0,0),(100,500),(100,1000),(-100,1500),(100,2000),(-100,2500),(-100,3000)
    # Axes = [0]

    at = Motion_ATCommand()
    atparameter = Motion_ATPoint()

    at.axis = 0
    at.pointCount = 7

    # Define point data
    atparameter.acc = 0
    atparameter.timeMilliseconds = 0
    at.SetPoints(0, atparameter)

    atparameter.acc = 100
    atparameter.timeMilliseconds = 500
    at.SetPoints(1, atparameter)

    atparameter.acc = 100
    atparameter.timeMilliseconds = 1000
    at.SetPoints(2, atparameter)

    atparameter.acc = -100
    atparameter.timeMilliseconds = 1500
    at.SetPoints(3, atparameter)

    atparameter.acc = 100
    atparameter.timeMilliseconds = 2000
    at.SetPoints(4, atparameter)

    atparameter.acc = -100
    atparameter.timeMilliseconds = 2500
    at.SetPoints(5, atparameter)

    atparameter.acc = -100
    atparameter.timeMilliseconds = 3000
    at.SetPoints(6, atparameter)

    ret = Wmx3Lib_cm.motion.StartAT(at)
    if ret != 0:
        print('StartAT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
