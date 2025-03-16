
# Axes = [6, 3]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Set Axis 6 to single-turn mode, single-turn encoder count 360000.
ret = Wmx3Lib_cm.config.SetSingleTurn(6, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# The following example illustrates a typical Repeat type E-CAM table:
#   Master Axis Position      Slave Axis Position
#   0                         125
#   50                        75
#   100                       150
#   150                       100
#   200                       180

ECAMdata = AdvSync_ECAMData()
ecopt = AdvSync_ECAMOptions()

ecopt.type = AdvSync_ECAMType.Repeat
ecopt.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ecopt.clutch.type = AdvSync_ECAMClutchType.PyNone
ecopt.clutch.simpleCatchUpVelocity = 1000
ecopt.clutch.simpleCatchUpAcc = 10000

# Set the E-CAM table.
ECAMdata.masterAxis = 6
ECAMdata.slaveAxis = 3
ECAMdata.numPoints = 5
ECAMdata.options = ecopt

ECAMdata.SetMasterPos(0, 0)
ECAMdata.SetMasterPos(1, 50)
ECAMdata.SetMasterPos(2, 100)
ECAMdata.SetMasterPos(3, 150)
ECAMdata.SetMasterPos(4, 200)

ECAMdata.SetSlavePos(0, 125)
ECAMdata.SetSlavePos(1, 75)
ECAMdata.SetSlavePos(2, 150)
ECAMdata.SetSlavePos(3, 100)
ECAMdata.SetSlavePos(4, 180)

# Start ECAM
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Create a command value with a target value of 1500.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 1500
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Stop ECAM is a necessary step! 
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
