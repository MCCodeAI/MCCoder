# Write Python code to establish a Repeat type E-CAM (Electronic CAM) motion for master Axis 6 and slave Axis 8. Set the master axis to single-turn mode with a range of 0-360 degree. Set up an E-CAM table with the pairs (0, 25), (50, 75), (100, 50), (150, 100) and start the E-CAM motion. and move from position 0 to 1500 at a speed of 1000.

    # Axes = [0, 1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    #Set Axis 0 to single-turn mode, single-turn encoder count 360000.
    ret=Wmx3Lib_cm.config.SetSingleTurn(0,True,360000)
    if ret != 0:
        print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # The following example illustrates a typical Repeat type E-CAM table:
    #   Master Axis Position      Slave Axis Position
    #   0                         25
    #   50                        75
    #   100                       50
    #   150                       100

    ECAMdata =AdvSync_ECAMData()
    ecopt =AdvSync_ECAMOptions()

    ecopt.type=AdvSync_ECAMType.Repeat
    ecopt.source.type=AdvSync_ECAMSourceType.MasterCommandPos
    #PyNone: When the E-CAM is activated, the slave axis synchronizes with the master axis immediately.
    ecopt.clutch.type=AdvSync_ECAMClutchType.PyNone
    #In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to track the speed of the master-slave curve in the E-CAM table.
    ecopt.clutch.simpleCatchUpVelocity=1000
    #In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to catch up with the acceleration and deceleration of the master-slave curve in the E-CAM table.
    ecopt.clutch.simpleCatchUpAcc=10000

    #Set the E-CAM table.
    ECAMdata.masterAxis=0
    ECAMdata.slaveAxis=1
    ECAMdata.numPoints=4
    ECAMdata.options=ecopt

    ECAMdata.SetMasterPos(0, 0)
    ECAMdata.SetMasterPos(1, 50)
    ECAMdata.SetMasterPos(2, 100)
    ECAMdata.SetMasterPos(3, 150)

    ECAMdata.SetSlavePos(0, 25)
    ECAMdata.SetSlavePos(1, 75)
    ECAMdata.SetSlavePos(2, 50)
    ECAMdata.SetSlavePos(3, 100)

    # Start ECAM
    ret=Wmx3Lib_adv.advSync.StartECAM(0,ECAMdata)
    if ret!=0:
        print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    #Create a command value with a target value of 1500.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 1500
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret!=0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(0)

    #Turn off Axis 0 single-turn mode.
    AxisParam=Config_AxisParam()
    ret,AxisParam =Wmx3Lib_cm.config.GetAxisParam()
    AxisParam.SetSingleTurnMode(0,False)

    ret,AxisParamError=Wmx3Lib_cm.config.SetAxisParam(AxisParam)
    if ret != 0:
        print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        return

    # Stop ECAM
    ret = Wmx3Lib_adv.advSync.StopECAM(0)
    if ret != 0:
        print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return
