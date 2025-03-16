
# Axes = [9]
# IOInputs = []
# IOOutputs = [0.3]

# Create event control, IO event input, and motion event output objects.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_IO = IoEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for the event.
posEventID = 9

# Configure the event input.
# Here we want the event to trigger when IO Output 0.3 equals 0.
# According to the "byte.bit" notation, byte = 0 and bit = 3.
eventIN_IO.type = IoEventInputType.NotIOBit
eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
eventIN_IO.ioBit.byteAddress = 0
eventIN_IO.ioBit.bitAddress = 3

# Configure the event output for an absolute position command.
# This command sets Axis 9 to move to 160 with a velocity of 1000.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 9
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 160
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set the event with the specified input and motion output.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    exit()

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Short sleep before triggering the event.
sleep(0.01)

# Trigger the event by setting the corresponding IO Output.
# For "Output 0.3", we use a mask that represents bit 3.
# Assuming that writing a 0 triggers the "NotIOBit" condition.
Wmx3Lib_Io = Io(Wmx3Lib)
# The mask 0x08 corresponds to bit 3 (binary 00001000).
ret = Wmx3Lib_Io.SetOutBit(0x08, 0x00, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    exit()

# Wait for Axis 9 to complete the motion.
ret = Wmx3Lib_cm.motion.Wait(9)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Remove the event after the motion has completed.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    exit()
