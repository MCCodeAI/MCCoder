
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

import time
import math

# Note: This script assumes that all the motion control classes, constants,
# and objects (e.g., AdvancedMotion, Wmx3Lib, Wmx3Lib_cm, AdvMotion_PathIntplLookaheadCommand,
# AdvMotion_PathIntplLookaheadCommandPoint, AdvMotion_PathIntplLookaheadSegmentType,
# AdvMotion_PathIntplLookaheadConfiguration, AdvMotion_PathIntplLookaheadState, etc.)
# are defined and available in the runtime environment.

# -----------------------------------------------------------------------
# First continuous motion block:
#   1. Linear interpolation to (50, 0)
#   2. Circular interpolation to (50, 0) through (50, 100)
#   3. Linear interpolation to (100, 0)
# -----------------------------------------------------------------------

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Free previous look-ahead buffer (using channel 0) then create a new one with velocity 2200.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code:', ret)
    exit()

# Set up look-ahead configuration for Axes 2 and 7.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 2)
conf.SetAxis(1, 7)
conf.compositeVel = 2200
conf.compositeAcc = 4000  # Assumed acceleration value
conf.sampleDistance = 50  # Chosen sample distance
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code:', ret)
    exit()

# Create a look-ahead path command with 3 segments.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 3

# --- Segment 1: Linear interpolation to (50, 0) ---
pt0 = AdvMotion_PathIntplLookaheadCommandPoint()
pt0.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt0.linear.axisCount = 2
pt0.linear.SetAxis(0, 2)
pt0.linear.SetAxis(1, 7)
pt0.linear.SetTarget(0, 50)   # Axis 2 target = 50
pt0.linear.SetTarget(1, 0)    # Axis 7 target = 0
path.SetPoint(0, pt0)

# --- Segment 2: Circular interpolation to (50, 0) via (50, 100) ---
pt1 = AdvMotion_PathIntplLookaheadCommandPoint()
pt1.type = AdvMotion_PathIntplLookaheadSegmentType.Circular
# The following assumes the circular segment structure similar to the linear one,
# but with additional center point and direction settings.
pt1.circular.axisCount = 2
pt1.circular.SetAxis(0, 2)
pt1.circular.SetAxis(1, 7)
pt1.circular.SetTarget(0, 50)    # Axis 2 target = 50
pt1.circular.SetTarget(1, 0)     # Axis 7 target = 0
pt1.circular.SetCenter(0, 50)    # Axis 2 center = 50 (from through point)
pt1.circular.SetCenter(1, 100)   # Axis 7 center = 100 (through point)
pt1.circular.direction = 1       # 1 for counterclockwise rotation
path.SetPoint(1, pt1)

# --- Segment 3: Linear interpolation to (100, 0) ---
pt2 = AdvMotion_PathIntplLookaheadCommandPoint()
pt2.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt2.linear.axisCount = 2
pt2.linear.SetAxis(0, 2)
pt2.linear.SetAxis(1, 7)
pt2.linear.SetTarget(0, 100)   # Axis 2 target = 100
pt2.linear.SetTarget(1, 0)     # Axis 7 target = 0
path.SetPoint(2, pt2)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code:', ret)
    exit()

ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code:', ret)
    exit()

# Wait for the first motion block to finish.
timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
    time.sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('First motion block timeout.')
        exit()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code:', ret)
    exit()

# -----------------------------------------------------------------------
# Pause between continuous motions.
# -----------------------------------------------------------------------
time.sleep(0.5)

# -----------------------------------------------------------------------
# Second continuous motion block:
#   4. Linear interpolation to (150, 100)
#   5. Linear interpolation to (200, 0)
# -----------------------------------------------------------------------

ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
if ret != 0:
    print('CreatePathIntplLookaheadBuffer error code:', ret)
    exit()

# Reuse the same configuration for the second motion block.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 2)
conf.SetAxis(1, 7)
conf.compositeVel = 2200
conf.compositeAcc = 4000
conf.sampleDistance = 50
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print('SetPathIntplLookaheadConfiguration error code:', ret)
    exit()

# Create a look-ahead command with 2 segments.
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = 2

# --- Segment 4: Linear interpolation to (150, 100) ---
pt0 = AdvMotion_PathIntplLookaheadCommandPoint()
pt0.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt0.linear.axisCount = 2
pt0.linear.SetAxis(0, 2)
pt0.linear.SetAxis(1, 7)
pt0.linear.SetTarget(0, 150)   # Axis 2 target = 150
pt0.linear.SetTarget(1, 100)   # Axis 7 target = 100
path.SetPoint(0, pt0)

# --- Segment 5: Linear interpolation to (200, 0) ---
pt1 = AdvMotion_PathIntplLookaheadCommandPoint()
pt1.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt1.linear.axisCount = 2
pt1.linear.SetAxis(0, 2)
pt1.linear.SetAxis(1, 7)
pt1.linear.SetTarget(0, 200)   # Axis 2 target = 200
pt1.linear.SetTarget(1, 0)     # Axis 7 target = 0
path.SetPoint(1, pt1)

ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print('AddPathIntplLookaheadCommand error code:', ret)
    exit()

ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print('StartPathIntplLookahead error code:', ret)
    exit()

timeoutCounter = 0
ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)
while pathStatus.state != AdvMotion_PathIntplLookaheadState.Stopped:
    time.sleep(0.1)
    timeoutCounter += 1
    if timeoutCounter > 500:
        print('Second motion block timeout.')
        exit()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplLookaheadStatus(0)

ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print('FreePathIntplLookaheadBuffer error code:', ret)
    exit()
