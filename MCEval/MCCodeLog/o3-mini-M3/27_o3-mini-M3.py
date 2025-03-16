
# Axes = [7, 8]
# IOInputs = []
# IOOutputs = []

import math
import time

# Initialize the advanced motion object
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free any existing path interpolation buffer for channel 0 before starting
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print("Error freeing previous interpolation buffer: " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Create the path interpolation (absolute path interpolation using the lookahead buffer)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 1500)
if ret != 0:
    print("CreatePathIntplLookaheadBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Configure the interpolation for Axes 7 and 8
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 7)
conf.SetAxis(1, 8)
conf.compositeVel = 1500      # Set velocity to 1500 as specified
conf.compositeAcc = 4000      # Acceleration value (example value)
conf.sampleDistance = 10      # A sample distance (chosen arbitrarily)
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print("SetPathIntplLookaheadConfiguration error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Define the pentastar points (each point is expressed as an absolute coordinate)
points = [
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

# Create the path command and add each of the 10 points
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = len(points)

for i, (x, y) in enumerate(points):
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 7)     # For Axis 7 (x-coordinate)
    pt.linear.SetAxis(1, 8)     # For Axis 8 (y-coordinate)
    pt.linear.SetTarget(0, x)
    pt.linear.SetTarget(1, y)
    path.SetPoint(i, pt)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print("AddPathIntplLookaheadCommand error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Start executing the absolute path interpolation
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print("StartPathIntplLookahead error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait until the entire path motion is complete.
# Since this is a continuous motion, we wait only after its completion.
Wmx3Lib_cm.motion.Wait(7)  # Wait using one of the moving axes (Axis 7 is used here)
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while True:
    if pathStatus.state == AdvMotion_PathIntplLookaheadState.Stopped:
        break
    time.sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print("Path interpolation running timeout!")
        break
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

# Free the interpolation buffer (normally done at the end of the application)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print("FreePathIntplLookaheadBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()
