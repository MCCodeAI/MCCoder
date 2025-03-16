
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplWithRotationCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
# Create the path interpolation with rotation buffer with velocity 1000
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()
conf.SetAxis(0, 5)  # Map X axis to Axis 5
conf.SetAxis(1, 6)  # Map Y axis to Axis 6
conf.rotationalAxis = 3  # Rotational axis is Axis 3
conf.SetCenterOfRotation(0, 80)  # X center of rotation at 80
conf.SetCenterOfRotation(1, 80)  # Y center of rotation at 80

# Set the motion profile parameters for the rotational axis
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 1000
conf.angleCorrectionProfile.acc = 2000
conf.angleCorrectionProfile.dec = 2000

# Disable rotating the X and Y axes around the center of rotation
conf.disableXYRotationalMotion = 1

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Set Axis 3 (the rotational axis) to single-turn mode with encoder count 360000
ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define the four path points for interpolation
path.numPoints = 4

# Point 0: (160, 0)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)  # Target for Axis 5 (X)
point.SetTarget(1, 0)    # Target for Axis 6 (Y)
path.SetPoint(0, point)

# Point 1: (160, 160)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)
point.SetTarget(1, 160)
path.SetPoint(1, point)

# Point 2: (0, 160)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 0)
point.SetTarget(1, 160)
path.SetPoint(2, point)

# Point 3: (0, 0)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
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

# Execute the path interpolation with rotation (runs continuously through all segments)
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the axes to stop moving after the full motion is executed
Wmx3Lib_cm.motion.Wait(0)
timeoutCounter = 0
pathStatus = AdvMotion_PathIntplWithRotationState()
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplWithRotationState.Idle:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
if timeoutCounter > 500:
    print('PathIntplWithRotation running timeout.')
    return

# Free the path interpolation with rotation buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

sleep(1)
# Turn off single-turn mode on Axis 3
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(3, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
