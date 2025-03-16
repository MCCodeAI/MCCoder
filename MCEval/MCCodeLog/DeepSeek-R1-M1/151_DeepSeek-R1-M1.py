
# Axes = [0]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 0

# Set the event input.
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 0
eventIN_Motion.equalPos.pos = 1000

# Stops the motion of Axis 0
eventOut_Motion.type = CoreMotionEventOutputType.StopSingleAxis
eventOut_Motion.stopSingleAxis.axis = 0

# Set input events, output events, and event addresses.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

sleep(0.01)
# Move Axis 0 to 2200
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 2200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(0)

# Move Axis 0 to 2000 with speed 1000 using JerkLimitedFixedVelocityT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(0)

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
