
# Axes = [7]
# Inputs = []
# Outputs = []

# Define the AT command for Axis 7 with specified points
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

# Start the AT command
ret = Wmx3Lib_cm.motion.StartAT(at)
if ret != 0:
    print('StartAT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(7)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
