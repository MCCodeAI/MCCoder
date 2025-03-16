
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Start an absolute position command for Axis 10 to move to position -800 with a velocity of 600.
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

# Wait for Axis 10 to reach the DistanceToTarget of 200.
while True:
    ret, axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(10)
    if ret != 0:
        print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    if axisStatus.distanceToTarget <= 200:
        break

# Trigger Axis 10 to move to 300 with a velocity of 1000.
trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = 300
trigPosCommand.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 200

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach the position of 100.
while True:
    ret, axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(10)
    if ret != 0:
        print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    if axisStatus.position >= 100:
        break

# Set an event that triggers to start the movement of Axis 12 to -50.
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.GreaterPos
eventIN_Motion.greaterPos.axis = 10
eventIN_Motion.greaterPos.pos = 100

# Move Axis 12 to -50 with a velocity of 500.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 12
posCommand.target = -50
posCommand.profile.velocity = 500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to stop moving.
Wmx3Lib_cm.motion.Wait(12)
