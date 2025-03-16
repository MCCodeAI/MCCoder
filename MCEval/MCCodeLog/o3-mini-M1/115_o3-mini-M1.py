
def main():
    # Step 1: Move Axis 5 to the position -55 at a speed of 1000 using an scurve profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Scurve  # Use the scurve profile type
    posCommand.axis = 5
    posCommand.target = -55
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000   # Example acceleration
    posCommand.profile.dec = 10000   # Example deceleration

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for Axis 5 to stop moving.
    axisSel = AxisSelection()
    axisSel.axisCount = 1
    axisSel.SetAxis(0, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Step 2: Calculate variables.
    a = 6
    b = a + 1
    c = a * 10
    d = c - b

    # Step 3: Start an absolute linear interpolation motion command for Axis 5 and Axis 2 
    # to position (a, c) with a velocity of 1000.
    linCommand = Motion_LinearIntplCommand()
    linCommand.axisCount = 2
    # Assign first axis as Axis 5 and second as Axis 2.
    linCommand.SetAxis(0, 5)
    linCommand.SetAxis(1, 2)
    linCommand.profile.type = ProfileType.Trapezoidal
    linCommand.profile.velocity = 1000
    linCommand.profile.acc = 10000
    linCommand.profile.dec = 10000
    linCommand.SetTarget(0, a)  # Target for Axis 5
    linCommand.SetTarget(1, c)  # Target for Axis 2

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(linCommand)
    if ret != 0:
        print("StartLinearIntplPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for both Axis 5 and Axis 2 to stop moving.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 5)
    axisSel.SetAxis(1, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Step 4: Start a counterclockwise circular interpolation motion command for Axis 5 and Axis 2.
    # Sleep for 1.1 seconds before starting the circular motion.
    import time
    time.sleep(1.1)

    circCommand = Motion_CenterAndLengthCircularIntplCommand()
    circCommand.SetAxis(0, 5)
    circCommand.SetAxis(1, 2)
    # Set the center position to (50, 50)
    circCommand.SetCenterPos(0, 50)
    circCommand.SetCenterPos(1, 50)
    # Set the arc length to d and velocity to c, using a trapezoidal profile.
    circCommand.arcLengthDegree = d
    circCommand.profile.type = ProfileType.Trapezoidal
    circCommand.profile.velocity = c
    circCommand.profile.acc = 10000
    circCommand.profile.dec = 10000
    # For counterclockwise circular motion, assign the direction value as 1 (1 for counterclockwise, -1 for clockwise).
    circCommand.clockwise = 1

    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(circCommand)
    if ret != 0:
        print("StartCircularIntplPos_CenterAndLength error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for both Axis 5 and Axis 2 to complete the circular motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 5)
    axisSel.SetAxis(1, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
