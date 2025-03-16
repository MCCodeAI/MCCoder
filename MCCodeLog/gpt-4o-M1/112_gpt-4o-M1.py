
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# Initialize the necessary objects for event control and IO operations
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 5

# Step 1: Move Axis 2 to position 150
posCommand = Motion_PosCommand()
posCommand.axis = 2
posCommand.target = 150
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the move command
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 to stop moving
Wmx3Lib_cm.motion.Wait(2)

# Step 2: Set an event for a relative position command for Axis 2
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.bitAddress = 2
eventIN_IO.ioBit.byteAddress = 1

eventOut_Motion.type = CoreMotionEventOutputType.StartMultipleMov
eventOut_Motion.startMultipleMov.axisCount = 1
eventOut_Motion.startMultipleMov.SetAxis(0, 2)
eventOut_Motion.startMultipleMov.SetType(0, ProfileType.Trapezoidal)
eventOut_Motion.startMultipleMov.SetVelocity(0, 1100)
eventOut_Motion.startMultipleMov.SetAcc(0, 10000)
eventOut_Motion.startMultipleMov.SetDec(0, 10000)
eventOut_Motion.startMultipleMov.SetTarget(0, 260)

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Step 3: Execute linear interpolation of Axis 1 and Axis 3 to (80, 110)
eventOut_Motion.type = CoreMotionEventOutputType.LinearIntplPos
eventOut_Motion.linearIntplPos.axisCount = 2
eventOut_Motion.linearIntplPos.SetAxis(0, 1)
eventOut_Motion.linearIntplPos.SetAxis(1, 3)
eventOut_Motion.linearIntplPos.type = ProfileType.Trapezoidal
eventOut_Motion.linearIntplPos.velocity = 1500
eventOut_Motion.linearIntplPos.acc = 10000
eventOut_Motion.linearIntplPos.dec = 10000
eventOut_Motion.linearIntplPos.SetTarget(0, 80)
eventOut_Motion.linearIntplPos.SetTarget(1, 110)

# Execute the linear interpolation command
ret = Wmx3Lib_cm.motion.StartLinearIntplPos(eventOut_Motion.linearIntplPos)
if ret != 0:
    print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 and Axis 3 to stop moving
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Step 4: Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it to 0
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Wait for 0.2 seconds
sleep(0.2)

# Set IO output bit 1.2 to 0
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
