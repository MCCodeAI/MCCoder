
# Axes = [1]
# IOInputs = []
# IOOutputs = []

pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

# Set for Axis 1 with 6 points.
pvt.axis = 1
pvt.pointCount = 6

# Define point data:
# Point 0: (0, 0, 0)
pvtparameter.pos = 0
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 0
pvt.SetPoints(0, pvtparameter)

# Point 1: (50, 1000, 100)
pvtparameter.pos = 50
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 100
pvt.SetPoints(1, pvtparameter)

# Point 2: (100, 2000, 200)
pvtparameter.pos = 100
pvtparameter.velocity = 2000
pvtparameter.timeMilliseconds = 200
pvt.SetPoints(2, pvtparameter)

# Point 3: (200, 3000, 300)
pvtparameter.pos = 200
pvtparameter.velocity = 3000
pvtparameter.timeMilliseconds = 300
pvt.SetPoints(3, pvtparameter)

# Point 4: (300, 1000, 400)
pvtparameter.pos = 300
pvtparameter.velocity = 1000
pvtparameter.timeMilliseconds = 400
pvt.SetPoints(4, pvtparameter)

# Point 5: (200, 0, 500)
pvtparameter.pos = 200
pvtparameter.velocity = 0
pvtparameter.timeMilliseconds = 500
pvt.SetPoints(5, pvtparameter)

# Execute PVT motion on Axis 1
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 1 stops moving before proceeding.
    ret = Wmx3Lib_cm.motion.Wait(1)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
