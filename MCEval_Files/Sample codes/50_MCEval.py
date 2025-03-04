# Write python code to Executes a path interpolation of Axis 0 and 1 with a rotation Axis 2 and with a Z axis 3, the center of rotation is (75,75) and the velocity is 1000. There are 7 segments. 1)Linear interpolation to (100,0) and Z axis to 25; 2)Circular interpolation to (150,50) with center (100,50) and Z axis to 50; 3)Linear interpolation to (150,100) and Z axis to 75; 4)Circular interpolation to (100,150) with center (100,100) and Z axis to 100; 5)Linear interpolation to (50,150) and Z axis to 125; 6)Circular interpolation to (100,150) with center (50,100) and Z axis to 150; 7)Linear interpolation to (0,0) and Z axis to 175.
    # Axes = [0, 1, 2, 3]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplWithRotationCommand()
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    # Create the path interpolation with rotation buffer
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
    if ret != 0:
        print('CreatePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Configure the path interpolation with rotation channel
    conf = AdvMotion_PathIntplWithRotationConfiguration()

    conf.SetAxis(0, 0)  # X axis
    conf.SetAxis(1, 1)  # Y axis
    conf.rotationalAxis = 2  # Rotational axis
    conf.SetCenterOfRotation(0, 75)  # X axis center of rotation position
    conf.SetCenterOfRotation(1, 75)  # Y axis center of rotation position

    # Enable constant profile
    conf.enableConstProfile = 1

    # Prevent stop from occurring at very small angles
    conf.angleCorrectionMinimumAngle = 0.01

    # Enable Z axis
    conf.enableZAxis = 1
    conf.zAxis = 3

    # Rotational axis angle correction motion profile parameters
    conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
    conf.angleCorrectionProfile.velocity = 900
    conf.angleCorrectionProfile.acc = 1800
    conf.angleCorrectionProfile.dec = 1800

    ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
    if ret != 0:
        print('SetPathIntplWithRotationConfiguration error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    #Set Axis 2 to single-turn mode, single-turn encoder count 360. Single-turn mode is necessary for rotation axis in path interpolatioin with rotation function.
    ret=Wmx3Lib_cm.config.SetSingleTurn(2,True,360000)
    if ret != 0:
        print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Add the path interpolation with rotation commands
    path.numPoints = 7

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 100)
    point.SetTarget(1, 0)
    point.zAxisTarget = 25
    path.SetPoint(0, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Circular
    point.direction = 1
    point.SetCenterPos(0, 100)
    point.SetCenterPos(1, 50)
    point.SetTarget(0, 150)
    point.SetTarget(1, 50)
    point.zAxisTarget = 50
    path.SetPoint(1, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.SetTarget(0, 150)
    point.SetTarget(1, 100)
    point.zAxisTarget = 75
    path.SetPoint(2, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Circular
    point.direction = 1
    point.SetCenterPos(0, 100)
    point.SetCenterPos(1, 100)
    point.SetTarget(0, 150)
    point.SetTarget(1, 150)
    point.zAxisTarget = 100
    path.SetPoint(3, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.SetTarget(0, 50)
    point.SetTarget(1, 150)
    point.zAxisTarget = 125
    path.SetPoint(4, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Circular
    point.direction = 1
    point.SetCenterPos(0, 50)
    point.SetCenterPos(1, 100)
    point.SetTarget(0, 0)
    point.SetTarget(1, 100)
    point.zAxisTarget = 1500
    path.SetPoint(5, point)

    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.SetTarget(0, 0)
    point.SetTarget(1, 0)
    point.zAxisTarget = 175
    path.SetPoint(6, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
    if ret != 0:
        print('AddPathIntplWithRotationCommand error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Execute path interpolation with rotation
    ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
    if ret != 0:
        print('StartPathIntplWithRotation error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return
    Wmx3Lib_cm.motion.Wait(0)
    timeoutCounter = 0
    # Wait until the path interpolation with rotation is in Idle state
    pathStatus = AdvMotion_PathIntplWithRotationState()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
    while True:
        if (pathStatus.state == AdvMotion_PathIntplWithRotationState.Idle):
            break
        sleep(0.1)
        timeoutCounter = timeoutCounter + 1
        if (timeoutCounter > 500):
            break
        ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
    if (timeoutCounter > 500):
        print('PathIntplWithRotation Runuing timeout.!')
        return
    # Free the path interpolation with rotation buffer (normally, the buffer should only be freed at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    if ret != 0:
        print('FreePathIntplWithRotationBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    #Turn off Axis 2 single-turn mode.
    AxisParam=Config_AxisParam()
    ret,AxisParam =Wmx3Lib_cm.config.GetAxisParam()
    AxisParam.SetSingleTurnMode(2,False)

    ret,AxisParamError=Wmx3Lib_cm.config.SetAxisParam(AxisParam)
    if ret != 0:
        print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

