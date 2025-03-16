
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

# Initialize the AdvancedMotion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create the path interpolation with rotation buffer
path = AdvMotion_PathIntplWithRotationCommand()
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with rotation channel
conf = AdvMotion_PathIntplWithRotationConfiguration()
conf.SetAxis(0, 5)  # Axis 5
conf.SetAxis(1, 6)  # Axis 6
conf.rotationalAxis = 3  # Rotational axis
conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position

# Disable rotating the X and Y axes around the center of rotation
conf.disableXYRotationalMotion = 1

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with rotation commands
path.numPoints = 4

# Define the path points
points = [(160, 0), (160, 160), (0, 160), (0, 0)]

for i, (x, y) in enumerate(points):
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, x)
    point.SetTarget(1, y)
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with rotation
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation to complete
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
    print('PathIntplWithRotation Running timeout.!')
    return

# Free the path interpolation with rotation buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
