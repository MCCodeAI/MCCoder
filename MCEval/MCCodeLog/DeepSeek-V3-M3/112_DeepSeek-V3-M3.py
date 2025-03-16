
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# 1. Move Axis 2 to position 150
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

Wmx3Lib_cm.motion.StartPos(posCommand)
Wmx3Lib_buf.Wait(2)

# 2. Set an event that triggers a relative position command for Axis 2 with a distance of 260 and a velocity of 1100 when IO Output 1.2 equals 1. The event ID is 5.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()
posEventID = 5

eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.bitAddress = 2
eventIN_IO.ioBit.byteAddress = 1

eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
eventOut_Motion.startSingleMov.axis = 2
eventOut_Motion.startSingleMov.type = ProfileType.Trapezoidal
eventOut_Motion.startSingleMov.target = 260
eventOut_Motion.startSingleMov.velocity = 1100
eventOut_Motion.startSingleMov.acc = 10000
eventOut_Motion.startSingleMov.dec = 10000

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# 3. Execute linear interpolation of Axis 1 and Axis 3 to (80, 110) at a velocity of 1500
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
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_buf.Wait(1)
Wmx3Lib_buf.Wait(3)

# 4. Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it to 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

sleep(0.2)

ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# End Recording
Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

# Wait for the motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 2)
axisSel.SetAxis(2, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Destroy API buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
