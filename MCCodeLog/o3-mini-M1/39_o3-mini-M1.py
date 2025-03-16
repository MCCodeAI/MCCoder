
# Axes = [9]
# IOInputs = []
# IOOutputs = [0.3]

import time

def main():
    # Create event control objects.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_IO = IoEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    
    # Use event ID 9.
    posEventID = 9

    # Set the event input: trigger when IO Output 0.3 equals 0.
    # In the "byte.bit" notation, "0.3" means byteAddress = 0 and bitAddress = 3.
    eventIN_IO.type = IoEventInputType.NotIOBit
    eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
    eventIN_IO.ioBit.byteAddress = 0
    eventIN_IO.ioBit.bitAddress = 3

    # Set the event output: an absolute position command for Axis 9.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 9
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = 160
    eventOut_Motion.startSinglePos.velocity = 1000
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    # Set the event with the event command.
    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

    # Wait a short time for the event setup.
    time.sleep(0.01)

    # Trigger the event by setting IO Output 0.3 = 0.
    # In our assumed SetOutBit(byte, bit, value) method, we use:
    #   byte = 0 (from "0.3"), bit = 3, and value = 0.
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x00, 0x03, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

    # Wait until Axis 9 stops moving.
    ret = Wmx3Lib_cm.motion.Wait(9)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Remove the event once motion is complete.
    ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
