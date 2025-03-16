
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

def main():
    # -------------------------------
    # Absolute Triggered Position Command for Axis 10
    # Start an absolute position command to move Axis 10 to -1000 with velocity 600.
    # Then, when the remaining distance of Axis 10 equals 500, trigger it to move to -300 with velocity 1000.
    # -------------------------------
    posCommand = Motion_PosCommand()
    posCommand.axis = 10
    posCommand.target = -1000
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 600
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 10 stops moving.
    Wmx3Lib_cm.motion.Wait(10)

    # Set up the triggered command for Axis 10.
    tgrPosCommand = Motion_TriggerPosCommand()
    tgrPosCommand.axis = 10
    tgrPosCommand.target = -300
    tgrPosCommand.profile.type = ProfileType.Trapezoidal
    tgrPosCommand.profile.velocity = 1000
    tgrPosCommand.profile.acc = 10000
    tgrPosCommand.profile.dec = 10000

    # Trigger when the remaining distance of Axis 10 equals 500.
    trigger = Trigger()
    trigger.triggerAxis = 10
    trigger.triggerType = TriggerType.RemainingDistance
    trigger.triggerValue = 500
    tgrPosCommand.trigger = trigger

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(tgrPosCommand)
    if ret != 0:
        print("StartPos_Trigger error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 10 completes the triggered motion.
    Wmx3Lib_cm.motion.Wait(10)

    # -------------------------------
    # Event Setup: When Axis 10 reaches position 100, trigger Axis 2 to move to -200.
    # -------------------------------
    # Create an event with event ID 0.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    eventID = 0

    # Set the event input: trigger when Axis 10 equals position 100.
    eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN_Motion.equalPos.axis = 10
    eventIN_Motion.equalPos.pos = 100

    # Set the event output: start an absolute position command for Axis 2 to move to -200.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 2
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = -200
    eventOut_Motion.startSinglePos.velocity = 1000
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print("SetEvent_ID error code: " + str(ret))
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # For demonstration purposes, command Axis 10 to move to position 100.
    posCommand = Motion_PosCommand()
    posCommand.axis = 10
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 10 stops moving.
    Wmx3Lib_cm.motion.Wait(10)

    # The event should have triggered the movement of Axis 2.
    # Wait until Axis 2 completes its motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 1
    axisSel.SetAxis(0, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Remove the event.
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("RemoveEvent error code: " + str(ret) + ": " + WMX3Log.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
