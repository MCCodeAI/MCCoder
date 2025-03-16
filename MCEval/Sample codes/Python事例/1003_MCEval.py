#Write Python code to create a  Periodic E-CAM table corresponding to the master axis positions ( 50, 150, 250) and the slave axis positions (100, 200, 100).The master axis is set to single-turn mode, with the encoder range being 0-300.then establishes the E-CAM table, and subsequently moves from the position of 0 to 360 at a speed of 100.
    # Axes = [0,1]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    #Set Axis 0 to single-turn mode, single-turn encoder count 360000.
    ret=Wmx3Lib_cm.config.SetSingleTurn(0,True,360000)
    if ret != 0:
        print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # The following example illustrates a typical Periodic type E-CAM table:
    #   Master Axis Position      Slave Axis Position
    #   50                        100
    #   150                       200
    #   250                       100

    ECAMdata =AdvSync_ECAMData()
    ecopt =AdvSync_ECAMOptions()

    # The master-slave position curve will be repeated when the master axis moves outside the range defined in the E-CAM table.
    ecopt.type=AdvSync_ECAMType.Periodic
    # The master input is the command position of the master axis.
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
    ECAMdata.numPoints=3
    ECAMdata.options=ecopt

    ECAMdata.SetMasterPos(0, 50)
    ECAMdata.SetMasterPos(1, 150)
    ECAMdata.SetMasterPos(2, 250)

    ECAMdata.SetSlavePos(0, 100)
    ECAMdata.SetSlavePos(1, 200)
    ECAMdata.SetSlavePos(2, 100)

    # Start ECAM
    ret=Wmx3Lib_adv.advSync.StartECAM(0,ECAMdata)
    if ret!=0:
        print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Create a command value of target as 300.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 300
    posCommand.profile.velocity = 100
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

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