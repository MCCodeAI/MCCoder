
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

def main():
    # ---------------------------------------------------------------------------
    # 1. Start absolute position command on Axis 10:
    #    Move Axis 10 to position -1000 with a velocity of 600.
    posCommand = Motion_PosCommand()
    posCommand.axis = 10
    posCommand.target = -1000
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 600
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.endVelocity = 600

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos (Axis 10 to -1000) error code:", ret)
        return

    # Wait until Axis 10 finishes the motion.
    Wmx3Lib_cm.motion.Wait(10)

    # ---------------------------------------------------------------------------
    # 2. Configure a triggered motion command for Axis 10:
    #    When the remaining distance for Axis 10 becomes 500, trigger a move 
    #    to position -500 with a velocity of 1000.
    trigCommand = Motion_TriggerPosCommand()
    trigCommand.axis = 10
    trigCommand.target = -500
    trigCommand.profile.type = ProfileType.Trapezoidal
    trigCommand.profile.velocity = 1000
    trigCommand.profile.acc = 10000
    trigCommand.profile.dec = 10000

    # Set trigger condition: use RemainingDistance trigger when it equals 500.
    trigCommand.trigger.triggerType = TriggerType.RemainingDistance
    trigCommand.trigger.triggerAxis = 10
    trigCommand.trigger.triggerValue = 500

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCommand)
    if ret != 0:
        print("StartPos_Trigger (Axis 10 to -500) error code:", ret)
        return

    # Note: Do not wait here because this triggered motion is part of a continuous sequence.

    # ---------------------------------------------------------------------------
    # 3. Set an event that triggers a motion for Axis 2:
    #    When Axis 10 reaches the absolute position of 100, start a motion command 
    #    to move Axis 2 to -200 with a velocity of 1000.
    #
    # Create the event input condition (EqualPos).
    eventIn = CoreMotionEventInput()
    eventIn.inputFunction = CoreMotionEventInputType.EqualPos
    eventIn.equalPos.axis = 10
    eventIn.equalPos.pos = 100

    # Create the event output action (StartPos for Axis 2).
    eventOut = CoreMotionEventOutput()
    eventOut.type = CoreMotionEventOutputType.StartPos
    eventOut.startPos.axis = 2
    eventOut.startPos.target = -200
    eventOut.startPos.profile.type = ProfileType.Trapezoidal
    eventOut.startPos.profile.velocity = 1000
    eventOut.startPos.profile.acc = 10000
    eventOut.startPos.profile.dec = 10000
    eventOut.startPos.profile.endVelocity = 1000

    # Pick an event ID (for example, 1).
    eventID = 1

    ret, returnedEventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIn, eventOut, eventID)
    if ret != 0:
        print("SetEvent_ID error code:", ret)
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # Now wait for the continuous motion chain on Axis 10 to complete.
    Wmx3Lib_cm.motion.Wait(10)

    # Optionally, clean up: remove the event once done.
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("RemoveEvent error code:", ret)
        return

if __name__ == "__main__":
    main()
