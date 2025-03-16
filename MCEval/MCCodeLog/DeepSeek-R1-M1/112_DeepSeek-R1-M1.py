
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# 1. Record and execute an API buffer to move Axis 2 to position 150
Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
cond = ApiBufferCondition()

# Clear the buffer of the specified channel
Wmx3Lib_buf.Clear(0)
# Create a buffer for the specified channel
Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
# Start recording for the specified channel
Wmx3Lib_buf.StartRecordBufferChannel(0)

# Add position command to move Axis 2 to position 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.axis = 2

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# End recording
Wmx3Lib_buf.EndRecordBufferChannel()
# Execute the buffer
Wmx3Lib_buf.Execute(0)

# Wait for Axis 2 motion to complete
Wmx3Lib_cm.motion.Wait(2)
# Destroy API buffer resources
Wmx3Lib_buf.Halt(0)
Wmx3Lib_buf.FreeApiBuffer(0)

# 2. Set event for relative position command on Axis 2
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()
posEventID = 5

# Set event input
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.bitAddress = 2
eventIN_IO.ioBit.byteAddress = 1

# Set event output for relative position command
eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
eventOut_Motion.startSingleMov.axis = 2
eventOut_Motion.startSingleMov.profile.type = ProfileType.Trapezoidal
eventOut_Motion.startSingleMov.target = 260
eventOut_Motion.startSingleMov.profile.velocity = 1100
eventOut_Motion.startSingleMov.profile.acc = 10000
eventOut_Motion.startSingleMov.profile.dec = 10000

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# 3. Execute linear interpolation for Axis 1 and Axis 3
eventOut_Motion.type = CoreMotionEventOutputType.LinearIntplMov
eventOut_Motion.linearIntplMov.axisCount = 2
eventOut_Motion.linearIntplMov.SetAxis(0, 1)
eventOut_Motion.linearIntplMov.SetAxis(1, 3)
eventOut_Motion.linearIntplMov.type = ProfileType.Trapezoidal
eventOut_Motion.linearIntplMov.velocity = 1500
eventOut_Motion.linearIntplMov.acc = 10000
eventOut_Motion.linearIntplMov.dec = 10000
eventOut_Motion.linearIntplMov.SetTarget(0, 80)
eventOut_Motion.linearIntplMov.SetTarget(1, 110)

ret = Wmx3Lib_cm.motion.StartLinearIntplMov(eventOut_Motion.linearIntplMov)
if ret != 0:
    print('StartLinearIntplMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for linear interpolation motion to complete
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# 4. Set IO output bit 1.2 to 1, wait, then set to 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 2, 1)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

sleep(0.2)
ret = Wmx3Lib_Io.SetOutBit(0x01, 2, 0)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Remove event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
