
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create an AT command with 5 points for Axis 7
at = Motion_ATCommand()
atparameter = Motion_ATPoint()

at.axis = 7
at.pointCount = 5

# Define point 1: (700, 0)
atparameter.acc = 700
atparameter.timeMilliseconds = 0
at.SetPoints(0, atparameter)

# Define point 2: (-700, 100)
atparameter.acc = -700
atparameter.timeMilliseconds = 100
at.SetPoints(1, atparameter)

# Define point 3: (700, 200)
atparameter.acc = 700
atparameter.timeMilliseconds = 200
at.SetPoints(2, atparameter)

# Define point 4: (-700, 300)
atparameter.acc = -700
atparameter.timeMilliseconds = 300
at.SetPoints(3, atparameter)

# Define point 5: (0, 400)
atparameter.acc = 0
atparameter.timeMilliseconds = 400
at.SetPoints(4, atparameter)

# Start the AT command for Axis 7
ret = Wmx3Lib_cm.motion.StartAT(at)
if ret != 0:
    print('StartAT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 7 stops moving after executing the AT command.
    ret = Wmx3Lib_cm.motion.Wait(7)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
