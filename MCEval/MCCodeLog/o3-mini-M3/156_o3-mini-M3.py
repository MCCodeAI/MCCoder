
# -*- coding: utf-8 -*-
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# This script executes an absolute triggered position command for Axis 10
# and sets an event so that when Axis 10 reaches position 100 it triggers 
# an absolute move for Axis 12.
#
# The motion sequence is as follows:
# 1. Before starting Axis 10’s move, set up an event so that when Axis 10 equals 100,
#    Axis 12 will move to -50 (using a trapezoidal profile).
# 2. Start Axis 10 moving to -800 at a velocity of 600.
# 3. When the remaining distance for Axis 10 equals 200, it is triggered to move 
#    to 300 at 1000 velocity.
# 4. Wait until Axis 10 has finished its continuous motion.
# 5. Then wait until the event-triggered move for Axis 12 is complete.
# 6. Finally, clear the event.

# --- Set up the event for Axis 12 ---

# Create an instance of the event control object.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Choose an event ID that is not currently in use (use 2 instead of 1 to avoid conflict).
eventID = 2

# Configure the event input: trigger when Axis 10 equals 100.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Configure the event output: when triggered, start an absolute position command for Axis 12.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -50
# Using a chosen velocity value for Axis 12; adjust as needed.
eventOut_Motion.startSinglePos.velocity = 600
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set the event with the chosen event ID.
ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print("SetEvent_ID error code:", ret)
    # Depending on requirements, you might clear the old event or try a different ID.

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# --- Execute the absolute triggered position command for Axis 10 ---

posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()

# Configure the primary motion for Axis 10: move to -800 at velocity 600.
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
# End velocity set equal to velocity for a clean stop.
posCommand.profile.endVelocity = 600
posCommand.target = -800

# Start the primary move for Axis 10.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Axis 10 StartPos error code:", ret)
    # Handle error as needed

# Configure the triggered motion for Axis 10: when the remaining distance equals 200,
# trigger a move to 300 at velocity 1000.
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger.triggerType = TriggerType.RemainingDistance
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 200

# Start the triggered motion command for Axis 10.
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print("Axis 10 StartPos_Trigger error code:", ret)
    # Handle error as needed

# Wait until Axis 10 has completed its motion.
Wmx3Lib_cm.motion.Wait(10)

# --- Wait for the event-triggered motion of Axis 12 to finish ---

Wmx3Lib_cm.motion.Wait(12)

# --- Clear the event now that the triggered motion is complete ---

ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
if ret != 0:
    print("RemoveEvent error code:", ret)
    # Handle error as needed
