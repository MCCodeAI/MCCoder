# Write Python code to establish a Periodic type E-CAM (Electronic CAM) motion for master Axis 8 and slave Axis 9. Move Axis 8 to -400 with a velocity of 1000. Then set up an E-CAM table with the pairs (-50, 150), (0, 100), (50, 50), (100, 100) and start the E-CAM motion. Finally, move Axis 8 to 400.

# Axes = [8, 9]

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Start an absolute position command of Axis 8 to position -200 with 1000 velocity.
    # Create a command value.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = -400
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position. e.g. 'Move to Position -300..'
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(8)

    # The following example illustrates a typical Periodic type E-CAM table:
    #   Master Axis Position      Slave Axis Position
    #   -50                       150
    #   0                         100
    #   50                        50
    #   100                       100

    ECAMdata = AdvSync_ECAMData()
    ECAMoption = AdvSync_ECAMOptions()

    # The master-slave position curve will be repeated when the master axis moves outside the range defined in the E-CAM table. When the Periodic type, if the slave command positions of the first and last points in the E-CAM table are not equal, there will be a sudden change in the slave command position at each interface where the first and last points meet.
    ECAMoption.type = AdvSync_ECAMType.Periodic
    # The master input is the command position of the master axis.
    ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
    # PyNone: When the E-CAM is activated, the slave axis synchronizes with the master axis immediately.
    ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
    # In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to track the speed of the master-slave curve in the E-CAM table.
    ECAMoption.clutch.simpleCatchUpVelocity = 1000
    # In the AdvSync.ECAMClutchType.SimpleCatchUp mode, it is used to catch up with the acceleration and deceleration of the master-slave curve in the E-CAM table.
    ECAMoption.clutch.simpleCatchUpAcc = 10000

    # Set the E-CAM table.
    ECAMdata.masterAxis = 8
    ECAMdata.slaveAxis = 9
    ECAMdata.numPoints = 4
    ECAMdata.options = ECAMoption

    ECAMdata.SetMasterPos(0, -50)
    ECAMdata.SetMasterPos(1, 0)
    ECAMdata.SetMasterPos(2, 50)
    ECAMdata.SetMasterPos(3, 100)

    ECAMdata.SetSlavePos(0, 150)
    ECAMdata.SetSlavePos(1, 100)
    ECAMdata.SetSlavePos(2, 50)
    ECAMdata.SetSlavePos(3, 100)

    # Start ECAM in channel 0
    ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata) 
    if ret != 0:
        print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Create a command value with a target value of 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 400
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(8)

    # Stop ECAM in channel 0
    ret = Wmx3Lib_adv.advSync.StopECAM(0)
    if ret != 0:
        print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return
