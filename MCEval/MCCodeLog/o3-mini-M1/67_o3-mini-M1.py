
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

from time import sleep

def main():
    # Create an instance of AdvancedMotion using the provided Wmx3Lib object
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    
    # Free any pre-existing path interpolation with rotation buffer
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    if ret != 0:
        print("FreePathIntplWithRotationBuffer error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Create a new path interpolation with rotation buffer with velocity = 1000
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
    if ret != 0:
        print("CreatePathIntplWithRotationBuffer error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with rotation channel
    conf = AdvMotion_PathIntplWithRotationConfiguration()
    # Map the two linear interpolation axes: X => Axis 5 and Y => Axis 6
    conf.SetAxis(0, 5)  # X axis
    conf.SetAxis(1, 6)  # Y axis
    # Set the rotational axis to Axis 3
    conf.rotationalAxis = 3

    # Set the global center of rotation (for X and Y) to (80, 80)
    conf.SetCenterOfRotation(0, 80)  # X axis center of rotation
    conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation

    # Set the rotational axis angle correction motion profile parameters.
    conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
    conf.angleCorrectionProfile.velocity = 1000
    conf.angleCorrectionProfile.acc = 2000
    conf.angleCorrectionProfile.dec = 2000

    # Enable rotating the X and Y axes around a local center of rotation
    conf.enableLocalCenterOfRotation = 1

    ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
    if ret != 0:
        print("SetPathIntplWithRotationConfiguration error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Set Axis 3 (the rotational axis) to single-turn mode.
    ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
    if ret != 0:
        print("SetSingleTurn error code " + str(ret) +
              ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Create the path command and set the number of points to 4
    path = AdvMotion_PathIntplWithRotationCommand()
    path.numPoints = 4

    # --- Point 0 ---
    # Linear move to (160, 0) with local center rotation (50, 40)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)  # X coordinate for Axis 5
    point.SetTarget(1, 0)    # Y coordinate for Axis 6
    point.autoSmoothRadius = 10
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 50)  # Local center rotation X for this segment
    point.SetLocalCenterOfRotation(1, 40)  # Local center rotation Y for this segment
    path.SetPoint(0, point)

    # --- Point 1 ---
    # Linear move to (160, 160) with local center rotation (60, 50)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)  # X coordinate for Axis 5
    point.SetTarget(1, 160)  # Y coordinate for Axis 6
    point.autoSmoothRadius = 10
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 60)  # Local center rotation X for this segment
    point.SetLocalCenterOfRotation(1, 50)  # Local center rotation Y for this segment
    path.SetPoint(1, point)

    # --- Point 2 ---
    # Linear move to (0, 160) with local center rotation (50, 60)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)    # X coordinate for Axis 5
    point.SetTarget(1, 160)  # Y coordinate for Axis 6
    point.autoSmoothRadius = 10
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 50)  # Local center rotation X for this segment
    point.SetLocalCenterOfRotation(1, 60)  # Local center rotation Y for this segment
    path.SetPoint(2, point)

    # --- Point 3 ---
    # Linear move to (0, 0) with local center rotation (40, 50)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)   # X coordinate for Axis 5
    point.SetTarget(1, 0)   # Y coordinate for Axis 6
    point.autoSmoothRadius = 10
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 40)  # Local center rotation X for this segment
    point.SetLocalCenterOfRotation(1, 50)  # Local center rotation Y for this segment
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
    if ret != 0:
        print("AddPathIntplWithRotationCommand error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Execute the entire path interpolation with rotation (continuous motion)
    ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
    if ret != 0:
        print("StartPathIntplWithRotation error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the motion to complete
    ret = Wmx3Lib_cm.motion.Wait(0)
    
    timeoutCounter = 0
    pathStatus = AdvMotion_PathIntplWithRotationState()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
    while True:
        if pathStatus.state == AdvMotion_PathIntplWithRotationState.Idle:
            break
        sleep(0.1)
        timeoutCounter += 1
        if timeoutCounter > 500:
            break
        ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
    if timeoutCounter > 500:
        print("PathIntplWithRotation Running timeout!")
        return

    # Free the path interpolation with rotation buffer
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    if ret != 0:
        print("FreePathIntplWithRotationBuffer error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(1)

    # Turn off single-turn mode for the rotational axis (Axis 3)
    AxisParam = Config_AxisParam()
    ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
    AxisParam.SetSingleTurnMode(3, False)
    ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
    if ret != 0:
        print("Close SingleTurnMode error code " + str(ret) +
              ": " + Wmx3Lib_adv.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
