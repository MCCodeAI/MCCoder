
# Axes = [6, 7, 8]
# IOInputs = []
# IOOutputs = [6.7]

# This script demonstrates multiple motion commands according to the given question:
# 1. Move Axis 6 to position 20 using a trapezoidal profile at 900 velocity.
# 2. Set IO output bit 6.7 to 1, sleep for 0.1 seconds, then set it to 0.
# 3. Move Axis 7 to position 30.
# 4. Linearly interpolate Axes 7 and 8 to positions (40, 50).
# 5. Start a clockwise circular interpolation motion command for Axes 6 and 7 with center (50,50) and an arc length of 360°.
# 6. Establish a synchronous control between master Axis 6 and slave Axis 7 (via a simple E‐CAM configuration) and then move Axis 6 to position 60.
#
# NOTE: This example follows the code structure in the provided context.
#       It assumes that objects such as Wmx3Lib_cm, Wmx3Lib_adv, and various command classes (e.g. Motion_PosCommand)
#       as well as the IO interface (Wmx3Lib_cm.io) and platform-specific waiting functions are already defined.

from time import sleep

# ---- Step 1: Move Axis 6 to position 20 using a trapezoidal profile at 900 velocity. ----
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('Error starting position command on Axis 6: ' + str(ret))
    # Optionally return or raise an exception

# Wait for Axis 6 to stop moving.
Wmx3Lib_cm.motion.Wait(6)


# ---- Step 2: Set IO output bit 6.7 to 1, sleep 0.1 sec, then set it to 0 ----
ret = Wmx3Lib_cm.io.Write(6, 7, 1)
if ret != 0:
    print('Error setting IO output 6.7 to 1: ' + str(ret))
sleep(0.1)
ret = Wmx3Lib_cm.io.Write(6, 7, 0)
if ret != 0:
    print('Error setting IO output 6.7 to 0: ' + str(ret))


# ---- Step 3: Move Axis 7 to position 30 ----
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 30
posCommand.profile.velocity = 900
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('Error starting position command on Axis 7: ' + str(ret))
Wmx3Lib_cm.motion.Wait(7)


# ---- Step 4: Linearly interpolate Axes 7 and 8 to positions (40, 50) ----
linIntplCommand = Motion_LineIntplCommand()
# Set the interpolation axes
linIntplCommand.SetAxis(0, 7)
linIntplCommand.SetAxis(1, 8)
# Set target positions for Axis 7 and 8 respectively.
linIntplCommand.SetTargetPos(0, 40)
linIntplCommand.SetTargetPos(1, 50)
# Configure the motion profile.
linIntplCommand.profile.type = ProfileType.Trapezoidal
linIntplCommand.profile.velocity = 900
linIntplCommand.profile.acc = 1000
linIntplCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartLineIntplPos(linIntplCommand)
if ret != 0:
    print('Error starting linear interpolation for Axes 7 and 8: ' + str(ret))
# Wait until both Axis 7 and Axis 8 finish the motion.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 8)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Error waiting for linear interpolation to complete: ' + str(ret))


# ---- Step 5: Start clockwise circular interpolation for Axes 6 and 7 with center (50,50) and arc length 360 ----
circCommand = Motion_CircIntplCommand()
circCommand.SetAxis(0, 6)
circCommand.SetAxis(1, 7)
circCommand.SetCenterPos(0, 50)
circCommand.SetCenterPos(1, 50)
circCommand.arcLengthDegree = 360
# 1 indicates clockwise motion.
circCommand.clockwise = 1
# Set the motion profile.
circCommand.profile.type = ProfileType.Trapezoidal
circCommand.profile.velocity = 900
circCommand.profile.acc = 1000
circCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartCircIntplPos(circCommand)
if ret != 0:
    print('Error starting circular interpolation for Axes 6 and 7: ' + str(ret))
# Wait until both Axis 6 and Axis 7 complete the motion.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 6)
axisSel.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Error waiting for circular interpolation to complete: ' + str(ret))


# ---- Step 6: Establish synchronous control between master Axis 6 and slave Axis 7, then move Axis 6 to position 60 ----
# Configure a simple E-CAM table to provide synchronous control.
syncECAM = AdvSync_ECAMData()
ecOptions = AdvSync_ECAMOptions()
ecOptions.type = AdvSync_ECAMType.Repeat
ecOptions.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ecOptions.clutch.type = AdvSync_ECAMClutchType.PyNone
ecOptions.clutch.simpleCatchUpVelocity = 1000
ecOptions.clutch.simpleCatchUpAcc = 10000

syncECAM.masterAxis = 6
syncECAM.slaveAxis = 7
# For a simple synchronous control, define a minimal table with two points.
syncECAM.numPoints = 2
syncECAM.options = ecOptions

syncECAM.SetMasterPos(0, 0)
syncECAM.SetSlavePos(0, 0)
syncECAM.SetMasterPos(1, 60)
syncECAM.SetSlavePos(1, 60)

ret = Wmx3Lib_adv.advSync.StartECAM(0, syncECAM)
if ret != 0:
    print('Error starting synchronous (E-CAM) control between Axis 6 and Axis 7: ' + str(ret))
    # Optionally return or raise an exception

# Now move the master Axis 6 to position 60 under synchronous control.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 900
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('Error starting synchronized motion for Axis 6: ' + str(ret))
Wmx3Lib_cm.motion.Wait(6)

# Stop the synchronous (E-CAM) control.
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('Error stopping synchronous (E-CAM) control: ' + str(ret))
