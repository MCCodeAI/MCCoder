# Write python code to Set an event to trigger a relative position command of Axis 0 with 100 distance and 1000 velocity, when Output 1.0 = 0. Event id is 10.
    # Axes = [0]

    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_IO = IoEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    # Event ID
    posEventID = 10
    # RemoveEvent
    Wmx3Lib_EventCtl.RemoveEvent(posEventID)

    eventIN_IO.type = IoEventInputType.NotIOBit
    eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
    eventIN_IO.ioBit.bitAddress = 0
    eventIN_IO.ioBit.byteAddress = 1

    eventOut_Motion.type = CoreMotionEventOutputType.StartSingleMov
    eventOut_Motion.startSingleMov.axis = 0
    eventOut_Motion.startSingleMov.type = ProfileType.Trapezoidal
    eventOut_Motion.startSingleMov.target = 100
    eventOut_Motion.startSingleMov.velocity = 1000
    eventOut_Motion.startSingleMov.acc = 10000
    eventOut_Motion.startSingleMov.dec = 10000

    # Set input events, output events, and event addresses.
    ret,Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return
    # EnableEvent
    Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

    sleep(0.01)
    # Set Output 1.0 = 1 to trigger the motion
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x00, 0x01)
    if ret!=0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)


