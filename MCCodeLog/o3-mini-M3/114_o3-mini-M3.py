
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# Establish Normal type E-CAM motion for master Axis 4 and slave Axis 6.
# Step 1: Move Axis 4 to -100 with a velocity of 1000.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
# Wait until Axis 4 reaches the target position and stops.
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Step 2: Set up the Normal type E-CAM table.
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 4
ECAMdata.slaveAxis = 6
ECAMdata.numPoints = 7
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, -100)
ECAMdata.SetSlavePos(0, 100)

ECAMdata.SetMasterPos(1, -50)
ECAMdata.SetSlavePos(1, 150)

ECAMdata.SetMasterPos(2, 0)
ECAMdata.SetSlavePos(2, 100)

ECAMdata.SetMasterPos(3, 50)
ECAMdata.SetSlavePos(3, 50)

ECAMdata.SetMasterPos(4, 100)
ECAMdata.SetSlavePos(4, 100)

ECAMdata.SetMasterPos(5, 150)
ECAMdata.SetSlavePos(5, 50)

ECAMdata.SetMasterPos(6, 250)
ECAMdata.SetSlavePos(6, 150)

# Start the E-CAM motion on channel 0.
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit(1)

# Step 3: After starting ECAM, move Axis 4 to 300.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)
# Wait until Axis 4 reaches 300 and stops.
ret = Wmx3Lib_cm.motion.Wait(4)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Stop E-CAM motion (this is a necessary step).
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit(1)
