
# -*- coding: utf-8 -*-
import math
from time import sleep

# Assume that the following global objects and classes exist and have been initialized elsewhere:
#   Wmx3Lib, Wmx3Lib_adv, Wmx3Lib_cm,
#   AdvancedMotion, AdvMotion_PathIntplLookaheadCommand, AdvMotion_PathIntplLookaheadCommandPoint,
#   AdvMotion_PathIntplLookaheadSegmentType, AdvMotion_PathIntplLookaheadConfiguration,
#   AxisSelection

# --------------------------------------------------------------------
# COMMAND 1:
# Execute path interpolation with look-ahead on Axis 2 and Axis 7 at 2200 velocity.
# The path consists of:
#   1. A line segment to (50, 0)
#   2. A circular arc from (50,0) that goes through (50,100) and returns to (50,0)
#      (approximated by a series of linear segments over a full circle, where the circle has
#       center (50,50) and radius 50)
#   3. A line segment to (100, 0)
#
# Wait for the axes to be idle after the motion completes.
# --------------------------------------------------------------------

# Free any previous look-ahead buffer (channel 0 used arbitrarily)
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create a look-ahead buffer for channel 0 with the commanded composite (linear) velocity of 2200.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
if ret != 0:
    print("CreatePathIntplLookaheadBuffer error code is", ret)
    # Handle error as appropriate

# Configure look-ahead settings for axes 2 and 7.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 2)
conf.SetAxis(1, 7)
conf.compositeVel = 2200
conf.compositeAcc = 10000  # Assumed acceleration value
conf.sampleDistance = 10   # Chosen sample distance (units as required)
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print("SetPathIntplLookaheadConfiguration error code is", ret)
    # Handle error as appropriate

# Build the look-ahead command for Command 1.
# This command is composed of:
#   - Point 0: Line to (50, 0)
#   - Points 1 to 10: Approximated circular arc (full circle) starting from (50,0), going through (50,100)
#                    and returning to (50,0)
#   - Point 11: Line to (100, 0)
num_points = 12
path = AdvMotion_PathIntplLookaheadCommand()
path.numPoints = num_points

# Point 0: Line to (50, 0)
pt = AdvMotion_PathIntplLookaheadCommandPoint()
pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt.linear.axisCount = 2
pt.linear.SetAxis(0, 2)
pt.linear.SetAxis(1, 7)
pt.linear.SetTarget(0, 50)
pt.linear.SetTarget(1, 0)
path.SetPoint(0, pt)

# Points 1-10: Approximated circular arc
center_x = 50
center_y = 50
radius = 50
start_angle = -math.pi / 2
num_circle_pts = 10
for i in range(num_circle_pts):
    angle = start_angle + (2 * math.pi * (i + 1) / num_circle_pts)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 2)
    pt.linear.SetAxis(1, 7)
    pt.linear.SetTarget(0, x)
    pt.linear.SetTarget(1, y)
    path.SetPoint(i + 1, pt)

# Point 11: Line to (100, 0)
pt = AdvMotion_PathIntplLookaheadCommandPoint()
pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt.linear.axisCount = 2
pt.linear.SetAxis(0, 2)
pt.linear.SetAxis(1, 7)
pt.linear.SetTarget(0, 100)
pt.linear.SetTarget(1, 0)
path.SetPoint(num_points - 1, pt)

# Add the command to the look-ahead buffer.
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
if ret != 0:
    print("AddPathIntplLookaheadCommand error code is", ret)
    # Handle error as appropriate

# Start executing the look-ahead path interpolation command.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print("StartPathIntplLookahead error code is", ret)
    # Handle error as appropriate

# Wait until both Axis 2 and Axis 7 have completed their motion.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 2)
axes.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error code is", ret)
    # Handle error as appropriate

# Free the look-ahead buffer after motion completion.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print("FreePathIntplLookaheadBuffer error code is", ret)
    # Handle error as appropriate

# --------------------------------------------------------------------
# End of COMMAND 1
# --------------------------------------------------------------------

# Pause for 0.5 seconds.
sleep(0.5)

# --------------------------------------------------------------------
# COMMAND 2:
# Execute path interpolation with look-ahead on Axis 2 and Axis 7 at 2200 velocity.
# The path consists of:
#   1. A line segment to (150, 100)
#   2. A line segment to (200, 0)
#
# Wait for the axes to be idle after the motion completes.
# --------------------------------------------------------------------

# Free any previous look-ahead buffer on channel 0.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

# Create a look-ahead buffer for channel 0 with velocity of 2200.
ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
if ret != 0:
    print("CreatePathIntplLookaheadBuffer error code is", ret)
    # Handle error as appropriate

# Reuse the same configuration for axes 2 and 7.
conf = AdvMotion_PathIntplLookaheadConfiguration()
conf.axisCount = 2
conf.SetAxis(0, 2)
conf.SetAxis(1, 7)
conf.compositeVel = 2200
conf.compositeAcc = 10000
conf.sampleDistance = 10
conf.stopOnEmptyBuffer = True

ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
if ret != 0:
    print("SetPathIntplLookaheadConfiguration error code is", ret)
    # Handle error as appropriate

# Build the look-ahead command for Command 2 with 2 points.
path2 = AdvMotion_PathIntplLookaheadCommand()
path2.numPoints = 2

# Point 0: Line to (150, 100)
pt = AdvMotion_PathIntplLookaheadCommandPoint()
pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt.linear.axisCount = 2
pt.linear.SetAxis(0, 2)
pt.linear.SetAxis(1, 7)
pt.linear.SetTarget(0, 150)
pt.linear.SetTarget(1, 100)
path2.SetPoint(0, pt)

# Point 1: Line to (200, 0)
pt = AdvMotion_PathIntplLookaheadCommandPoint()
pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
pt.linear.axisCount = 2
pt.linear.SetAxis(0, 2)
pt.linear.SetAxis(1, 7)
pt.linear.SetTarget(0, 200)
pt.linear.SetTarget(1, 0)
path2.SetPoint(1, pt)

# Add the second command to the look-ahead buffer.
ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path2)
if ret != 0:
    print("AddPathIntplLookaheadCommand error code is", ret)
    # Handle error as appropriate

# Start executing the Command 2 look-ahead motion.
ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
if ret != 0:
    print("StartPathIntplLookahead error code is", ret)
    # Handle error as appropriate

# Wait until both Axis 2 and Axis 7 have completed their motion.
axes.SetAxis(0, 2)
axes.SetAxis(1, 7)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error code is", ret)
    # Handle error as appropriate

# Free the look-ahead buffer after motion completion.
ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
if ret != 0:
    print("FreePathIntplLookaheadBuffer error code is", ret)
    # Handle error as appropriate
