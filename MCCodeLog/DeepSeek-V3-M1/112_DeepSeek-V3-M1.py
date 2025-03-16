
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = [1.2]

# Move Axis 2 to position 150
Wmx3Lib_cm = CoreMotion(Wmx3Lib)
posCommand = Motion_PosCommand()
posCommand.axis = 2
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 to stop moving
Wmx3Lib_cm.motion.Wait(2)

# Set an event that triggers a relative position command for Axis 2 with a distance of 260 and a velocity of 1100 when IO Output 1.2 equals 1. The event ID is 5.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()
posEventID = 5

# Set the event input
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.bitAddress = 2
eventIN_IO.ioBit.byteAddress = 1

# Set the event output
eventOut_Motion.type = CoreMotionEventOutputType.StartMov
eventOut_Motion.startMov.axis = 2
eventOut_Motion.startMov.type = ProfileType.Trapezoidal
eventOut_Motion.startMov.velocity = 1100
eventOut_Motion.startMov.acc = 10000
eventOut_Motion.startMov.dec = 10000
eventOut_Motion.startMov.target = 260

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Execute linear interpolation of Axis 1 and Axis 3 to (80, 110) at a velocity of 1500
linIntplCommand = Motion_LinearIntplCommand()
linIntplCommand.axisCount = 2
linIntplCommand.SetAxis(0, 1)
linIntplCommand.SetAxis(1, 3)
linIntplCommand.profile.type = ProfileType.Trapezoidal
linIntplCommand.profile.velocity = 1500
linIntplCommand.profile.acc = 10000
linIntplCommand.profile.dec = 10000
linIntplCommand.SetTarget(0, 80)
linIntplCommand.SetTarget(1, 110)

ret = Wmx3Lib_cm.motion.StartLinearIntpl(linIntplCommand)
if ret != 0:
    print('StartLinearIntpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
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

# Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it to 0
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

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
