
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Create an instance of the PT command for Axis 5 using 5 points.
pt = Motion_PTCommand()
ptparameter = Motion_PTPoint()

pt.axis = 5
pt.pointCount = 5

# Define point 0: (50, 0)
ptparameter.pos = 50
ptparameter.timeMilliseconds = 0
pt.SetPoints(0, ptparameter)

# Define point 1: (-50, 100)
ptparameter.pos = -50
ptparameter.timeMilliseconds = 100
pt.SetPoints(1, ptparameter)

# Define point 2: (50, 200)
ptparameter.pos = 50
ptparameter.timeMilliseconds = 200
pt.SetPoints(2, ptparameter)

# Define point 3: (-50, 300)
ptparameter.pos = -50
ptparameter.timeMilliseconds = 300
pt.SetPoints(3, ptparameter)

# Define point 4: (0, 400)
ptparameter.pos = 0
ptparameter.timeMilliseconds = 400
pt.SetPoints(4, ptparameter)

# Start the PT motion command for Axis 5.
ret = Wmx3Lib_cm.motion.StartPT(pt)
if ret != 0:
    print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 5 has stopped moving after the PT motion.
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
