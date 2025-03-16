
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = []

# Set the input event to monitor if the CompletedTime of Axis 3's movement is 300ms.
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.CompletedTime
eventIN_Motion.completedTime.axis = 3
eventIN_Motion.completedTime.timeMilliseconds = 300
eventIN_Motion.completedTime.disableIdleAxisTrigger = 1

# Define the event output to move Axis 1 to position 300 at a speed of 1000.
eventOut_Motion = CoreMotionEventOutput()
eventOut_Motion.type = CoreMotionEventOutputType.PosCommand
eventOut_Motion.posCommand.axis = 1
eventOut_Motion.posCommand.target = 300
eventOut_Motion.posCommand.profile.velocity = 1000
eventOut_Motion.posCommand.profile.acc = 10000
eventOut_Motion.posCommand.profile.dec = 10000

# Set the event ID and enable the event.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, 0)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(0, 1)

# Move Axis 3 and Axis 2 to position 2000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

posCommand.axis = 2
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 2 and Axis 3 to stop moving.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 2)
axisSel.SetAxis(1, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 1 to stop moving after the event triggers.
Wmx3Lib_cm.motion.Wait(1)

# Remove the event after completion.
ret = Wmx3Lib_EventCtl.RemoveEvent(0)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
