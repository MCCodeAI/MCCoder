
# Axes = [8]
# IOInputs = []
# IOOutputs = [0.1]

import time

def main():
    # Create EventControl object and IO/Motion event objects.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_IO = IoEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    
    # Event ID for this event.
    posEventID = 5

    # Configure the event input to trigger when IO Output 0.1 equals 0.
    eventIN_IO.type = IoEventInputType.NotIOBit
    eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
    # "0.1" means byte 0 and bit 1.
    eventIN_IO.ioBit.byteAddress = 0
    eventIN_IO.ioBit.bitAddress = 1

    # Configure the relative motion command for Axis 8.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
    eventOut_Motion.startSingleMov.axis = 8
    eventOut_Motion.startSingleMov.type = ProfileType.Trapezoidal
    eventOut_Motion.startSingleMov.target = 130
    eventOut_Motion.startSingleMov.velocity = 1000
    eventOut_Motion.startSingleMov.acc = 10000
    eventOut_Motion.startSingleMov.dec = 10000

    # Set up the event with the Event Control library.
    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

    # Short delay before triggering the event.
    time.sleep(0.01)

    # Create an IO object to trigger the event by setting the output.
    Wmx3Lib_Io = Io(Wmx3Lib)
    # Set IO Output 0.1 to 0 to trigger the event.
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x00, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

    # Wait until Axis 8 stops moving.
    ret = Wmx3Lib_cm.motion.Wait(8)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Remove the event after motion completes.
    ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
