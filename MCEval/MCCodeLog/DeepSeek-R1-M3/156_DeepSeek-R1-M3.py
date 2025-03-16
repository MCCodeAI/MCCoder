
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use unique Event IDs for each event
eventIDs = [1, 2]  # First event ID 1, second event ID 2

# Set the event input for the first condition (distance to target 200)
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 10
eventIN_Motion.distanceToTarget.distance = 200

# Configure the first event output (move Axis 10 to 300)
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 10
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 300
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses for the first condition
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventIDs[0])
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(eventIDs[0], 1)

sleep(0.01)

# Start the initial movement of Axis 10 to -800
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = -800
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach -800
Wmx3Lib_cm.motion.Wait(10)

# Now set up the second event for when Axis 10 reaches 100
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Configure the second event output (move Axis 12 to -50)
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.target = -50
eventOut_Motion.startSinglePos.velocity = 1000

# Set input events, output events, and event addresses for the second condition
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventIDs[1])
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(eventIDs[1], 1)

sleep(0.01)

# Wait for Axis 10 to reach 300 (from the first event trigger)
Wmx3Lib_cm.motion.Wait(10)

# Wait for Axis 12 to finish its movement
Wmx3Lib_cm.motion.Wait(12)

# Clean up events
for eventId in eventIDs:
    ret = Wmx3Lib_EventCtl.DisableEvent(eventId, 1)
    if ret != 0:
        print('DisableEvent error code is ' + str(ret))
        return
        
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventId)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret))
        return
