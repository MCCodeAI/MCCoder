
import time

# -------------------------------
# 1. Record and execute an API buffer to move Axis 2 to position 150.
# -------------------------------
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
Wmx3Lib_buf.Clear(0)
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
Wmx3Lib_buf.StartRecordBufferChannel(0)

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 2 stops moving before ending the buffer recording.
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print("Wait error code for Axis 2 is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Ensure Axis 2 has completed its motion.
ret = Wmx3Lib_cm.motion.Wait(2)
if ret != 0:
    print("Post-execute wait error for Axis 2: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# -------------------------------
# 2. Set an event that triggers a relative move command for Axis 2.
#    When IO Output 1.2 equals 1, move Axis 2 by 260 (relative) at 1100 velocity.
#    Event ID is 5.
# -------------------------------
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

eventIN_IO = IoEventInput()
# Correction: Use the correct IO event type for matching the bit condition.
eventIN_IO.type = IoEventInputType.IOBit
# Specify the I/O source: Output with byte address 1 and bit address 2 (i.e., Output 1.2).
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.byteAddress = 1
eventIN_IO.ioBit.bitAddress = 2

eventOut_Motion = CoreMotionEventOutput()
# Use the multiple motion command even for a single axis.
eventOut_Motion.type = CoreMotionEventOutputType.StartMultipleMov
eventOut_Motion.startMultipleMov.axisCount = 1
eventOut_Motion.startMultipleMov.SetAxis(0, 2)
eventOut_Motion.startMultipleMov.SetType(0, ProfileType.Trapezoidal)
eventOut_Motion.startMultipleMov.SetVelocity(0, 1100)
# Specify acceleration/deceleration as needed.
eventOut_Motion.startMultipleMov.SetAcc(0, 10000)
eventOut_Motion.startMultipleMov.SetDec(0, 10000)
eventOut_Motion.startMultipleMov.SetTarget(0, 260)

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, 5)
if ret != 0:
    print("SetEvent_ID error code is " + str(ret))
    exit(1)

Wmx3Lib_EventCtl.EnableEvent(5, 1)

# -------------------------------
# 3. Execute linear interpolation of Axis 1 and Axis 3 to (80, 110) at 1500 velocity.
# -------------------------------
lin = Motion_LinearIntplCommand()
lin.axisCount = 2
lin.SetAxis(0, 1)
lin.SetAxis(1, 3)
lin.profile.type = ProfileType.Trapezoidal
lin.profile.velocity = 1500
lin.profile.acc = 10000
lin.profile.dec = 10000
lin.SetTarget(0, 80)
lin.SetTarget(1, 110)

ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
if ret != 0:
    print("StartLinearIntplPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# -------------------------------
# 4. Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it to 0.
# -------------------------------
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)

time.sleep(0.2)

ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)

# -------------------------------------------------------------------
# Additional snippet: 
# Set output bit 0.2 to be 1, sleep for 0.15 seconds, and then set it to 0.
# -------------------------------------------------------------------
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x00, 0x02, 0x01)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)

time.sleep(0.15)

ret = Wmx3Lib_Io.SetOutBit(0x00, 0x02, 0x00)
if ret != 0:
    print("SetOutBit error code is " + str(ret) + ": " + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)
