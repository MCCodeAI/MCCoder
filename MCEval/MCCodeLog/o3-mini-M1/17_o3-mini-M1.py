
# Axes = [5, 7]
# IOInputs = []
# IOOutputs = []

import time

# Create a relative path interpolation motion command for Axes 7 and 5 with a velocity of 1000.
# The path will add linear interpolation segments with the relative increments (10*j, -10*j) for j = 0,...,4.
#
# Note:
#   - This code uses a similar structure as the provided context examples.
#   - It waits for the motion to complete only after starting the overall path, not in between the segments.
#   - All motion library objects (e.g., AdvancedMotion, AdvMotion_PathIntplCommand, etc.) 
#     are assumed to be defined elsewhere in the application.

# Initialize the AdvancedMotion object (assumed defined elsewhere)
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a new relative path interpolation command instance.
path = AdvMotion_PathIntplCommand()

# Configure the two-axis path.
# Using the order as in the command: axis index 0 for Axis 7 and axis index 1 for Axis 5.
path.SetAxis(0, 7)
path.SetAxis(1, 5)

# Use a constant motion profile for the entire path.
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 4000
profile.dec = 4000
path.SetProfile(0, profile)

# Set the command as a relative motion command.
# (Assuming the API supports an isRelative flag for path commands.)
path.isRelative = 1

# Build the path segments using a loop.
# The path will have 5 segments; each segment adds a relative offset of (10*j, -10*j).
numSegments = 5
path.numPoints = numSegments

for j in range(numSegments):
    # Create a path point for the current segment.
    point = AdvMotion_PathIntplCommandPoint()
    # Set the segment type to linear interpolation.
    point.type = AdvMotion_PathIntplSegmentType.Linear
    # Define that this segment involves 2 axes.
    point.linear.axisCount = 2
    # For a relative motion, targets represent incremental changes.
    # The target for Axis at index 0 is 10 * j, and for Axis at index 1 is -10 * j.
    point.linear.SetTarget(0, 10 * j)
    point.linear.SetTarget(1, -10 * j)
    # Add the constructed point into the path.
    path.SetPoint(j, point)

# Start the relative path interpolation motion command.
ret = Wmx3Lib_adv.advMotion.StartPathIntplMov(path)
if ret != 0:
    print("StartPathIntplMov error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()

# Wait for the motion to complete on the specified axes.
axes = AxisSelection()
axes.axisCount = 2
axes.SetAxis(0, 7)
axes.SetAxis(1, 5)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
if ret != 0:
    print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    exit()
