
# Axes = [4, 5]
# IOInputs = []
# IOOutputs = []

# The following code is for establishing a Periodic type E-CAM motion.

# Define an advanced motion interface for E-CAM configuration
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a command value to move Axis 5 to position -400 with velocity 2000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = -400
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to specified position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 5 to arrive at position -400 and stop
Wmx3Lib_cm.motion.Wait(5)

# ECAM Setup
# Initialize ECAM options and data for periodic motion.
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# Configure ECAM options to be Periodic type
ECAMoption.type = AdvSync_ECAMType.Periodic
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 2000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Define the E-CAM table
ECAMdata.masterAxis = 5
ECAMdata.slaveAxis = 4
ECAMdata.numPoints = 5
ECAMdata.options = ECAMoption

# Set master and slave positions for ECAM table
master_positions = [-100, -50, 0, 50, 100]
slave_positions = [100, 150, 100, 50, 100]

for i in range(5):
    ECAMdata.SetMasterPos(i, master_positions[i])
    ECAMdata.SetSlavePos(i, slave_positions[i])

# Start ECAM
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

# Create a command value to move Axis 5 to position 800
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 800
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move Axis 5 to position 800
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))

# Wait for Axis 5 to arrive at position 800 and stop
Wmx3Lib_cm.motion.Wait(5)

# Stop ECAM is a necessary step!
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
