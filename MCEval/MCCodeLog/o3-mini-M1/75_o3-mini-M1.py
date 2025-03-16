
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

# Establish a Normal type E-CAM motion for master Axis 2 and slave Axis 1.
# Move Axis 2 to -100 with a velocity of 1000. Set up an E-CAM table with the pairs:
#   (-100, 100), (-50, 150), (0, 100), (50, 50), (100, 100), (150, 50) and (250, 150).
# Start the E-CAM motion. Then, move Axis 2 to 300.

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Move Axis 2 to -100
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
# Wait until Axis 2 stops moving
Wmx3Lib_cm.motion.Wait(2)

# Set up the Normal type E-CAM table
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 2   # Master axis is Axis 2
ECAMdata.slaveAxis = 1    # Slave axis is Axis 1
ECAMdata.numPoints = 7    # 7 points in the table
ECAMdata.options = ECAMoption

# Define the E-CAM table points
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

# Start the E-CAM motion
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# Move Axis 2 to 300 while the E-CAM motion is active
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
    exit()

# Wait until Axis 2 stops moving
Wmx3Lib_cm.motion.Wait(2)

# Stop the E-CAM motion after the axis has stopped moving
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()
