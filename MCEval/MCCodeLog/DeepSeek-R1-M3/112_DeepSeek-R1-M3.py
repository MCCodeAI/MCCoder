
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# Task 1: API buffer for Axis 2 movement
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

# Add command to buffer (assuming API appends commands during recording)
Wmx3Lib_cm.motion.StartPos(posCommand)  # Verify if this is buffer-safe
Wmx3Lib_buf.WaitAxisIdle(2)  # Wait for Axis 2 to idle in buffer

Wmx3Lib_buf.EndRecordBufferChannel()
Wmx3Lib_buf.Execute(0)

axisSel = AxisSelection()
axisSel.axisCount = 1
axisSel.SetAxis(0, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Task 2: Set event for relative position command (trigger on rising edge)
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()

eventIN_IO.type = IoEventInputType.IOBitRisingEdge  # Corrected to rising edge
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.byteAddress = 1
eventIN_IO.ioBit.bitAddress = 2

eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
eventOut_Motion.startSingleMov.axis = 2
eventOut_Motion.startSingleMov.type = ProfileType.Trapezoidal
eventOut_Motion.startSingleMov.relative = 1
eventOut_Motion.startSingleMov.target = 260
eventOut_Motion.startSingleMov.velocity = 1100
eventOut_Motion.startSingleMov.acc = 10000
eventOut_Motion.startSingleMov.dec = 10000

ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, 5)
if ret != 0:
    print(f'SetEvent_ID error: {ret}')
    return
Wmx3Lib_EventCtl.EnableEvent(5, 1)

# Task 3: Linear interpolation for Axis 1 & 3
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
    print(f'StartLinearIntplPos error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Task 4: IO Output sequence
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)  # Set 1.2 to 1
if ret != 0:
    print(f'SetOutBit error: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
    return

sleep(0.2)

ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)  # Set 1.2 to 0
if ret != 0:
    print(f'SetOutBit error: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
    return

# Wait for Axis 2 to complete event-triggered motion
axisSel.axisCount = 1
axisSel.SetAxis(0, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    return

# Cleanup
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)
ret = Wmx3Lib_EventCtl.RemoveEvent(5)
if ret != 0:
    print(f'RemoveEvent error: {ret}')
