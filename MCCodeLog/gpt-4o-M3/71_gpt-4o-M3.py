
# Axes = [1, 5]
# Inputs = []
# Outputs = []

import math

# Constants
PI = float(3.141592653589793238)
VELOCITY = 1600
SAMPLE_DISTANCE = 50
ANGLE_TOLERANCE = 11
RADIUS = 100
NUM_POINTS = 18

# Initialize the Advanced Motion Library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1000)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Configure the path interpolation with look ahead channel
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 1)
conf.SetAxis(1, 5)
conf.compositeVel = VELOCITY
conf.compositeAcc = 4000
conf.sampleDistance = SAMPLE_DISTANCE
conf.stopOnEmptyBuffer = True
conf.setAngleTolerance = True
conf.angleToleranceDegrees = ANGLE_TOLERANCE

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Add the path interpolation with look ahead commands
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = NUM_POINTS

for i in range(NUM_POINTS):
    Point = AdvMotion_PathIntplLookaheadCommandPoint()
    Point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    Point.linear.axisCount = 2
    Point.linear.SetAxis(0, 1)
    Point.linear.SetAxis(1, 5)
    Point.linear.SetTarget(0, RADIUS * math.cos((i + 1) / NUM_POINTS * (2 * PI)))
    Point.linear.SetTarget(1, RADIUS * math.sin((i + 1) / NUM_POINTS * (2 * PI)))
    path.SetPoint(i, Point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Execute path interpolation with look ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Wait for the path interpolation with look ahead to complete
Wmx3Lib_cm.motion.Wait(1)
timeoutCounter = 0
# Wait until the path interpolation with look ahead is in Stopped state
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

if timeoutCounter > 500:
    print('PathIntplLookahead Running timeout.!')
    return

# Free the path interpolation with look ahead buffer
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return
