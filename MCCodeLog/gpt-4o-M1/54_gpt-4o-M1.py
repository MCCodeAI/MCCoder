
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

import math

# Define the circle parameters
diameter = 100
radius = diameter / 2
center_x = -50
center_y = 0
velocity0 = 100
velocity1 = 100

# Generate 20 points on the circle
points = []
for i in range(20):
    angle = (2 * math.pi / 20) * i
    position0_x = center_x + radius * math.cos(angle)
    position0_y = center_y + radius * math.sin(angle)
    position1_x = center_x + radius * math.cos(angle + math.pi)
    position1_y = center_y + radius * math.sin(angle + math.pi)
    time = i * 100
    points.append((position0_x, velocity0, position1_x, velocity1, time))

# Execute PVT interpolation command for Axis 4 and Axis 5
pvti = Motion_PVTIntplCommand()

pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, len(points))
pvti.SetPointCount(1, len(points))

# Set the points for the PVT command
for index, (pos0, vel0, pos1, vel1, time) in enumerate(points):
    pvtparameter0.pos = pos0
    pvtparameter0.velocity = vel0
    pvtparameter0.timeMilliseconds = time
    pvtparameter1.pos = pos1
    pvtparameter1.velocity = vel1
    pvtparameter1.timeMilliseconds = time
    pvti.SetPoints(0, index, pvtparameter0)
    pvti.SetPoints(1, index, pvtparameter1)

# Start the PVT interpolation
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
