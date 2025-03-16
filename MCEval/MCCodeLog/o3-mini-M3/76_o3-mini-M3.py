
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

# Initialize the advanced motion interface.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# -----------------------------------------------------------------
# Step 1: Move master Axis 5 to -400 with a velocity of 2000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = -400
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
Wmx3Lib_cm.motion.Wait(5)  # Wait until Axis 5 stops moving

# -----------------------------------------------------------------
# Step 2: Set up a Periodic type E-CAM table for master Axis 5 and slave Axis 4.
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Periodic
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 2000  # Optional: adjust as needed.
ECAMoption.clutch.simpleCatchUpAcc = 10000

ECAMdata.masterAxis = 5
ECAMdata.slaveAxis = 4
ECAMdata.numPoints = 5
ECAMdata.options = ECAMoption

# Set E-CAM table points: (Master, Slave)
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
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    # If starting the E-CAM fails, exit the routine.
    exit()

# -----------------------------------------------------------------
# Step 3: Move master Axis 5 to 800 with a velocity of 2000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 800
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
Wmx3Lib_cm.motion.Wait(5)  # Wait until Axis 5 stops moving

# -----------------------------------------------------------------
# Step 4: Stop the E-CAM motion.
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()
