
# Axes = [7]
# IOInputs = []
# IOOutputs = [6.0, 7.1, 8.2]

# Execute an AT (Acceleration-Time) command for Axis 7 using points in the format (Acceleration, time): (700, 0), (-700, 100), (700, 200), (-700, 300), (0, 400).

at = Motion_ATCommand()
atparameter = Motion_ATPoint()

at.axis = 7
at.pointCount = 5

# Define point data
atparameter.acc = 700
atparameter.timeMilliseconds = 0
at.SetPoints(0, atparameter)

atparameter.acc = -700
atparameter.timeMilliseconds = 100
at.SetPoints(1, atparameter)

atparameter.acc = 700
atparameter.timeMilliseconds = 200
at.SetPoints(2, atparameter)

atparameter.acc = -700
atparameter.timeMilliseconds = 300
at.SetPoints(3, atparameter)

atparameter.acc = 0
atparameter.timeMilliseconds = 400
at.SetPoints(4, atparameter)

ret = Wmx3Lib_cm.motion.StartAT(at)
if ret != 0:
    print('StartAT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(7)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
