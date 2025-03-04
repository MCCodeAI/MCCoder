# Write python code to Execute a simple PVT command of Axis 0 consisting of five points as a format of (Position, Velocity, Time): (0,0,0),(55,1000,100),(205,2000,200),(450,3000,300),(600,0,400)
    # Axes = [0]

    pvt = Motion_PVTCommand()
    pvtparameter = Motion_PVTPoint()

    pvt.axis = 0
    pvt.pointCount = 5

    # Define point data
    pvtparameter.pos = 0
    pvtparameter.velocity = 0
    pvtparameter.timeMilliseconds = 0
    pvt.SetPoints(0, pvtparameter)

    pvtparameter.pos = 55
    pvtparameter.velocity = 1000
    pvtparameter.timeMilliseconds = 100
    pvt.SetPoints(1, pvtparameter)

    pvtparameter.pos = 205
    pvtparameter.velocity = 2000
    pvtparameter.timeMilliseconds = 200
    pvt.SetPoints(2, pvtparameter)

    pvtparameter.pos = 450
    pvtparameter.velocity = 3000
    pvtparameter.timeMilliseconds = 300
    pvt.SetPoints(3, pvtparameter)

    pvtparameter.pos = 600
    pvtparameter.velocity = 0
    pvtparameter.timeMilliseconds = 400
    pvt.SetPoints(4, pvtparameter)

    # Start PVT motion
    ret = Wmx3Lib_cm.motion.StartPVT(pvt)
    if ret != 0:
        print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
