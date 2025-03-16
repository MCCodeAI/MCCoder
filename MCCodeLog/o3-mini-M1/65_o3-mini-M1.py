
# Axes = [3, 5, 6]
# IOInputs = []
# IOOutputs = []

import time
from time import sleep

def run_path_interpolation():
    # Instantiate the advanced motion library object.
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    
    # Free any existing interpolation with rotation buffer on channel 0.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    
    # Create the path interpolation with rotation buffer on channel 0 with velocity 1000.
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
    if ret != 0:
        print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with rotation channel.
    conf = AdvMotion_PathIntplWithRotationConfiguration()
    
    # Set the two interpolation axes (Axis 5 and Axis 6) and rotational axis (Axis 3).
    conf.SetAxis(0, 5)  # First interpolation axis (analogous to X axis) -> Axis 5
    conf.SetAxis(1, 6)  # Second interpolation axis (analogous to Y axis) -> Axis 6
    conf.rotationalAxis = 3  # Rotational axis -> Axis 3

    # Set the global center of rotation to (80,80).
    conf.SetCenterOfRotation(0, 80)  # X coordinate of the center of rotation.
    conf.SetCenterOfRotation(1, 80)  # Y coordinate of the center of rotation.
    
    # Set the rotational axis motion profile parameters.
    conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
    conf.angleCorrectionProfile.velocity = 1000
    conf.angleCorrectionProfile.acc = 2000
    conf.angleCorrectionProfile.dec = 2000
    
    # Disable rotating the X and Y axes (i.e. the interpolation axes) around the center of rotation.
    conf.disableXYRotationalMotion = 1
    
    ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
    
    # Set the rotational axis (Axis 3) to single-turn mode (required for rotation).
    ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
    if ret != 0:
        print('SetSingleTurn error code is ' + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Create the path interpolation command and configure the four path points.
    path = AdvMotion_PathIntplWithRotationCommand()
    path.numPoints = 4

    # Define the first path point (160, 0).
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)
    point.SetTarget(1, 0)
    path.SetPoint(0, point)

    # Define the second path point (160, 160).
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)
    point.SetTarget(1, 160)
    path.SetPoint(1, point)

    # Define the third path point (0, 160).
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)
    point.SetTarget(1, 160)
    path.SetPoint(2, point)
    
    # Define the fourth path point (0, 0).
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)
    point.SetTarget(1, 0)
    path.SetPoint(3, point)
    
    # Add the path interpolation with rotation command to channel 0.
    ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
    if ret != 0:
        print('AddPathIntplWithRotationCommand error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Execute the continuous path interpolation with rotation.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
    if ret != 0:
        print('StartPathIntplWithRotation error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Wait for the motion to complete.
    Wmx3Lib_cm.motion.Wait(0)
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
        print('PathIntplWithRotation running timeout!')
        return

    # Free the path interpolation with rotation buffer.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    if ret != 0:
        print('FreePathIntplWithRotationBuffer error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    sleep(1)
    
    # Turn off single-turn mode for the rotational axis (Axis 3).
    AxisParam = Config_AxisParam()
    ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
    AxisParam.SetSingleTurnMode(3, False)
    ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
    if ret != 0:
        print('Close SingleTurnMode error code is ' + str(ret) +
              ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

if __name__ == "__main__":
    run_path_interpolation()
