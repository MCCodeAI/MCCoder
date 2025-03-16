
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Move Axis 7 to -300 at a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = -300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 7 stops moving.
Wmx3Lib_cm.motion.Wait(7)

# Set up a Repeat type E-CAM table with the following master-slave pairs:
#   Master Axis Position    Slave Axis Position
#   0                        25
#   50                       75
#   100                      50
#   150                      100
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Repeat
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 7
ECAMdata.slaveAxis = 2
ECAMdata.numPoints = 4
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, 0)
ECAMdata.SetMasterPos(1, 50)
ECAMdata.SetMasterPos(2, 100)
ECAMdata.SetMasterPos(3, 150)

ECAMdata.SetSlavePos(0, 25)
ECAMdata.SetSlavePos(1, 75)
ECAMdata.SetSlavePos(2, 50)
ECAMdata.SetSlavePos(3, 100)

# Start E-CAM motion.
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Move Axis 7 to 300 at a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 7 stops moving.
Wmx3Lib_cm.motion.Wait(7)

# Stop E-CAM motion.
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
