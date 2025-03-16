
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

def main():
    # -------------------------------
    # Step 1: Configure an event so that when Axis 10 reaches position 100,
    #         Axis 12 will start an absolute move to -50.
    # -------------------------------
    # Create an event control object (assumes Wmx3Lib is already available).
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN = CoreMotionEventInput()
    eventOUT = CoreMotionEventOutput()
    # Change the eventID to avoid the "IDInUse" error. Using 2 instead of 1.
    eventID = 2

    # Set the event input: When Axis 10's position equals 100.
    eventIN.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN.equalPos.axis = 10
    eventIN.equalPos.pos = 100

    # Set the event output: Start an absolute position command on Axis 12.
    eventOUT.type = CoreMotionEventOutputType.StartSinglePos
    eventOUT.startSinglePos.axis = 12
    eventOUT.startSinglePos.type = ProfileType.Trapezoidal
    eventOUT.startSinglePos.target = -50
    eventOUT.startSinglePos.velocity = 1000
    eventOUT.startSinglePos.acc = 10000
    eventOUT.startSinglePos.dec = 10000

    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN, eventOUT, eventID)
    if ret != 0:
        print('SetEvent_ID error code is', ret)
        return
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # -------------------------------
    # Step 2: Execute Axis 10 absolute triggered position command.
    #         First, command Axis 10 to move to -800 at 600 velocity.
    #         Then, when its remaining distance equals 400, trigger a new command
    #         for Axis 10 to move to 300 at 1000 velocity.
    #         (Do not call a wait() function in between these two commands.)
    # -------------------------------
    # Start the first (absolute) motion command for Axis 10.
    posCommand = Motion_PosCommand()
    posCommand.axis = 10
    posCommand.target = -800
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 600
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

    # Immediately set up the triggered command for Axis 10.
    trigCommand = Motion_TriggerPosCommand()
    trigCommand.axis = 10
    trigCommand.target = 300
    trigCommand.profile.type = ProfileType.Trapezoidal
    trigCommand.profile.velocity = 1000
    trigCommand.profile.acc = 10000
    trigCommand.profile.dec = 10000

    # Configure the trigger: When the remaining distance of Axis 10 equals 400.
    trig = Trigger()
    trig.triggerAxis = 10
    trig.triggerType = TriggerType.RemainingDistance
    trig.triggerValue = 400
    trigCommand.trigger = trig

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCommand)
    if ret != 0:
        print('StartPos_Trigger error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

    # -------------------------------
    # Step 3: Wait for the motions of each axis to complete.
    #         (Wait for the complete continuous motion of Axis 10,
    #         and then wait (blocking) for the event-triggered move on Axis 12.)
    # -------------------------------
    # Wait for Axis 10 to finish its triggered motion sequence.
    axisSel10 = AxisSelection()
    axisSel10.axisCount = 1
    axisSel10.SetAxis(0, 10)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel10)
    if ret != 0:
        print('Wait_AxisSel error code for Axis 10 is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 12 to finish the event-triggered motion.
    axisSel12 = AxisSelection()
    axisSel12.axisCount = 1
    axisSel12.SetAxis(0, 12)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel12)
    if ret != 0:
        print('Wait_AxisSel error code for Axis 12 is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
        return

    # -------------------------------
    # Step 4: Remove the event after the motion is complete.
    # -------------------------------
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print('RemoveEvent error code is', ret)
        return

if __name__ == "__main__":
    main()
