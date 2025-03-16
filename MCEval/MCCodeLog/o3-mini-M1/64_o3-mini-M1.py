
# Axes = [2, 4, 5]
# IOInputs = []
# IOOutputs = []

# This script executes a 3D path interpolation for axes 4, 5, and 2 (sorted as [2, 4, 5])
# with a constant velocity of 300. The path consists of a forward sequence of 21 segments
# (a mix of linear and circular interpolations) followed by the reverse of that sequence.
# After starting the motion, the script waits for all axes to stop moving before ending.

# Note: This script assumes that the AdvancedMotion library and its related API objects
# (e.g., AdvMotion_PathIntpl3DCommand, Profile, AxisSelection, etc.) are defined elsewhere.
# No motion libraries are imported here as per instructions.

def execute_3d_path_interpolation():
    # Create an instance of AdvancedMotion and a new 3D path interpolation command object.
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    path = AdvMotion_PathIntpl3DCommand()

    # Set the axes in sorted order: 2, 4, and 5.
    path.SetAxis(0, 2)  # X coordinate mapped to Axis 2
    path.SetAxis(1, 4)  # Y coordinate mapped to Axis 4
    path.SetAxis(2, 5)  # Z coordinate mapped to Axis 5

    # Use a constant profile for the entire path.
    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 300
    profile.acc = 2000
    profile.dec = 2000
    path.SetProfile(0, profile)  # Applies to all segments when using constant profile.

    # Define the forward segments (21 segments)
    # Each segment is defined as a dictionary with 'type', 'target', and, if circular, a 'center'
    forward_segments = [
        { "type": "Linear",   "target": (90, 0, 0) },
        { "type": "Circular", "target": (100, 10, 0),    "center": (97.071, 2.929, 0) },
        { "type": "Linear",   "target": (100, 90, 0) },
        { "type": "Circular", "target": (90, 100, 0),    "center": (97.071, 97.071, 0) },
        { "type": "Linear",   "target": (10, 100, 0) },
        { "type": "Circular", "target": (0, 90, 0),      "center": (2.929, 97.071, 0) },
        { "type": "Linear",   "target": (0, 0, 0) },
        { "type": "Linear",   "target": (90, 0, 0) },
        { "type": "Circular", "target": (100, 0, -10),   "center": (97.071, 0, -2.929) },
        { "type": "Linear",   "target": (100, 0, -90) },
        { "type": "Circular", "target": (90, 0, -100),   "center": (97.071, 0, -97.071) },
        { "type": "Linear",   "target": (10, 0, -100) },
        { "type": "Circular", "target": (0, 0, -90),     "center": (2.929, 0, -97.071) },
        { "type": "Linear",   "target": (0, 0, 0) },
        { "type": "Linear",   "target": (0, 90, 0) },
        { "type": "Circular", "target": (0, 100, -10),   "center": (0, 97.071, -2.929) },
        { "type": "Linear",   "target": (0, 100, -90) },
        { "type": "Circular", "target": (0, 90, -100),   "center": (0, 97.071, -97.071) },
        { "type": "Linear",   "target": (0, 10, -100) },
        { "type": "Circular", "target": (0, 0, -90),     "center": (0, 2.929, -97.071) },
        { "type": "Linear",   "target": (0, 0, 0) }
    ]

    # Create the complete sequence including the reverse.
    # The reverse sequence is obtained by reversing the forward segments.
    # In this case, we duplicate the entire forward sequence in reverse order so that the
    # path goes from step 21 back to step 1.
    reverse_segments = forward_segments[::-1]
    full_segments = forward_segments + reverse_segments
    num_segments = len(full_segments)
    path.numPoints = num_segments

    # Helper function to set a segment in the path command.
    def set_segment(i, segment):
        # Determine segment type.
        if segment["type"] == "Linear":
            path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
        elif segment["type"] == "Circular":
            path.SetType(i, AdvMotion_PathIntplSegmentType.Circular)
        else:
            raise ValueError("Unknown segment type at index {}.".format(i))

        # Set target positions for X, Y, and Z.
        # Here, target values are extracted from the tuple.
        path.SetTarget(0, i, segment["target"][0])
        path.SetTarget(1, i, segment["target"][1])
        path.SetTarget(2, i, segment["target"][2])

        # If the segment is circular, set the circle intermediate (center) targets.
        if segment["type"] == "Circular":
            path.SetCircleIntermediateTarget(0, i, segment["center"][0])
            path.SetCircleIntermediateTarget(1, i, segment["center"][1])
            path.SetCircleIntermediateTarget(2, i, segment["center"][2])

    # Loop over the complete (forward + reverse) segments and set each one.
    for idx, seg in enumerate(full_segments):
        set_segment(idx, seg)

    # Start the 3D path interpolation motion.
    ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
    if ret != 0:
        print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait until motion is complete.
    # Waiting is done after the entire continuous path (all segments) completes.
    axes = AxisSelection()
    axes.axisCount = 3
    axes.SetAxis(0, 2)
    axes.SetAxis(1, 4)
    axes.SetAxis(2, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

# Execute the path interpolation command.
execute_3d_path_interpolation()
