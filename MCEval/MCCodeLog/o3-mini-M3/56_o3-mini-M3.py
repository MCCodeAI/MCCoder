
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Execute a VT (Velocity-Time) command for Axis 6 using 5 points:
# Points: (60, 0), (-60, 100), (60, 200), (-60, 300), (0, 400)

# Create the VT command object and point holder
vt = Motion_VTCommand()
vt_point = Motion_VTPoint()

# Set the axis and the number of points
vt.axis = 6
vt.pointCount = 5

# Define the VT points
vt_point.velocity = 60
vt_point.timeMilliseconds = 0
vt.SetPoints(0, vt_point)

vt_point.velocity = -60
vt_point.timeMilliseconds = 100
vt.SetPoints(1, vt_point)

vt_point.velocity = 60
vt_point.timeMilliseconds = 200
vt.SetPoints(2, vt_point)

vt_point.velocity = -60
vt_point.timeMilliseconds = 300
vt.SetPoints(3, vt_point)

vt_point.velocity = 0
vt_point.timeMilliseconds = 400
vt.SetPoints(4, vt_point)

# Execute the VT command for Axis 6
ret = Wmx3Lib_cm.motion.StartVT(vt)
if ret != 0:
    print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 6 finishes moving
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
