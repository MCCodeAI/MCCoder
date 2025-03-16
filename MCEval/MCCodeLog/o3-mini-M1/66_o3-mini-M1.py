
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

from time import sleep

# Instantiate the advanced motion controller interface
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a new path interpolation with rotation command instance
path = AdvMotion_PathIntplWithRotationCommand()

# Free any existing path interpolation with rotation buffer (buffer index 0)
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
# Create the path interpolation with rotation buffer with a velocity of 1000
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with rotation channel.
# X and Y axes will be driven by Axis 5 and Axis 6, respectively.
# The rotational axis is Axis 3.
conf = AdvMotion_PathIntplWithRotationConfiguration()
conf.SetAxis(0, 5)  # X axis is Axis 5
conf.SetAxis(1, 6)  # Y axis is Axis 6
conf.rotationalAxis = 3  # Rotation about Axis 3

# Set the global center of rotation to (80, 80)
conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position

# Enable rotating the X and Y axes around the center of rotation.
# Also enable auto smoothing; the smoothing radius will be applied per segment.
conf.enableAutoSmooth = 1

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Set the rotational axis (Axis 3) to single-turn mode with an encoder count of 360,000.
ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) +
          ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Define 4 sequential path points
path.numPoints = 4

# Point 0: (160, 0)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)  # X target (Axis 5)
point.SetTarget(1, 0)    # Y target (Axis 6)
point.autoSmoothRadius = 10
path.SetPoint(0, point)

# Point 1: (160, 160)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 160)  # X target
point.SetTarget(1, 160)  # Y target
point.autoSmoothRadius = 10
path.SetPoint(1, point)

# Point 2: (0, 160)
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

# Point 3: (0, 0)
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
profile = Profile()
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 0)
point.SetTarget(1, 0)
# For the last segment no smoothing is necessary, but you can still set the radius if required.
point.autoSmoothRadius = 10
path.SetPoint(3, point)

# Add the configured path interpolation with rotation commands into buffer index 0
ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Execute the continuous path interpolation with rotation.
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait until the entire interpolation motion is completed.
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
    print('PathIntplWithRotation running timeout!')
    exit()

# Free the path interpolation with rotation buffer (typically done at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

sleep(1)

# Turn off single-turn mode for the rotational axis (Axis 3)
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(3, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) +
          ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
