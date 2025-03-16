
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

# Set the input event to monitor Axis 3’s DistanceToTarget.
# When the remaining distance to the target for Axis 3 reaches (or becomes less than) 500, the event will trigger.
eventIN_Motion = Motion_EventInput()  # Assuming an instance of the input event class.
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 3
eventIN_Motion.distanceToTarget.distance = 500
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Continuously check if the input event is triggered.
# (In a real system, this function would check the hardware/driver status.)
while not Wmx3Lib_cm.motion.IsEventTriggered(eventIN_Motion):
    Wmx3Lib_cm.motion.Wait(0.1)

# Once the event has been triggered, move Axis 1 to position -200 at a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 1
posCommand.target = -200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error on Axis 1: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 1 stops moving.
Wmx3Lib_cm.motion.Wait(1)

# Move Axis 3 to 1200.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 1200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error on Axis 3: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 3 stops moving.
Wmx3Lib_cm.motion.Wait(3)
