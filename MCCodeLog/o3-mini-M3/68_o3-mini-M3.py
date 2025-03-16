
# Axes = [8, 9, 0, 1]
# This script executes a continuous path interpolation‐with‐rotation 
# for Axis 8 (X) and Axis 9 (Y), with rotation about Axis 0 and a Z-axis move on Axis 1.
# The center of rotation is (30, 30) and the motion velocity is 1000.
#
# The 5 segments are defined as follows:
# 1. Linear move to (50, 50) with Z to 25.
# 2. Circular move to (100, 100) with a circle center of (20, 20) and Z to 50.
# 3. Linear move to (150, 150) with Z to 75.
# 4. Circular move to (200, 200) with a circle center of (40, 40) and Z to 100.
# 5. Linear move to (300, 300) with Z to 125.
#
# After starting the entire continuous motion, the routine waits for the entire motion
# to complete (axes stop moving). (For discrete, non‐continuous motions, one should wait 
# after each motion command, but here the segments are connected for a continuous interpolation.)

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation-with-rotation buffer and create a new one.
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation-with-rotation channel.
conf = AdvMotion_PathIntplWithRotationConfiguration()
conf.SetAxis(0, 8)           # X axis is assigned to Axis 8
conf.SetAxis(1, 9)           # Y axis is assigned to Axis 9
conf.rotationalAxis = 0       # Rotation is performed about Axis 0
conf.enableConstProfile = 1   # Use constant motion profile.
conf.angleCorrectionMinimumAngle = 0.01
conf.enableZAxis = 1          # Enable Z axis motion.
conf.zAxis = 1                # Z axis is assigned to Axis 1.
# The center of rotation for the tool is (30,30).
conf.SetCenterOfRotation(0, 30)
conf.SetCenterOfRotation(1, 30)
# Set the motion profile (using trapezoidal profile parameters).
conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
conf.angleCorrectionProfile.velocity = 1000
conf.angleCorrectionProfile.acc = 2000
conf.angleCorrectionProfile.dec = 2000

ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create a multi-segment path interpolation command with 5 points.
path = AdvMotion_PathIntplWithRotationCommand()
path.numPoints = 5

# ---------------- District 1: Linear segment ----------------
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 50)    # X target position
point.SetTarget(1, 50)    # Y target position
point.zAxisTarget = 25     # Z target position
path.SetPoint(0, point)

# ---------------- District 2: Circular segment ----------------
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 100)    # X target position
point.SetTarget(1, 100)    # Y target position
point.zAxisTarget = 50      # Z target position
# For circular segments, specify the circle center relative to the chord.
# (Assuming the API provides these properties; change the field names if necessary.)
point.circleCenterX = 20    # Circle center X coordinate
point.circleCenterY = 20    # Circle center Y coordinate
path.SetPoint(1, point)

# ---------------- District 3: Linear segment ----------------
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 150)   # X target position
point.SetTarget(1, 150)   # Y target position
point.zAxisTarget = 75     # Z target position
path.SetPoint(2, point)

# ---------------- District 4: Circular segment ----------------
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Circular
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 200)   # X target position
point.SetTarget(1, 200)   # Y target position
point.zAxisTarget = 100    # Z target position
point.circleCenterX = 40   # Circle center X coordinate
point.circleCenterY = 40   # Circle center Y coordinate
path.SetPoint(3, point)

# ---------------- District 5: Linear segment ----------------
point = AdvMotion_PathIntplWithRotationCommandPoint()
point.type = AdvMotion_PathIntplSegmentType.Linear
point.profile.type = ProfileType.Trapezoidal
point.profile.velocity = 1000
point.profile.acc = 2000
point.profile.dec = 2000
point.SetTarget(0, 300)   # X target position
point.SetTarget(1, 300)   # Y target position
point.zAxisTarget = 125    # Z target position
path.SetPoint(4, point)

# Add the entire continuous path interpolation command.
ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
if ret != 0:
    print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Execute the continuous path interpolation with rotation.
ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
if ret != 0:
    print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Since the segments are continuously blended, we wait only for the entire motion to complete.
timeoutCounter = 0
pathStatus = AdvMotion_PathIntplWithRotationState()
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
while pathStatus.state != AdvMotion_PathIntplWithRotationState.Idle:
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
if timeoutCounter > 500:
    print('Path interpolation running timeout!')
    exit()

# Free the path interpolation-with-rotation buffer.
ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
if ret != 0:
    print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
