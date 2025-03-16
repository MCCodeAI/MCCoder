
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = []

import math
import time

# Create an instance of AdvancedMotion from your motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation buffer on channel 0
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed

# Create the path interpolation buffer on channel 0 with velocity 1500
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1500)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed

# Configure the path interpolation channel for Axes 7 and 8
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 7)
conf.SetAxis(1, 8)
conf.compositeVel = 1500
conf.compositeAcc = 4000  # Example composite acceleration (adjust as needed)
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed

# Define the pentastar path points
# (x, y) coordinates:
# (0.00, 0.00), (22.45, -69.10), (95.11, -69.10), (36.33, -111.80),
# (58.78, -180.90), (0.00, -138.20), (-58.78, -180.90), (-36.33, -111.80),
# (-95.11, -69.10), (-22.45, -69.10)
path_points = [
    (0.00, 0.00),
    (22.45, -69.10),
    (95.11, -69.10),
    (36.33, -111.80),
    (58.78, -180.90),
    (0.00, -138.20),
    (-58.78, -180.90),
    (-36.33, -111.80),
    (-95.11, -69.10),
    (-22.45, -69.10)
]

# Create a path interpolation command and add the defined points
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = len(path_points)

for i, (x, y) in enumerate(path_points):
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    point.linear.axisCount = 2
    point.linear.SetAxis(0, 7)
    point.linear.SetAxis(1, 8)
    point.linear.SetTarget(0, x)
    point.linear.SetTarget(1, y)
    path.SetPoint(i, point)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed

# Start the absolute path interpolation with look ahead
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed

# Wait for the motion to complete on Axis 7 (the first axis in the configuration).
Wmx3Lib_cm.motion.Wait(7)

# Poll the path interpolation status until it has stopped
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    time.sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
if timeoutCounter > 500:
    print('PathIntplLookahead Running timeout.!')
    # Handle timeout error as needed

# Free the path interpolation buffer (typically done at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    # Handle error as needed
