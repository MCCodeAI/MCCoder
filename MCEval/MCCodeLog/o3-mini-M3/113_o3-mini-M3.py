
import math
import time

# Ensure that Axis 3 and Axis 5 are servo on before starting any motion.
for axis in [3, 5]:
    ret = Wmx3Lib_cm.motion.SetServoOn(axis)
    if ret != 0:
        print("SetServoOn for axis {} failed with error code {}: {}".format(axis, ret, Wmx3Lib_cm.ErrorToString(ret)))
        exit()
    # Wait until the axis reports ServoOn state.
    counter = 1000
    while counter > 0:
        st = Wmx3Lib_cm.GetStatus()  # Assumes GetStatus() returns an object with AxesStatus dictionary keyed by axis numbers.
        if st.AxesStatus[axis].ServoOn:
            break
        time.sleep(0.01)
        counter -= 1
    if counter == 0:
        print("Timeout: Servo did not turn on for axis {}".format(axis))
        exit()

# Create a PVT interpolation command for Axis 3 and Axis 5
pvti = Motion_PVTIntplCommand()
pvti.axisCount = 2
pvti.SetAxis(0, 3)
pvti.SetAxis(1, 5)

numPoints = 20
pvti.SetPointCount(0, numPoints)
pvti.SetPointCount(1, numPoints)

# Parameters for the circle
center_x = -50
center_y = 0
radius = 50

# For each point, compute coordinates on the circle,
# assign velocity=100 for both axes and time increments by 100 ms for each point.
for i in range(numPoints):
    theta = (2 * math.pi * i) / numPoints
    x = center_x + radius * math.cos(theta)
    y = center_y + radius * math.sin(theta)
    t_ms = i * 100

    # Set point for Axis 3 (Position0)
    pvt_point_axis3 = Motion_PVTPoint()
    pvt_point_axis3.pos = x
    pvt_point_axis3.velocity = 100
    pvt_point_axis3.timeMilliseconds = t_ms
    pvti.SetPoints(0, i, pvt_point_axis3)

    # Set corresponding point for Axis 5 (Position1)
    pvt_point_axis5 = Motion_PVTPoint()
    pvt_point_axis5.pos = y
    pvt_point_axis5.velocity = 100
    pvt_point_axis5.timeMilliseconds = t_ms
    pvti.SetPoints(1, i, pvt_point_axis5)

# Start the PVT interpolation command for Axis 3 and Axis 5
ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
if ret != 0:
    print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until both axes (3 and 5) stop moving after motion completes
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 3)
axisSel.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Example of a sleep call corrected to use time.sleep which avoids the UnboundLocalError.
time.sleep(1.6)
