
# Axes = [8, 9, 0, 1]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create the path interpolation with rotation command
path = AdvMotion_PathIntplWithRotationCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)

# Create the path interpolation with rotation buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()

conf.SetAxis(0, 8)  # Axis 8
conf.SetAxis(1, 9)  # Axis 9
conf.rotationalAxis = 0  # Rotational axis
conf.SetCenterOfRotation(0, 30)  # X axis center of rotation position
conf.SetCenterOfRotation(1, 30)  # Y axis center of rotation position

# Enable Z axis
conf.enableZAxis = 1
conf.zAxis = 1

# Rotational axis angle correction motion profile parameters
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 900
conf.angleCorrectionProfile.acc = 1800
conf.angleCorrectionProfile.dec = 1800

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with rotation commands
path.numPoints = 5

# Segment 1: Linear to (50, 50) and Z to 25
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 50)
point.SetTarget(1, 50)
point.zAxisTarget = 25
path.SetPoint(0, point)

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(8)

# Segment 2: Circular to (100, 100) with center (20, 20) and Z to 50
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.direction = 1
point.SetCenterPos(0, 20)
point.SetCenterPos(1, 20)
point.SetTarget(0, 100)
point.SetTarget(1, 100)
point.zAxisTarget = 50
path.SetPoint(1, point)

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(8)

# Segment 3: Linear to (150, 150) and Z to 75
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

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(8)

# Segment 4: Circular to (200, 200) with center (40, 40) and Z to 100
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.direction = 1
point.SetCenterPos(0, 40)
point.SetCenterPos(1, 40)
point.SetTarget(0, 200)
point.SetTarget(1, 200)
point.zAxisTarget = 100
path.SetPoint(3, point)

# Wait for axes to stop moving
Wmx3Lib_cm.motion.Wait(8)

# Segment 5: Linear to (300, 300) and Z to 125
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
    return

# Execute path interpolation with rotation
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with rotation to complete
Wmx3Lib_cm.motion.Wait(8)
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
    print('PathIntplWithRotation Running timeout.!')
    return

# Free the path interpolation with rotation buffer (normally, the buffer should only be freed at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
