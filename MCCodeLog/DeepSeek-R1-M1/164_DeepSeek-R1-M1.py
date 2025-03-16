
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()
trig = Trigger()
eventIN_Motion = CoreMotionEventInput()
posCommand = Motion_PosCommand()

# Execute normal motion command for Axis 10
pos.axis = 10
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 600
pos.profile.acc = 10000
pos.profile.dec = 10000
pos.target = 800

ret = Wmx3Lib_cm.motion.StartPos(pos)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute trigger motion command for Axis 10
trig.triggerType = TriggerType.DistanceToTarget
trig.triggerAxis = 10
trig.triggerValue = 200

pos.axis = 10
pos.profile.velocity = 1000
pos.target = 300
pos.trigger = trig

ret = Wmx3Lib_cm.motion.StartPos_Trigger(pos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set up event for Axis 12
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 10
eventIN_Motion.distanceToTarget.distance = 400
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Execute motion command for Axis 12
posCommand.axis = 12
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 80

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to complete
Wmx3Lib_cm.motion.Wait(12)
