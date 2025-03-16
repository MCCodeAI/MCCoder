
# Axes = [7, 9]
# IOInputs = []
# IOOutputs = [0.7]

# Move Axis 7 to position 220 with a speed of 1500.
posCommand = Motion_PosCommand()
posCommand.axis = 7
posCommand.target = 220
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error starting absolute move on Axis 7: " + str(ret))
# Wait until Axis 7 stops moving.
Wmx3Lib_cm.motion.Wait(7)

# Set IO output bit 0.7 to 1, sleep for 0.2 seconds, then set it to 0.
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x80, 1)  # 0x80 represents bit 7 in byte 0.
if ret != 0:
    print("Error setting IO output 0.7 to 1: " + str(ret))
sleep(0.2)
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x80, 0)
if ret != 0:
    print("Error setting IO output 0.7 to 0: " + str(ret))

# Start an absolute linear interpolation for Axes 7 and 9 to position (200, 50) with a velocity of 1200.
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 7)
lin.SetAxis(1, 9)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1200
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 200)
lin.SetTarget(1, 50)
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print("Error starting absolute linear interpolation on Axes 7 and 9: " + str(ret))
# Wait until Axis 7 and 9 stop.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error waiting for Axes 7 and 9: " + str(ret))

# Start a relative linear interpolation for Axes 7 and 9 to move by (-100, 50).
lin.SetTarget(0, -100)
lin.SetTarget(1, 50)
ret = Wmx3Lib_cm.motion.StartLinearIntplMov(lin)
if ret != 0:
    print("Error starting relative linear interpolation on Axes 7 and 9: " + str(ret))
# Wait until the relative move completes.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error waiting for relative motion on Axes 7 and 9: " + str(ret))

# Start a counterclockwise circular interpolation motion command for Axes 7 and 9.
# The command uses a center position of (50, 50), an arc length of 270 degrees, and a velocity of 1000.
circularCommand = Motion_CenterAndLengthCircularIntplCommand()
circularCommand.SetAxis(0, 7)
circularCommand.SetAxis(1, 9)
circularCommand.SetCenterPos(0, 50)
circularCommand.SetCenterPos(1, 50)
circularCommand.arcLengthDegree = 270
# For counterclockwise, set clockwise flag to 0.
circularCommand.clockwise = 0  
circularCommand.profile.type = ProfileType.Trapezoidal
circularCommand.profile.velocity = 1000
circularCommand.profile.acc = 10000
circularCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circularCommand)
if ret != 0:
    print("Error starting circular interpolation on Axes 7 and 9: " + str(ret))
# Wait until the circular motion completes.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 7)
axisSel.SetAxis(1, 9)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Error waiting for circular motion on Axes 7 and 9: " + str(ret))
