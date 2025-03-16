
import time

def main():
    # Initialize the advanced motion library
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    
    # Attempt to free any previously allocated spline buffer on channel 0.
    # Note: Error code 65627 indicates that no buffer is currently allocated,
    # so we ignore that specific error.
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0 and ret != 65627:
        print("FreeSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return
    elif ret == 65627:
        print("FreeSplineBuffer returned error code 65627 (buffer not allocated), continuing...")
    
    # Create the spline channel buffer (buffer size chosen as 200)
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 200)
    if ret != 0:
        print("CreateSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    time.sleep(0.001)

    # Set up the S curve spline command options for a cubic spline motion.
    # Instead of using AdvMotion_SCurveSplineCommand (which is not defined),
    # we use AdvMotion_ProfileSplineCommand and configure its profile for S-Curve motion.
    spl = AdvMotion_ProfileSplineCommand()
    spl.dimensionCount = 2
    # Map axis indices to physical axes.
    # We assign Axis 6 to index 0 and Axis 9 to index 1.
    spl.SetAxis(0, 6)
    spl.SetAxis(1, 9)
    # Set up the S-Curve profile parameters for each axis (velocity=1200, acceleration/deceleration=5000)
    spl.profile = Profile()
    spl.profile.type = ProfileType.SCurve
    spl.profile.velocity = 1200
    spl.profile.acc = 5000
    spl.profile.dec = 5000
    # Increase sample multiplier to improve trajectory smoothness if needed.
    spl.sampleMultiplier = 20

    # Define the spline points.
    # Each AdvMotion_SplinePoint holds position data for the two axes:
    # for index 0 (Axis 6) and index 1 (Axis 9) respectively.
    pts = []
    # Points: (0,0), (30,50), (60,0), (90,50), (120,0)
    point_data = [(0, 0), (30, 50), (60, 0), (90, 50), (120, 0)]
    for pos in point_data:
        pt = AdvMotion_SplinePoint()
        pt.SetPos(0, pos[0])
        pt.SetPos(1, pos[1])
        pts.append(pt)
    
    # Execute the S curve spline motion.
    # This call initiates the cubic spline motion on a pre-allocated channel.
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_Profile(0, spl, len(pts), pts)
    if ret != 0:
        print("StartCSplinePos_Profile error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for axes to complete the motion before proceeding.
    # (Wait after this discrete motion; in a series of continuous motions,
    #  waiting would only be applied between discrete moves.)
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 6)
    axes.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Free the spline buffer (typically done at the end of the spline motion)
    ret = Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)
    if ret != 0 and ret != 65627:
        print("FreeSplineBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        return
    elif ret == 65627:
        print("FreeSplineBuffer returned error code 65627 (buffer already freed or not allocated), continuing...")

    time.sleep(0.5)

if __name__ == '__main__':
    main()
