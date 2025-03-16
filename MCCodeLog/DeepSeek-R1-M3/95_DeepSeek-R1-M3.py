
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 150
posCommand.profile.velocity = 1000  # Default velocity
posCommand.profile.acc = 10000     # Default acceleration
posCommand.profile.dec = 10000     # Default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(8)

# Set Enable Global Starting Velocity to TRUE
motionParam = Config_MotionParam()
ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(8)
if ret != 0:
    print('GetMotionParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

motionParam.enableGlobalStartingVelocity = True
ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(8, motionParam)
if ret != 0:
    print('Set enableGlobalStartingVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Global Starting Velocity to 555
motionParam = Config_MotionParam()
ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(8)
if ret != 0:
    print('GetMotionParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

motionParam.globalStartingVelocity = 555
ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(8, motionParam)
if ret != 0:
    print('Set globalStartingVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 8 to 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 300
posCommand.profile.velocity = 1000  # Default velocity
posCommand.profile.acc = 10000     # Default acceleration
posCommand.profile.dec = 10000     # Default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(8)
