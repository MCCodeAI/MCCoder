
# Axes = [0, 1, 8, 9]
# IOInputs = []
# IOOutputs = []

# Create a path interpolation with rotation for Axis 8 and 9, rotating around Axis 0 with Z axis as Axis 1.
# The center of rotation is (30, 30) and the motion velocity is 1000.
# The 5 segments are:
#   1) Linear to (50, 50) with Z axis target 25
#   2) Circular to (100, 100) with center (20, 20) and Z axis target 50
#   3) Linear to (150, 150) with Z axis target 75
#   4) Circular to (200, 200) with center (40, 40) and Z axis target 100
#   5) Linear to (300, 300) with Z axis target 125

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previous path interpolation with rotation buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create a new path interpolation with rotation buffer with velocity 1000
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()
# Set the interpolation axes: X axis is Axis 8 and Y axis is Axis 9.
conf.SetAxis(0, 8)  # X axis
conf.SetAxis(1, 9)  # Y axis
# Set the rotational axis: rotating around Axis 0
conf.rotationalAxis = 0
# Set the overall center of rotation, which applies as a reference position.
conf.SetCenterOfRotation(0, 30)
conf.SetCenterOfRotation(1, 30)
# Enable Z axis control: Z-axis is Axis 1.
conf.enableZAxis = 1
conf.zAxis = 1

# Set the motion profile for the translational axes (using a trapezoidal profile)
# Note: For the rotational axis, some applications require fine angle correction.
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 1000
conf.angleCorrectionProfile.acc = 2000
conf.angleCorrectionProfile.dec = 2000

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Set the rotational axis to single-turn mode (necessary for proper rotation handling)
ret = Wmx3Lib_cm.config.SetSingleTurn(0, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Create the path command and add segments
path = AdvMotion_PathIntplWithRotationCommand()
path.numPoints = 5

# Segment 1: Linear interpolation to (50, 50) with Z target 25
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 50)   # X axis target (Axis 8)
point.SetTarget(1, 50)   # Y axis target (Axis 9)
point.zAxisTarget = 25   # Z axis target (Axis 1)
path.SetPoint(0, point)

# Segment 2: Circular interpolation to (100, 100) with center (20, 20) and Z target 50
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.direction = 1  # Assuming a positive (clockwise) direction for the circular move
point.SetCenterPos(0, 20)  # X center of circle
point.SetCenterPos(1, 20)  # Y center of circle
point.SetTarget(0, 100)    # X axis target (Axis 8)
point.SetTarget(1, 100)    # Y axis target (Axis 9)
point.zAxisTarget = 50     # Z axis target (Axis 1)
path.SetPoint(1, point)

# Segment 3: Linear interpolation to (150, 150) with Z target 75
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 150)
point.SetTarget(1, 150)
point.zAxisTarget = 75
path.SetPoint(2, point)

# Segment 4: Circular interpolation to (200, 200) with center (40, 40) and Z target 100
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.direction = 1
point.SetCenterPos(0, 40)
point.SetCenterPos(1, 40)
point.SetTarget(0, 200)
point.SetTarget(1, 200)
point.zAxisTarget = 100
path.SetPoint(3, point)

# Segment 5: Linear interpolation to (300, 300) with Z target 125
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 300)
point.SetTarget(1, 300)
point.zAxisTarget = 125
path.SetPoint(4, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Execute the path interpolation with rotation
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the motion to complete: wait for all axes to stop moving
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
    print('PathIntplWithRotation Running timeout!')
    exit()

# Free the path interpolation with rotation buffer when done
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Turn off the single-turn mode for the rotational axis (Axis 0)
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(0, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
