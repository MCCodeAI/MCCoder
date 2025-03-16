
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Define the event input for Axis 10 to trigger Axis 12 when Axis 10 reaches position 400
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Execute an absolute position command for Axis 10 to move to position 800 with a velocity of 600
posCommand_Axis10 = Motion_PosCommand()
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000
posCommand_Axis10.target = 800

ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach position 400 to trigger Axis 12
while True:
    ret, axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(10)
    if ret != 0:
        print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    if axisStatus.pos == 400:
        break

# Trigger Axis 12 to move to position 80
posCommand_Axis12 = Motion_PosCommand()
posCommand_Axis12.axis = 12
posCommand_Axis12.profile.type = ProfileType.Trapezoidal
posCommand_Axis12.profile.velocity = 1000
posCommand_Axis12.profile.acc = 10000
posCommand_Axis12.profile.dec = 10000
posCommand_Axis12.target = 80

ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis12)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to stop moving
Wmx3Lib_cm.motion.Wait(12)

# Execute an absolute triggered position command for Axis 10 when the distance to target is 200
trigPosCommand_Axis10 = Motion_TriggerPosCommand()
trigPosCommand_Axis10.axis = 10
trigPosCommand_Axis10.profile.type = ProfileType.Trapezoidal
trigPosCommand_Axis10.profile.velocity = 1000
trigPosCommand_Axis10.profile.acc = 10000
trigPosCommand_Axis10.profile.dec = 10000
trigPosCommand_Axis10.target = 300

trigger = Trigger()
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerValue = 200

trigPosCommand_Axis10.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to stop moving
Wmx3Lib_cm.motion.Wait(10)
