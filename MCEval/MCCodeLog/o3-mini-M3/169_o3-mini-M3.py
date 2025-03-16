
# Axes = [5, 8]
# IOInputs = []
# IOOutputs = []

# ---------------------------------------------------------------------
# 1. Move Axis 5 to 200
# ---------------------------------------------------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error on Axis 5 code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 5 stops moving.
Wmx3Lib_cm.motion.Wait(5)

# ---------------------------------------------------------------------
# 2. Check Axis 5's status for its command position, and if it is 200, then move Axis 5 to 50.
# ---------------------------------------------------------------------
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error on Axis 5 is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

if CmStatus.GetAxesStatus(5).posCmd == 200:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 50
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error on Axis 5 (to 50) code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()
    Wmx3Lib_cm.motion.Wait(5)

# ---------------------------------------------------------------------
# 3. Move Axis 8 to 99 using a TimeAccJerkRatio profile
# ---------------------------------------------------------------------
# The TimeAccJerkRatio profile uses time-based acceleration/deceleration settings.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 8
posCommand.target = 99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error on Axis 8 (TimeAccJerkRatio) code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(8)
