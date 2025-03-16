
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use unique event IDs to avoid conflicts
eventID1 = 100  # Changed from 1 to avoid conflict
eventID2 = 200  # Changed from 2 to avoid conflict

# First event: Trigger when Axis 10 is 200 units away from target
eventIN_Distance = CoreMotionEventInput()
eventIN_Distance.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Distance.distanceToTarget.axis = 10
eventIN_Distance.distanceToTarget.distance = 200

eventOut_Position = CoreMotionEventOutput()
eventOut_Position.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Position.startSinglePos.axis = 10
eventOut_Position.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Position.startSinglePos.target = 300
eventOut_Position.startSinglePos.velocity = 1000
eventOut_Position.startSinglePos.acc = 10000
eventOut_Position.startSinglePos.dec = 10000

# Set up first event
ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Distance, eventOut_Position, eventID1)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable first event
Wmx3Lib_EventCtl.EnableEvent(eventID1, 1)

# Second event: Trigger when Axis 10 reaches position 100
eventIN_Position = CoreMotionEventInput()
eventIN_Position.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Position.equalPos.axis = 10
eventIN_Position.equalPos.pos = 100

eventOut_Axis12 = CoreMotionEventOutput()
eventOut_Axis12.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Axis12.startSinglePos.axis = 12
eventOut_Axis12.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Axis12.startSinglePos.target = -50
eventOut_Axis12.startSinglePos.velocity = 1000
eventOut_Axis12.startSinglePos.acc = 10000
eventOut_Axis12.startSinglePos.dec = 10000

# Set up second event
ret, _ = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Position, eventOut_Axis12, eventID2)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable second event
Wmx3Lib_EventCtl.EnableEvent(eventID2, 1)

# Start initial position command for Axis 10
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

# Wait for Axis 10 to complete initial movement
Wmx3Lib_cm.motion.Wait(10)

# Wait for Axis 10 to reach position 100 and trigger Axis 12 movement
Wmx3Lib_cm.motion.Wait(10)

# Remove events after they're no longer needed
ret = Wmx3Lib_EventCtl.RemoveEvent(eventID1)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret))
    return

ret = Wmx3Lib_EventCtl.RemoveEvent(eventID2)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret))
    return
