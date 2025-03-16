
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplWithRotationCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
# Create the path interpolation with rotation buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()

conf.SetAxis(0, 5)  # X axis
conf.SetAxis(1, 6)  # Y axis
conf.rotationalAxis = 3  # Rotational axis
conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position

# Rotational axis angle correction motion profile parameters
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 1000
conf.angleCorrectionProfile.acc = 2000
conf.angleCorrectionProfile.dec = 2000

# Enable rotating the X and Y axes around the center of rotation
conf.disableXYRotationalMotion = 0

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set Axis 3 to single-turn mode, single-turn encoder count 360. Single-turn mode is necessary for rotation axis in path interpolation with rotation function.
ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Add the path interpolation with rotation commands
path.numPoints = 4

point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)
point.SetTarget(1, 0)
point.autoSmoothRadius = 10  # Auto smoothing radius
path.SetPoint(0, point)

point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)
point.SetTarget(1, 160)
point.autoSmoothRadius = 10  # Auto smoothing radius
path.SetPoint(1, point)

point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 0)
point.SetTarget(1, 160)
point.autoSmoothRadius = 10  # Auto smoothing radius
path.SetPoint(2, point)

point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 0)
point.SetTarget(1, 0)
point.autoSmoothRadius = 10  # Auto smoothing radius
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with rotation
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(0)
timeoutCounter = 0
# Wait until the path interpolation with rotation is in Idle state
pathStatus = AdvMotion_PathIntplWithRotationState()
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
while True:
    if (pathStatus.state == AdvMotion_PathIntplWithRotationState.Idle):
        break
    sleep(0.1)
    timeoutCounter = timeoutCounter + 1
    if (timeoutCounter > 500):
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
if (timeoutCounter > 500):
    print('PathIntplWithRotation Running timeout!')
    return

# Free the path interpolation with rotation buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Turn off Axis 3 single-turn mode.
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(3, False)

ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
