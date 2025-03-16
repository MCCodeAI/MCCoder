
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Define a PT command for Axis 5 with specified points and times
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 5
pt.pointCount = 5

# Define point data
ptparameter.pos = 50
ptparameter.timeMilliseconds = 0
pt.SetPoints(0, ptparameter)

ptparameter.pos = -50
ptparameter.timeMilliseconds = 100
pt.SetPoints(1, ptparameter)

ptparameter.pos = 50
ptparameter.timeMilliseconds = 200
pt.SetPoints(2, ptparameter)

ptparameter.pos = -50
ptparameter.timeMilliseconds = 300
pt.SetPoints(3, ptparameter)

ptparameter.pos = 0
ptparameter.timeMilliseconds = 400
pt.SetPoints(4, ptparameter)

# Start PT motion
ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(5)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
