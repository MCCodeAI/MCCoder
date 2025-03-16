
# Axes = [6]
# Inputs = []
# Outputs = []

vt = Motion_VTCommand()
vtparameter = Motion_VTPoint()

vt.axis = 6
vt.pointCount = 5

# Define point data
vtparameter.velocity = 60
vtparameter.timeMilliseconds = 0
vt.SetPoints(0, vtparameter)

vtparameter.velocity = -60
vtparameter.timeMilliseconds = 100
vt.SetPoints(1, vtparameter)

vtparameter.velocity = 60
vtparameter.timeMilliseconds = 200
vt.SetPoints(2, vtparameter)

vtparameter.velocity = -60
vtparameter.timeMilliseconds = 300
vt.SetPoints(3, vtparameter)

vtparameter.velocity = 0
vtparameter.timeMilliseconds = 400
vt.SetPoints(4, vtparameter)

ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
