
# Axes = [6, 7, 8]
# IOInputs = []
# IOOutputs = [6.7]

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# 1. Move Axis 6 to 20 with velocity 900 using trapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 20
posCommand.profile.velocity = 900
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(6)

# 2. Set IO output bit 6.7 to 1, sleep, then set to 0
Wmx3Lib.io.SetBit(6, 7, 1)
sleep(0.1)
Wmx3Lib.io.SetBit(6, 7, 0)

# 3. Move Axis 7 to 30
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 30
posCommand.profile.velocity = 1000  # Default velocity
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(7)

# 4. Linearly interpolate Axis 7 and 8 to (40, 50)
linIntplCommand = Motion_LinIntplCommand()
linIntplCommand.SetAxis(0, 7)
linIntplCommand.SetAxis(1, 8)
linIntplCommand.SetTargetPos(0, 40)
linIntplCommand.SetTargetPos(1, 50)
linIntplCommand.profile.type = ProfileType.Trapezoidal
linIntplCommand.profile.velocity = 1000
linIntplCommand.profile.acc = 10000
linIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartLinIntplPos(linIntplCommand)
if ret != 0:
    print('StartLinIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(7)
Wmx3Lib_cm.motion.Wait(8)

# 5. Start clockwise circular interpolation for Axis 6 and 7
circIntplCommand = Motion_CircIntplCommand()
circIntplCommand.SetAxis(0, 6)
circIntplCommand.SetAxis(1, 7)
circIntplCommand.SetCenterPos(0, 50)
circIntplCommand.SetCenterPos(1, 50)
circIntplCommand.clockwise = 1
circIntplCommand.arcLengthDegree = 360
circIntplCommand.profile.type = ProfileType.Trapezoidal
circIntplCommand.profile.velocity = 1000
circIntplCommand.profile.acc = 10000
circIntplCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartCircIntplPos(circIntplCommand)
if ret != 0:
    print('StartCircIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for circular motion to complete
Wmx3Lib_cm.motion.Wait(6)
Wmx3Lib_cm.motion.Wait(7)

# 6. Establish synchronous control between Axis 6 and 7
syncData = AdvSync_SyncData()
syncData.masterAxis = 6
syncData.slaveAxis = 7
syncData.type = AdvSync_SyncType.Position

ret = Wmx3Lib_adv.advSync.StartSync(0, syncData)
if ret != 0:
    print('StartSync error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Move Axis 6 to 60
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(6)

# Stop synchronous control
ret = Wmx3Lib_adv.advSync.StopSync(0)
if ret != 0:
    print('StopSync error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
