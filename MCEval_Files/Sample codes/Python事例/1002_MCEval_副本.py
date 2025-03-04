#Create a  Periodic E-CAM table corresponding to the master axis positions ( -50, 0, 50, 100) and the slave axis positions (150, 100, 50, 100).The axis starts moving to the position of -200 at a speed of 1000, then establishes the E-CAM table, and subsequently moves from the position of -200 to 250 at a speed of 100.

    # Axes = [0,1]
    #Start an absolute position command of Axis 0 to position -200  with 100 velocity.
    # Create a command value.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = -200
    posCommand.profile.velocity = 100
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    # Execute command to move to a specified absolute position. e.g. 'Move to Position -300..'
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(0)

    # The following example illustrates a typical Periodic type E-CAM table:
    #   Master Axis Position      Slave Axis Position
    #   -50                       150
    #   0                         100
    #   50                        50
    #   100                       100

    ECAMdata =AdvSync_ECAMData()
    ecopt =AdvSync_ECAMOptions()

    #The master-slave position curve will be repeated when the master axis moves outside the range defined in the E-CAM table.
    ecopt.type=AdvSync_ECAMType.Periodic
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

    ECAMdata.SetMasterPos(0, -50)
    ECAMdata.SetMasterPos(1, 0)
    ECAMdata.SetMasterPos(2, 50)
    ECAMdata.SetMasterPos(3, 100)

    ECAMdata.SetSlavePos(0, 150)
    ECAMdata.SetSlavePos(1, 100)
    ECAMdata.SetSlavePos(2, 50)
    ECAMdata.SetSlavePos(3, 100)

    # Start ECAM
    ret=Wmx3Lib_adv.advSync.StartECAM(0,ECAMdata)
    if ret!=0:
        print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Create a command value with a target value of 250.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 250
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

    # Set servo off for Axes
    for axis in [0, 1]:
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
        if ret != 0:
            print(f'SetServoOn to off error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

    # Stop Communication.
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret!=0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Close Device.
    ret = Wmx3Lib.CloseDevice()
    if ret!=0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    print('Program End.')

if __name__ == '__main__':
    main()