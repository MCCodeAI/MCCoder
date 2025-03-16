# Write python code to Execute a VT (Velocity-Time) command of Axis 0 of 6 points: (0,0),(100,500),(200,1000),(300,1500),(400,2000),(500,2500)
    # Axes = [0]

    vt = Motion_VTCommand()
    vtparameter = Motion_VTPoint()

    vt.axis = 0
    vt.pointCount = 6

    # Define point data
    vtparameter.velocity = 0
    vtparameter.timeMilliseconds = 0
    vt.SetPoints(0, vtparameter)

    vtparameter.velocity = 100
    vtparameter.timeMilliseconds = 500
    vt.SetPoints(1, vtparameter)

    vtparameter.velocity = 200
    vtparameter.timeMilliseconds = 1000
    vt.SetPoints(2, vtparameter)

    vtparameter.velocity = 300
    vtparameter.timeMilliseconds = 1500
    vt.SetPoints(3, vtparameter)

    vtparameter.velocity = 400
    vtparameter.timeMilliseconds = 2000
    vt.SetPoints(4, vtparameter)

    vtparameter.velocity = 500
    vtparameter.timeMilliseconds = 2500
    vt.SetPoints(5, vtparameter)

    ret = Wmx3Lib_cm.motion.StartVT(vt)
    if ret != 0:
        print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until motion is finished
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
