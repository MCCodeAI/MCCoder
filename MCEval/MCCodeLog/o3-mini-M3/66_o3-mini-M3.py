
# -*- coding: utf-8 -*-

from time import sleep

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previously allocated interpolation buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Create the path interpolation with rotation buffer with a motion velocity of 1000.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()
conf.SetAxis(0, 5)  # Map logical X axis to physical Axis 5
conf.SetAxis(1, 6)  # Map logical Y axis to physical Axis 6
conf.rotationalAxis = 3  # Rotational axis is Axis 3
conf.SetCenterOfRotation(0, 80)  # X coordinate of the center of rotation
conf.SetCenterOfRotation(1, 80)  # Y coordinate of the center of rotation

# Setup the rotational axis angle correction motion profile parameters
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 900
conf.angleCorrectionProfile.acc = 1800
conf.angleCorrectionProfile.dec = 1800

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Set the rotational axis (Axis 3) to single-turn mode.
ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Define the path interpolation with rotation command with 4 points.
path = AdvMotion_PathIntplWithRotationCommand()
path.numPoints = 4

# Point 0: Move to (160, 0) with auto smoothing radius of 10.
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 2000
profile.dec = 2000
point.profile = profile
point.SetTarget(0, 160)  # X coordinate (Axis 5)
point.SetTarget(1, 0)    # Y coordinate (Axis 6)
point.autoSmoothRadius = 10
path.SetPoint(0, point)

# Point 1: Move to (160, 160) with auto smoothing radius of 10.
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 2000
profile.dec = 2000
point.profile = profile
point.SetTarget(0, 160)
point.SetTarget(1, 160)
point.autoSmoothRadius = 10
path.SetPoint(1, point)

# Point 2: Move to (0, 160) with auto smoothing radius of 10.
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 2000
profile.dec = 2000
point.profile = profile
point.SetTarget(0, 0)
point.SetTarget(1, 160)
point.autoSmoothRadius = 10
path.SetPoint(2, point)

# Point 3: Move to (0, 0); no auto smoothing is applied after the final segment.
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 2000
profile.dec = 2000
point.profile = profile
point.SetTarget(0, 0)
point.SetTarget(1, 0)
path.SetPoint(3, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Execute the complete continuous path interpolation with rotation.
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Wait for the continuous path interpolation motion to finish.
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
    print('PathIntplWithRotation running timeout!')
    exit(1)

# Free the interpolation buffer.
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

sleep(1)

# Turn off the single-turn mode for the rotational axis (Axis 3)
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(3, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)
