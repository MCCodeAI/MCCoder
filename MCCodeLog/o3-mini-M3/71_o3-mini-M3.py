
import math
import time  # Changed from "from time import sleep" to avoid shadowing issues

# Assume that the necessary classes and objects have been defined elsewhere:
# AdvancedMotion, AdvMotion_PathIntplLookaheadCommand, AdvMotion_PathIntplLookaheadConfiguration,
# AdvMotion_PathIntplLookaheadCommandPoint, AdvMotion_PathIntplLookaheadSegmentType,
# AdvMotion_PathIntplLookaheadState, and that Wmx3Lib is already available.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any previously allocated look-ahead buffer on channel 0.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create the path interpolation look-ahead buffer on channel 0 with a composite velocity of 1600.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1600)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Configure the look-ahead channel for Axis 1 and Axis 5.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 1)   # First axis is 1
conf.SetAxis(1, 5)   # Second axis is 5
conf.compositeVel = 1600
conf.compositeAcc = 4000  # Assumed composite acceleration.
conf.sampleDistance = 50
conf.stopOnEmptyBuffer = True
conf.setAngleTolerance = True
conf.angleToleranceDegrees = 11

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Create a path consisting of 18 linear interpolation segments forming 
# a counterclockwise circle with a radius of 100.
# The circle is centered at (0,0) and the points are generated on its perimeter.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 18

PI = math.pi

for i in range(18):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 1)
    point.linear.SetAxis(1, 5)

    # Correcting the error: For the first point, ensure its time is zero.
    if i == 0:
        point.linear.timeFromStart = 0

    # Compute the target point on the circle.
    # For a counterclockwise circle starting at angle 0, the first target is at (100, 0).
    angle = (i + 1) * (2 * PI) / 18
    x = 100 * math.cos(angle)
    y = 100 * math.sin(angle)
    point.linear.SetTarget(0, x)
    point.linear.SetTarget(1, y)
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Execute the path interpolation with look-ahead.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Wait for axes to finish their complete motion.
# (This waiting loop only occurs after the continuous blended motion is finished.)
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
    time.sleep(0.1)  # Wait only after the complete motion.
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('Path interpolation timeout.')
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

# Free the look-ahead buffer after motion completion.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)
