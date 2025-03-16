
# Axes = [4, 5]
# Inputs = []
# Outputs = []

import math

# Define the circle parameters
diameter = 100
radius = diameter / 2
center_x = -50
center_y = 0
velocity = 100
num_points = 20

# Initialize the PVT interpolation command
pvti = Motion_PVTIntplCommand()
pvtparameter0 = Motion_PVTPoint()
pvtparameter1 = Motion_PVTPoint()

pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)
pvti.SetPointCount(0, num_points)
pvti.SetPointCount(1, num_points)

# Calculate the points on the circle
for i in range(num_points):
    angle = (2 * math.pi / num_points) * i
    pos0_x = center_x + radius * math.cos(angle)
    pos0_y = center_y + radius * math.sin(angle)
    pos1_x = center_x + radius * math.cos(angle + 2 * math.pi / num_points)
    pos1_y = center_y + radius * math.sin(angle + 2 * math.pi / num_points)
    time = 100 * i

    # Set the PVT points for Axis 4
    pvtparameter0.pos = pos0_x
    pvtparameter0.velocity = velocity
    pvtparameter0.timeMilliseconds = time
    pvti.SetPoints(0, i, pvtparameter0)

    # Set the PVT points for Axis 5
    pvtparameter1.pos = pos1_x
    pvtparameter1.velocity = velocity
    pvtparameter1.timeMilliseconds = time
    pvti.SetPoints(1, i, pvtparameter1)

# Start the PVT interpolation
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 4 and Axis 5 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
