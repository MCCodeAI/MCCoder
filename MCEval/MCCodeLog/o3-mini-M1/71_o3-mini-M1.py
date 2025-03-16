
# Axes = [1, 5]
# IOInputs = []
# IOOutputs = []

import math
from time import sleep

# Initialize the AdvancedMotion instance.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any pre-existing path interpolation with look ahead buffer for channel 0.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create the path interpolation with look ahead buffer on channel 0 with composite velocity 1600.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1600)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the path interpolation with look ahead channel.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 1)
conf.SetAxis(1, 5)
conf.compositeVel = 1600
conf.compositeAcc = 4000
conf.sampleDistance = 50
conf.stopOnEmptyBuffer = True
conf.setAngleTolerance = True
conf.angleToleranceDegrees = 11

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create a path consisting of 18 linear interpolations forming a counterclockwise circle.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 18

PI = math.pi

for i in range(18):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    # Specify the axis numbers for the two axes.
    point.linear.SetAxis(0, 1)
    point.linear.SetAxis(1, 5)
    # Compute the target positions along a circle of radius 100.
    # The interpolation points are generated using an offset of (i+1) to distribute 18 points around the circle.
    angle = (i + 1) * (2 * PI / 18)
    point.linear.SetTarget(0, 100 * math.cos(angle))
    point.linear.SetTarget(1, 100 * math.sin(angle))
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Start executing the path interpolation with look ahead.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the motion to complete.
# The call below waits on axis 1. Since this example is a continuous motion sequence,
# we do not wait between segments but only after the full path is executed.
Wmx3Lib_cm.motion.Wait(1)
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('PathIntplLookahead Running timeout!')
        exit()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

# Free the path interpolation with look ahead buffer.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit()
