
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create an event to stop Axis 0 when its position equals 1000,
# then move Axis 0 to 2200 (the event will halt the motion when pos==1000),
# and finally move Axis 0 to position 2000 using a JerkLimitedFixedVelocityT profile at 1000 velocity.
#
# Note: After each motion command, wait until the axis stops before continuing.

# ----- Set up event for Axis 0 -----
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use event ID 0.
posEventID = 0

# Set the event input: trigger when Axis 0’s position equals 1000.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 0
eventIN_Motion.equalPos.pos = 1000

# Set the event output: stop the motion of Axis 0.
eventOut_Motion.type = CoreMotionEventOutputType.StopSingleAxis
eventOut_Motion.stopSingleAxis.axis = 0

# Register the event.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    exit()

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Allow a brief period for the event to be armed.
sleep(0.01)

# ----- First Motion: Move Axis 0 to position 2200 -----
# When Axis 0 reaches 1000 along its path to 2200, the event will trigger and stop the motion.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal  # Using a basic profile for the first motion.
posCommand.axis = 0
posCommand.target = 2200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 0 stops (the stop will occur very likely when it reaches pos 1000).
Wmx3Lib_cm.motion.Wait(0)

# Remove the event now that it has served its purpose.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    exit()

# ----- Second Motion: Move Axis 0 to position 2000 using a JerkLimitedFixedVelocityT profile -----
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT  # Using the JerkLimitedFixedVelocityT profile.
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 0 comes to a complete stop after the move.
Wmx3Lib_cm.motion.Wait(0)
