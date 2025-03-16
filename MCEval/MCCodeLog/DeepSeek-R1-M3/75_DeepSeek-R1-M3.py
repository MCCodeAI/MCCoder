
# Axes = [2, 1]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Move Axis 2 to -100 with velocity 1000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(2)

# Set up E-CAM table
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 2
ECAMdata.slaveAxis = 1
ECAMdata.numPoints = 7
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, -100)
ECAMdata.SetMasterPos(1, -50)
ECAMdata.SetMasterPos(2, 0)
ECAMdata.SetMasterPos(3, 50)
ECAMdata.SetMasterPos(4, 100)
ECAMdata.SetMasterPos(5, 150)
ECAMdata.SetMasterPos(6, 250)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 150)
ECAMdata.SetSlavePos(2, 100)
ECAMdata.SetSlavePos(3, 50)
ECAMdata.SetSlavePos(4, 100)
ECAMdata.SetSlavePos(5, 50)
ECAMdata.SetSlavePos(6, 150)

# Start E-CAM motion
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Move Axis 2 to 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(2)

# Stop E-CAM motion
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
