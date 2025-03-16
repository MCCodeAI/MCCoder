
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a PVT command for Axis 2
pvt = Motion_PVTCommand()
pvtparameter = Motion_PVTPoint()

pvt.axis = 2
pvt.pointCount = 10

# Populate the 10 points with data in the format (Position, Velocity, Time)
# Each point is calculated as: ( -2*i, 5*i, 10*i ) for i from 0 to 9.
for i in range(10):
    pvtparameter.pos = -2 * i
    pvtparameter.velocity = 5 * i
    pvtparameter.timeMilliseconds = 10 * i
    pvt.SetPoints(i, pvtparameter)

# Start the PVT motion for Axis 2
ret = Wmx3Lib_cm.motion.StartPVT(pvt)
if ret != 0:
    print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 2 stops moving after the motion command.
    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
