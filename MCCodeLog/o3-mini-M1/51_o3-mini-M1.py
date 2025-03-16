
# Axes = [1]
# IOInputs = []
# IOOutputs = []

pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 1
pvt.pointCount = 6

# Define point data for each point in the PVT command
pvtparameter.pos = 0
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 0
pvt.SetPoints(0, pvtparameter)

pvtparameter.pos = 50
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 100
pvt.SetPoints(1, pvtparameter)

pvtparameter.pos = 100
pvtparameter.velocity = 2000
pvtparameter.timeMilliseconds = 200
pvt.SetPoints(2, pvtparameter)

pvtparameter.pos = 200
pvtparameter.velocity = 3000
pvtparameter.timeMilliseconds = 300
pvt.SetPoints(3, pvtparameter)

pvtparameter.pos = 300
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 400
pvt.SetPoints(4, pvtparameter)

pvtparameter.pos = 200
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 500
pvt.SetPoints(5, pvtparameter)

# Start PVT motion for Axis 1
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed
    return

# Wait until the motion for Axis 1 is finished
ret = Wmx3Lib_cm.motion.Wait(0)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed
    return
