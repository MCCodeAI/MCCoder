
# Axes = [8]
# IOInputs = []
# IOOutputs = [0.1]

# Create the event control object and related event input/output objects.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for this event.
posEventID = 5

# Set the event input.
# This event is triggered when IO Output 0.1 equals 0.
# In our API, we use NotIOBit type. For IO Output "0.1", the byte address is 0 and the bit address is 1.
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.byteAddress = 0
eventIN_IO.ioBit.bitAddress = 1

# Set the event output for a single-axis relative motion command.
# Relative move (StartSingleMov) for Axis 8 with a target distance of 130 and a velocity of 1000.
eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
eventOut_Motion.startSingleMov.axis = 8
eventOut_Motion.startSingleMov.target = 130
eventOut_Motion.startSingleMov.velocity = 1000
eventOut_Motion.startSingleMov.acc = 10000
eventOut_Motion.startSingleMov.dec = 10000

# Set the event using the event control object.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    exit(1)

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

sleep(0.01)

# Trigger the event by setting the IO Output.
# Although the event is defined for when IO Output 0.1 equals 0, the API sample always uses SetOutBit to force the transition.
# Here, we simulate the change by setting the bit.
Wmx3Lib_Io = Io(Wmx3Lib)
ret = Wmx3Lib_Io.SetOutBit(0x01, 0x00, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    exit(1)

# Wait until Axis 8 stops moving before proceeding.
ret = Wmx3Lib_cm.motion.Wait(8)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Remove the event to clean up.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    exit(1)
