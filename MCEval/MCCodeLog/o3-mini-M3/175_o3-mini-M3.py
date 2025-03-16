
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # -------------------------------
    # Part A:
    # Set an event so that when Axis 10 reaches position 400,
    # Axis 12 is triggered to move to position 80.
    # -------------------------------
    
    # Create event control objects for core motion event
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    eventID = 0

    # Set the event input: trigger when Axis 10 equals 400.
    eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN_Motion.equalPos.axis = 10
    eventIN_Motion.equalPos.pos = 400

    # Set the event output: when triggered, execute an absolute position command for Axis 12.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 12
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = 80
    eventOut_Motion.startSinglePos.velocity = 1000
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    # Register the event.
    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print("SetEvent_ID error code is", ret)
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # To trigger the event, command Axis 10 to move to position 400.
    posCmd1 = Motion_PosCommand()
    posCmd1.axis = 10
    posCmd1.profile.type = ProfileType.Trapezoidal
    posCmd1.target = 400
    posCmd1.profile.velocity = 500
    posCmd1.profile.acc = 10000
    posCmd1.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCmd1)
    if ret != 0:
        print("StartPos error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for both Axis 10 (the triggering axis) and Axis 12 (the triggered axis) to complete their motions.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 10)
    axisSel.SetAxis(1, 12)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Remove the event after use.
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("RemoveEvent error code is", ret)
        return

    # -------------------------------
    # Part B:
    # Execute an absolute triggered position command.
    # First, command Axis 10 to move to position 800 with a velocity of 600.
    # Then, set a trigger: when the distance remaining for Axis 10 to its target is 200,
    # trigger it to move to position 300 with a velocity of 1000.
    # -------------------------------

    # Start the normal (absolute) position command for Axis 10.
    posCmd2 = Motion_PosCommand()
    posCmd2.axis = 10
    posCmd2.profile.type = ProfileType.Trapezoidal
    posCmd2.target = 800
    posCmd2.profile.velocity = 600
    posCmd2.profile.acc = 10000
    posCmd2.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCmd2)
    if ret != 0:
        print("StartPos error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Set the triggered position command for Axis 10.
    trigPosCmd = Motion_TriggerPosCommand()
    trigPosCmd.axis = 10
    trigPosCmd.profile.type = ProfileType.Trapezoidal
    trigPosCmd.target = 300
    trigPosCmd.profile.velocity = 1000
    trigPosCmd.profile.acc = 10000
    trigPosCmd.profile.dec = 10000

    # Set the trigger condition: when the distance to target for Axis 10 is 200.
    trigPosCmd.trigger.triggerType = TriggerType.DistanceToTarget
    trigPosCmd.trigger.triggerAxis = 10
    trigPosCmd.trigger.triggerValue = 200

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCmd)
    if ret != 0:
        print("StartPos_Trigger error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 10 completes all motions.
    ret = Wmx3Lib_cm.motion.Wait(10)
    if ret != 0:
        print("Wait error code is", ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    print("All motions completed successfully.")

if __name__ == "__main__":
    main()
