
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Set Axis 6 to single-turn mode, single-turn encoder count 360000.
ret = Wmx3Lib_cm.config.SetSingleTurn(6, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# The following example illustrates a typical Periodic type E-CAM table:
#   Master Axis Position      Slave Axis Position
#   50                        100
#   100                       200
#   200                       300

ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# The master-slave position curve will be repeated when the master axis moves outside the range defined in the E-CAM table.
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
ECAMdata.masterAxis = 6
ECAMdata.slaveAxis = 9
ECAMdata.numPoints = 3
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, 50)
ECAMdata.SetMasterPos(1, 100)
ECAMdata.SetMasterPos(2, 200)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 200)
ECAMdata.SetSlavePos(2, 300)

# Start ECAM
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Create a command value of target as 300.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Turn off Axis 6 single-turn mode.
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(6, False)

ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Stop ECAM is a necessary step!
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
