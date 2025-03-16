
# Axes = [2, 4, 5]
# IOInputs = []
# IOOutputs = []

# The following code performs a 3D path interpolation on axes 4, 5, and 2
# with a constant motion profile (velocity 300), following a sequence of
# 21 segments and then the reverse of that sequence (total 42 segments).
# For circular segments, the center of the arc is defined.
#
# NOTE:
# - "StartPathIntpl3DPos" is assumed to send the entire path command.
# - After starting the motion, the code waits for all the involved axes to
#   reach a stopped state.
# - This code uses a single constant motion profile for all segments.
#
# Assumptions: The motion library classes and functions (e.g. AdvancedMotion,
# AdvMotion_PathIntpl3DCommand, Profile, ProfileType, AdvMotion_PathIntplSegmentType,
# AxisSelection, etc.) are pre-defined elsewhere.
#
# Also, note that we wait for axes to stop only after the entire continuous motion
# is commanded (i.e. not between individual segments).

# Initialize the advanced motion command for 3D path interpolation
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
path = AdvMotion_PathIntpl3DCommand()

# Configure the axes: we use Axis 4, 5, and 2 (in the order provided by the command).
path.SetAxis(0, 4)
path.SetAxis(1, 5)
path.SetAxis(2, 2)

# Set a constant motion profile for the entire path. Here, velocity is 300.
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 300
profile.acc = 3000
profile.dec = 3000
path.SetProfile(0, profile)

# Define the 21 forward segments in a list of dictionaries.
# For each segment, 'type' can be 'Linear' or 'Circular'.
# For circular segments, a 'center' tuple is provided.
segments_forward = [
    {"type": "Linear",   "target": (90, 0, 0)},
    {"type": "Circular", "target": (100, 10, 0),   "center": (97.071, 2.929, 0)},
    {"type": "Linear",   "target": (100, 90, 0)},
    {"type": "Circular", "target": (90, 100, 0),   "center": (97.071, 97.071, 0)},
    {"type": "Linear",   "target": (10, 100, 0)},
    {"type": "Circular", "target": (0, 90, 0),     "center": (2.929, 97.071, 0)},
    {"type": "Linear",   "target": (0, 0, 0)},
    {"type": "Linear",   "target": (90, 0, 0)},
    {"type": "Circular", "target": (100, 0, -10),  "center": (97.071, 0, -2.929)},
    {"type": "Linear",   "target": (100, 0, -90)},
    {"type": "Circular", "target": (90, 0, -100),  "center": (97.071, 0, -97.071)},
    {"type": "Linear",   "target": (10, 0, -100)},
    {"type": "Circular", "target": (0, 0, -90),    "center": (2.929, 0, -97.071)},
    {"type": "Linear",   "target": (0, 0, 0)},
    {"type": "Linear",   "target": (0, 90, 0)},
    {"type": "Circular", "target": (0, 100, -10),  "center": (0, 97.071, -2.929)},
    {"type": "Linear",   "target": (0, 100, -90)},
    {"type": "Circular", "target": (0, 90, -100),  "center": (0, 97.071, -97.071)},
    {"type": "Linear",   "target": (0, 10, -100)},
    {"type": "Circular", "target": (0, 0, -90),    "center": (0, 2.929, -97.071)},
    {"type": "Linear",   "target": (0, 0, 0)}
]

# To reverse the entire sequence, we simply reverse the forward segments.
# The reverse sequence follows the same interpolation types with the same target and center parameters.
segments_reverse = list(reversed(segments_forward))

# Combine forward and reverse segments into one full path.
all_segments = segments_forward + segments_reverse

# Set the total number of segments (points) in the path.
path.numPoints = len(all_segments)

# Assign each segment's type, target and (if applicable) circle center.
for i, seg in enumerate(all_segments):
    if seg["type"] == "Linear":
        path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
    elif seg["type"] == "Circular":
        path.SetType(i, AdvMotion_PathIntplSegmentType.Circular)
    # Set the target coordinates for each axis
    path.SetTarget(0, i, seg["target"][0])
    path.SetTarget(1, i, seg["target"][1])
    path.SetTarget(2, i, seg["target"][2])
    # For circular segments, also set the circle intermediate target (center)
    if seg["type"] == "Circular":
        path.SetCircleIntermediateTarget(0, i, seg["center"][0])
        path.SetCircleIntermediateTarget(1, i, seg["center"][1])
        path.SetCircleIntermediateTarget(2, i, seg["center"][2])

# Start the 3D path interpolation motion.
ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
if ret != 0:
    print("StartPathIntpl3DPos error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
else:
    # Wait for the motion to complete on all three axes.
    axes = AxisSelection()
    axes.axisCount = 3
    axes.SetAxis(0, 4)
    axes.SetAxis(1, 5)
    axes.SetAxis(2, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
