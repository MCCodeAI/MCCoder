
# Axes = [2]
# IOInputs = []
# IOOutputs = []

pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 10

# Define point data for i from 0 to 9
for i in range(10):
    pvtparameter.pos = -2 * i
    pvtparameter.velocity = 5 * i
    pvtparameter.timeMilliseconds = 10 * i
    pvt.SetPoints(i, pvtparameter)

# Start PVT motion
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
