
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Set an event that will stop Axis 0 when it reaches position 1000.
# Then move Axis 0 to 2200 (the event will trigger when Axis 0 reaches position 1000,
# causing an immediate stop). After that, move Axis 0 to position 2000 at 1000 velocity
# using the JerkLimitedFixedVelocityT profile.

# Assume that objects and classes such as EventControl, CoreMotionEventInput, CoreMotionEventOutput,
# CoreMotionEventInputType, CoreMotionEventOutputType, Motion_PosCommand, ProfileType,
# Wmx3Lib, Wmx3Lib_cm, etc. are already defined and available.

# Create the event controller objects
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for this event
posEventID = 0

# Configure the event input:
# When Axis 0 equals position 1000, the event is triggered.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 0
eventIN_Motion.equalPos.pos = 1000

# Configure the event output:
# On trigger, stop the motion of Axis 0.
eventOut_Motion.type = CoreMotionEventOutputType.StopSingleAxis
eventOut_Motion.stopSingleAxis.axis = 0

# Register the event.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    exit(1)

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# A short pause before commanding motion.
sleep(0.01)

# --- First Motion Command: Move Axis 0 to 2200 ---
# Due to the event, as Axis 0 moves, when it reaches position 1000 it will be stopped.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal  # Use a normal profile command.
posCommand.axis = 0
posCommand.target = 2200
# For this move, use default speed/acceleration values (if not specified, we assume defaults)
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 0 stops moving.
Wmx3Lib_cm.motion.Wait(0)

# Remove the event since it has served its purpose.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# --- Second Motion Command: Move Axis 0 to 2000 using a JerkLimitedFixedVelocityT profile ---
# Here, even though the starting position may be 1000 (if the event stopped it there),
# we command an absolute move to 2000 with a fixed velocity profile that limits jerk.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT  # Specify the JerkLimited fixed velocity profile.
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
# Acceleration and deceleration values are set as in previous commands; they may be ignored by the profile if not needed.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 0 completes the motion.
Wmx3Lib_cm.motion.Wait(0)
