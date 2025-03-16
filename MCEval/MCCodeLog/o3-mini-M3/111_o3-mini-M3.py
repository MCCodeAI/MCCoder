
import time

# Ensure the servos for Axis 5 and Axis 6 are turned on before executing the spline motion.
ret = Wmx3Lib_cm.axisControl.SetServoOn(5, 1)
if ret != 0:
    print('SetServoOn for Axis 5 error code {}: {}'.format(ret, Wmx3Lib_cm.ErrorToString(ret)))
ret = Wmx3Lib_cm.axisControl.SetServoOn(6, 1)
if ret != 0:
    print('SetServoOn for Axis 6 error code {}: {}'.format(ret, Wmx3Lib_cm.ErrorToString(ret)))

# Create a spline buffer with capacity for 100 points on channel 0.
ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
if ret != 0:
    print('CreateSplineBuffer error code {}: {}'.format(ret, Wmx3Lib_adv.ErrorToString(ret)))
    # Optionally, exit here

# Set up the cubic spline command for a total time of 1500 milliseconds (1.5 s).
spline_cmd = AdvMotion_TotalTimeSplineCommand()
spline_cmd.dimensionCount = 2  # Two axes (Axis 5 and Axis 6).
spline_cmd.SetAxis(0, 5)
spline_cmd.SetAxis(1, 6)
spline_cmd.totalTimeMilliseconds = 1500

# Prepare the spline points.
points = []

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 0)    # Axis 5 position: 0
pt.SetPos(1, 0)    # Axis 6 position: 0
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 25)   # Axis 5 position: 25
pt.SetPos(1, 50)   # Axis 6 position: 50
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 50)   # Axis 5 position: 50
pt.SetPos(1, 0)    # Axis 6 position: 0
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 75)   # Axis 5 position: 75
pt.SetPos(1, -50)  # Axis 6 position: -50
points.append(pt)

pt = AdvMotion_SplinePoint()
pt.SetPos(0, 100)  # Axis 5 position: 100
pt.SetPos(1, 0)    # Axis 6 position: 0
points.append(pt)

# Execute the cubic spline command on channel 0 using 5 spline points.
ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spline_cmd, 5, points)
if ret != 0:
    print('StartCSplinePos_TotalTime error code {}: {}'.format(ret, Wmx3Lib_adv.ErrorToString(ret)))
    # Optionally, exit here

# Wait until both Axis 5 and Axis 6 finish the spline motion.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 5)
axes.SetAxis(1, 6)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print('Wait_AxisSel error code {}: {}'.format(ret, Wmx3Lib_adv.ErrorToString(ret)))
    # Optionally, exit here

# Free the spline buffer (normally done at the end of application if no further spline motions are planned).
ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
if ret != 0:
    print('FreeSplineBuffer error code {}: {}'.format(ret, Wmx3Lib_adv.ErrorToString(ret)))
    # Optionally, exit here

time.sleep(0.5)

# --- Additional Code Sections (Cyclic Buffer for Axis 1, PVT for Axis 2, PT for Axis 3, VT for Axis 4, 
#     move Axis 5, and other motions) would follow here. Each motion should include a wait-for-motion-complete 
#     after the motion command if it is a separate motion, but be omitted in the middle of continuous motion. ---

# Example snippet for inserting a sleep period (if required).
time.sleep(1.6)

# --- I/O Operation Section ---
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x01)
if ret != 0:
    print('SetOutBit error code {}: {}'.format(ret, Wmx3Lib_Io.ErrorToString(ret)))
time.sleep(0.15)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x00)
if ret != 0:
    print('SetOutBit error code {}: {}'.format(ret, Wmx3Lib_Io.ErrorToString(ret)))
