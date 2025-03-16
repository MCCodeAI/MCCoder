
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplWithRotationCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)

ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

conf = AdvMotion_PathIntplWithRotationConfiguration()

conf.SetAxis(0, 5)  # X axis
conf.SetAxis(1, 6)  # Y axis
conf.rotationalAxis = 3  # Rotational axis
conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position

conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 900
conf.angleCorrectionProfile.acc = 1800
conf.angleCorrectionProfile.dec = 1800

conf.disableXYRotationalMotion = 0  # Enable rotating X and Y axes

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

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
point.autoSmoothRadius = 10
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
point.autoSmoothRadius = 10
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
point.autoSmoothRadius = 10
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
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

timeoutCounter = 0
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
    print('PathIntplWithRotation Running timeout.!')
    return

ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(3, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
