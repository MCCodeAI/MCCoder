
# Axes = [1, 4]
# IOInputs = []
# IOOutputs = []

# Create a path interpolation with look-ahead for Axis 1 and Axis 4.
# The composite velocity is set to 1100.
# The interpolation points are:
#    1. (200, 0)
#    2. (200, 200)
#    3. (0, 200)
#    4. (0, 0)
#    5. (200, 200)
# The sample distance is 50 and the smooth radius for each segment is 10.
# The acceleration limits for each axis are 8800.
# The velocity limits are 700 for Axis 1 and 500 for Axis 4.
#
# Note: This script waits for the motion to complete after the entire
#       interpolation (i.e. at the end of continuous motion), but does not wait
#       in between individual segments.

# Assume that the following objects and functions are already defined in the environment:
#   - Wmx3Lib, Wmx3Lib_adv, Wmx3Lib_cm (for motion commands)
#   - AdvancedMotion, AdvMotion_PathIntplLookaheadCommand, AdvMotion_PathIntplLookaheadConfiguration,
#     AdvMotion_PathIntplLookaheadCommandPoint, AdvMotion_PathIntplLookaheadSegmentType,
#     AdvMotion_PathIntplLookaheadState
#   - sleep (from time module)
#
# The code below creates and executes a path with look-ahead.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any pre-existing look-ahead buffer on channel 0.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create a new path interpolation with look-ahead buffer.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the look-ahead interpolation parameters.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 1)  # First axis is Axis 1.
conf.SetAxis(1, 4)  # Second axis is Axis 4.
conf.compositeVel = 1100      # Overall interpolation velocity.
conf.compositeAcc = 8800      # Composite acceleration; individual axes are limited to 8800.
conf.stopOnEmptyBuffer = True # Automatically set axes to idle after path completion.
conf.sampleDistance = 50      # Sampling resolution for the generated profile.
# Set acceleration limits for each axis.
conf.SetAccLimit(0, 8800)
conf.SetAccLimit(1, 8800)
# Set individual velocity limits (Axis 1: 700, Axis 4: 500).
conf.SetVelocityLimit(0, 700)
conf.SetVelocityLimit(1, 500)

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Build the path interpolation command.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 5  # 5 interpolation segments corresponding to the 5 target points.

# Define each interpolation point with a smooth radius of 10.
# Point 0: Move to (200, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 10
path.SetPoint(0, point)

# Point 1: Move to (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(1, point)

# Point 2: Move to (0, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(2, point)

# Point 3: Move to (0, 0)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 0)
point.linear.SetTarget(1, 0)
point.linear.smoothRadius = 10
path.SetPoint(3, point)

# Point 4: Move to (200, 200)
point = AdvMotion_PathIntplLookaheadCommandPoint()
point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
point.linear.axisCount = 2
point.linear.SetAxis(0, 1)
point.linear.SetAxis(1, 4)
point.linear.SetTarget(0, 200)
point.linear.SetTarget(1, 200)
point.linear.smoothRadius = 10
path.SetPoint(4, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Execute the path interpolation with look-ahead.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the entire path motion to complete.
timeoutCounter = 0
while True:
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('PathIntplLookahead Running timeout.')
        exit()

# Free the path interpolation with look-ahead buffer.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

print("Path interpolation with look-ahead completed successfully.")
