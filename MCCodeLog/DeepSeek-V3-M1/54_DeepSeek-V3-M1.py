
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

import math

# Function to generate points on a circle
def generate_circle_points(center_x, center_y, diameter, num_points):
    radius = diameter / 2
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points

# Generate 20 points on a circle with diameter 100 and center at (-50, 0)
circle_points = generate_circle_points(-50, 0, 100, 20)

# Initialize PVT interpolation command
pvti = Motion_PVTIntplCommand()

# Set axis count and assign axes
pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)

# Set point count for each axis
pvti.SetPointCount(0, 20)
pvti.SetPointCount(1, 20)

# Define PVT points
pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

# Populate PVT points with circle points
for i in range(20):
    pvtparameter0.pos = circle_points[i][0]
    pvtparameter0.velocity = 100
    pvtparameter0.timeMilliseconds = i * 100
    pvtparameter1.pos = circle_points[i][1]
    pvtparameter1.velocity = 100
    pvtparameter1.timeMilliseconds = i * 100
    pvti.SetPoints(0, i, pvtparameter0)
    pvti.SetPoints(1, i, pvtparameter1)

# Start PVT interpolation motion
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
