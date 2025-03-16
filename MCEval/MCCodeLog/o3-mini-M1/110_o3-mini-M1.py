
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = [3.1]

import time

# -------------------------------------------------------------------------
# Step 1:
# Record and execute an API buffer to simultaneously move Axis 7 to position 150
# and Axis 8 to position 180.
# -------------------------------------------------------------------------

Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Command for Axis 7 to move to 150
posCmd7 = Motion_PosCommand()
posCmd7.profile.type = ProfileType.Trapezoidal
posCmd7.axis = 7
posCmd7.target = 150
posCmd7.profile.velocity = 1000
posCmd7.profile.acc = 10000
posCmd7.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCmd7)
if ret != 0:
    print("StartPos error for Axis 7: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # You may choose to exit on error.

# Command for Axis 8 to move to 180
posCmd8 = Motion_PosCommand()
posCmd8.profile.type = ProfileType.Trapezoidal
posCmd8.axis = 8
posCmd8.target = 180
posCmd8.profile.velocity = 1000
posCmd8.profile.acc = 10000
posCmd8.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCmd8)
if ret != 0:
    print("StartPos error for Axis 8: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # You may choose to exit on error.

Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait until both Axis 7 and Axis 8 have stopped moving.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error after initial move: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# -------------------------------------------------------------------------
# Step 2:
# Linearly interpolate Axis 7 and Axis 8 to the new positions (191, 222) at
# a velocity of 1000 and with acceleration and deceleration of 10000.
# -------------------------------------------------------------------------

lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 8)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1000
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 191)
lin.SetTarget(1, 222)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print("StartLinearIntplPos error: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the linear interpolation motion is complete.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error after linear interpolation: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# -------------------------------------------------------------------------
# Step 3:
# Execute a trapezoidal profile type cubic spline for Axis 7 and Axis 8.
# The spline goes through the points: (0,0), (25,-50), (50,0), (75,50), (100,0)
# at a velocity of 1600.
# -------------------------------------------------------------------------

spline = Motion_CubicSplineCommand()  # Assumed to exist similar to other motion command objects.
spline.axisCount = 2
spline.SetAxis(0, 7)
spline.SetAxis(1, 8)
spline.profile.type = ProfileType.Trapezoidal
spline.profile.velocity = 1600
spline.profile.acc = 10000
spline.profile.dec = 10000

# Define 5 spline points for the two axes
spline.numPoints = 5
spline.SetPoint(0, 0, 0)       # (Axis7, Axis8) = (0, 0)
spline.SetPoint(1, 25, -50)    # (25, -50)
spline.SetPoint(2, 50, 0)       # (50, 0)
spline.SetPoint(3, 75, 50)      # (75, 50)
spline.SetPoint(4, 100, 0)      # (100, 0)

ret = Wmx3Lib_cm.motion.StartCubicSplinePos(spline)
if ret != 0:
    print("StartCubicSplinePos error: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# Wait until the cubic spline motion is complete.
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error after cubic spline: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))

# -------------------------------------------------------------------------
# Step 4:
# Toggle IO output: set output bit 3.1 to 1, wait 0.2 seconds, then set it to 0.
# Repeat this cycle 5 times.
# -------------------------------------------------------------------------

for i in range(5):
    ret = Wmx3Lib_cm.io.WriteBit(3, 1, 1)
    if ret != 0:
        print("IO WriteBit set error on cycle " + str(i+1) + ": " + str(ret))
    time.sleep(0.2)
    ret = Wmx3Lib_cm.io.WriteBit(3, 1, 0)
    if ret != 0:
        print("IO WriteBit reset error on cycle " + str(i+1) + ": " + str(ret))
    time.sleep(0.2)
