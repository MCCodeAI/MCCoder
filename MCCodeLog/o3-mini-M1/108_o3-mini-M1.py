
# Axes = [7, 9]
# IOInputs = []
# IOOutputs = [0.7]

import time

# -----------------------------
# 1. Move Axis 7 to position 220 with a speed of 1500.
# -----------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 220
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
# Wait for Axis 7 to become idle.
Wmx3Lib_cm.motion.Wait(7)

# -----------------------------
# 2. Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0.
# -----------------------------
Wmx3Lib_cm.io.SetDigitalOut(0, 7, 1)
time.sleep(0.2)
Wmx3Lib_cm.io.SetDigitalOut(0, 7, 0)

# -----------------------------
# 3. Start an absolute linear interpolation for Axes 7 and 9 to position (200, 50) with a velocity of 1200.
# -----------------------------
lin = Motion_LinearIntplCommand()
lin.axisCount = 2 
lin.SetAxis(0, 7)
lin.SetAxis(1, 9)

lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1200
lin.profile.acc = 10000
lin.profile.dec = 10000

lin.SetTarget(0, 200)  # Target for Axis 7
lin.SetTarget(1, 50)   # Target for Axis 9

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for Axes 7 and 9 to become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# -----------------------------
# 4. Start a relative linear interpolation for Axes 7 and 9 to position (-100, 50).
# -----------------------------
# Reusing the same linear interpolation command, but now for a relative motion.
lin.SetTarget(0, -100)  # Relative move for Axis 7
lin.SetTarget(1, 50)    # Relative move for Axis 9

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for Axes 7 and 9 to become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# -----------------------------
# 5. Start a counterclockwise circular interpolation motion command for Axes 7 and 9.
#    - Center position: (50, 50)
#    - Arc length: 270
#    - Velocity: 1000
# -----------------------------
circCommand = Motion_CircularIntplCommand()
circCommand.axisCount = 2
circCommand.SetAxis(0, 7)
circCommand.SetAxis(1, 9)

circCommand.profile.type = ProfileType.Trapezoidal
circCommand.profile.velocity = 1000
circCommand.profile.acc = 10000
circCommand.profile.dec = 10000

# Set the center point for the circular arc.
circCommand.SetCenterPos(0, 50)
circCommand.SetCenterPos(1, 50)

# Set motion parameters
circCommand.arcLengthDegree = 270
# For circular interpolation, 0 indicates counterclockwise rotation.
circCommand.clockwise = 0  

ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circCommand)
if ret != 0:
    print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait for Axes 7 and 9 to become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
