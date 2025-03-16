
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

# Calculate 20 points on a circle with diameter 100 and center at (-50, 0)
import math

# Circle parameters
radius = 50
center_x = -50
center_y = 0
num_points = 20

# Generate points
points = []
for i in range(num_points):
    theta = (2 * math.pi * i) / num_points
    x = center_x + radius * math.cos(theta)
    y = center_y + radius * math.sin(theta)
    points.append((x, y))

# Create PVT interpolation command
pvti = Motion_PVTIntplCommand()

pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, num_points)
pvti.SetPointCount(1, num_points)

# Define point data
for i in range(num_points):
    time = i * 100
    
    # Set parameters for Axis 4 (X-axis)
    pvtparameter0.pos = points[i][0]
    pvtparameter0.velocity = 100
    pvtparameter0.timeMilliseconds = time
    
    # Set parameters for Axis 5 (Y-axis)
    pvtparameter1.pos = points[i][1]
    pvtparameter1.velocity = 100
    pvtparameter1.timeMilliseconds = time
    
    pvti.SetPoints(0, i, pvtparameter0)
    pvti.SetPoints(1, i, pvtparameter1)

# Start PVT interpolation motion
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
