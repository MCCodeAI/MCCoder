
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to position 150
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 8
posCommand.target = 150
posCommand.profile.velocity = 1000  # Assuming a default velocity
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to a specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(8)

# Set the Enable Global Starting Velocity parameter of Axis 8 to TRUE
motionParam = Config_MotionParam()
ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(8)
motionParam.enableGlobalStartingVelocity = True
ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(8, motionParam)
if ret != 0:
    print('Set enableGlobalStartingVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set the Global Starting Velocity parameter to 555
motionParam.globalStartingVelocity = 555
ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(8, motionParam)
if ret != 0:
    print('Set globalStartingVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Move Axis 8 to position 300
posCommand.target = 300
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(8)
