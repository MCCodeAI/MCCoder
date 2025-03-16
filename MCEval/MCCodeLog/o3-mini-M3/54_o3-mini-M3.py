
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

import math

# Create a PVT interpolation command instance and configure axes.
pvti = Motion_PVTIntplCommand()
pvti.axisCount = 2
pvti.SetAxis(0, 4)  # Axis for Position0 (x-coordinate)
pvti.SetAxis(1, 5)  # Axis for Position1 (y-coordinate)

# Define the number of points: 20 points along a circle.
point_count = 20
pvti.SetPointCount(0, point_count)
pvti.SetPointCount(1, point_count)

# Circle parameters: diameter = 100, so radius = 50, and center = (-50, 0)
radius = 50
center_x = -50
center_y = 0

# Generate 20 points on the circle and set them for both axes.
for i in range(point_count):
    # Calculate the angle in radians
    angle = 2 * math.pi * i / point_count
    
    # Compute positions along the circle.
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    
    # Create PVT point objects for both Axis 4 and Axis 5.
    pvt_point_x = Motion_PVTPoint()
    pvt_point_y = Motion_PVTPoint()
    
    # Set positions, velocities and time for each point.
    # Velocity is fixed at 100 for both axes.
    # Time increments by 100 for each subsequent point (starting at 0).
    pvt_point_x.pos = x
    pvt_point_x.velocity = 100
    pvt_point_x.timeMilliseconds = i * 100
    
    pvt_point_y.pos = y
    pvt_point_y.velocity = 100
    pvt_point_y.timeMilliseconds = i * 100

    # Assign the points for Axis 4 (index 0) and Axis 5 (index 1).
    pvti.SetPoints(0, i, pvt_point_x)
    pvti.SetPoints(1, i, pvt_point_y)

# Start the PVT interpolation motion.
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print("StartPVT_Intpl error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for both Axis 4 and Axis 5 to complete the motion.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
