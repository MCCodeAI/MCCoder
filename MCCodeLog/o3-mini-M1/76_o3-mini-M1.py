
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

# Create an instance of the advanced motion class.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# ------------------------------------------------------------------------------
# Step 1: Move Axis 5 to -400 with a velocity of 2000.
# ------------------------------------------------------------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = -400
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
# Wait until Axis 5 stops moving.
Wmx3Lib_cm.motion.Wait(5)

# ------------------------------------------------------------------------------
# Step 2: Set up a Periodic type E-CAM table and start the E-CAM motion.
# E-CAM Table pairs:
#   Master Axis (Axis 5):   -100,  -50,    0,   50,  100
#   Slave  Axis (Axis 4):    100,  150,  100,   50,  100
# ------------------------------------------------------------------------------
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Periodic
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 2000
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 5
ECAMdata.slaveAxis = 4
ECAMdata.numPoints = 5
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, -100)
ECAMdata.SetMasterPos(1, -50)
ECAMdata.SetMasterPos(2, 0)
ECAMdata.SetMasterPos(3, 50)
ECAMdata.SetMasterPos(4, 100)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 150)
ECAMdata.SetSlavePos(2, 100)
ECAMdata.SetSlavePos(3, 50)
ECAMdata.SetSlavePos(4, 100)

ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code: ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# ------------------------------------------------------------------------------
# Step 3: Move Axis 5 to 800.
# ------------------------------------------------------------------------------
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 800
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 5 stops moving.
Wmx3Lib_cm.motion.Wait(5)

# ------------------------------------------------------------------------------
# Final Step: Stop the E-CAM motion.
# ------------------------------------------------------------------------------
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code: ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()
