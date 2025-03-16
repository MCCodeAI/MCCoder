
# Axes = [8]
# IOInputs = []
# IOOutputs = [0.1]

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()
# Event ID
posEventID = 5

# Set the event input.
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.bitAddress = 1
eventIN_IO.ioBit.byteAddress = 0

# Starts a position command for which a relative target position is specified.
eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
eventOut_Motion.startSingleMov.axis = 8
eventOut_Motion.startSingleMov.type = ProfileType.Trapezoidal
eventOut_Motion.startSingleMov.target = 130
eventOut_Motion.startSingleMov.velocity = 1000
eventOut_Motion.startSingleMov.acc = 10000
eventOut_Motion.startSingleMov.dec = 10000

# Remove any existing event with the same ID to avoid conflicts.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0 and ret != 90117:  # Ignore error if the event ID was not defined
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return

# Set input events, output events, and event addresses.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

sleep(0.01)
# Set Output 0.1 = 0 to trigger the motion
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x00, 0x01, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(8)

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
