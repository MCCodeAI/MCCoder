
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

import math

# Create instance of the PVT Interpolation command
pvti = Motion_PVTIntplCommand()
pvti.axisCount = 2
pvti.SetAxis(0, 4)
pvti.SetAxis(1, 5)

# We have 20 interpolation points
point_count = 20
pvti.SetPointCount(0, point_count)
pvti.SetPointCount(1, point_count)

# The circle parameters: center (-50, 0) and diameter 100 (radius 50)
center_x = -50
center_y = 0
radius = 50

# Generate 20 equally spaced points on the circle
for i in range(point_count):
    # Compute the angle for this point (in radians)
    angle = 2 * math.pi * i / point_count
    # For Axis 4 (Position0) we use the x-coordinate, and for Axis 5 (Position1) we use the y-coordinate.
    pos_x = center_x + radius * math.cos(angle)
    pos_y = center_y + radius * math.sin(angle)
    # Velocity for both axes is set to 100
    velocity = 100
    # Time increments by 100 milliseconds for each point (starting at 0)
    time_ms = i * 100

    # Create new PVTPoint objects for each axis
    pvt_point_axis4 = Motion_PVTPoint()
    pvt_point_axis5 = Motion_PVTPoint()

    pvt_point_axis4.pos = pos_x
    pvt_point_axis4.velocity = velocity
    pvt_point_axis4.timeMilliseconds = time_ms

    pvt_point_axis5.pos = pos_y
    pvt_point_axis5.velocity = velocity
    pvt_point_axis5.timeMilliseconds = time_ms

    # Set the PVT point for each axis at the current index
    pvti.SetPoints(0, i, pvt_point_axis4)
    pvti.SetPoints(1, i, pvt_point_axis5)

# Start the PVT Interpolation motion
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # In a real application, you might want to exit or handle the error accordingly.

# Wait for Axis 4 and Axis 5 to become idle (stop moving)
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 4)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
