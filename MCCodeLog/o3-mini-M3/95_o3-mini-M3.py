
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 150
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos (move to 150) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 8 stops moving
Wmx3Lib_cm.motion.Wait(8)

# Set Enable Global Starting Velocity to TRUE and Global Starting Velocity to 555 for Axis 8
motionParam = Config_MotionParam()
ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(8)
if ret != 0:
    print('GetMotionParam (Axis 8) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

motionParam.enableGlobalStartingVelocity = True
motionParam.globalStartingVelocity = 555

ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(8, motionParam)
if ret != 0:
    print('SetMotionParam (Axis 8) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Move Axis 8 to 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos (move to 300) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 8 stops moving
Wmx3Lib_cm.motion.Wait(8)
