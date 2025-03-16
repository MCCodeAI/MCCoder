
# Axes = [2, 7]
# IOInputs = []
# IOOutputs = []

# Initialize the AdvancedMotion class with your Wmx3Lib library instance
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Create a command to move master Axis 7 to position -300 with a velocity of 1000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = -300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

# Execute the command to move Axis 7
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 7 to reach the target position and stop moving
Wmx3Lib_cm.motion.Wait(7)

# Define the E-CAM table with a Repeat type
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# Configure the E-CAM options
ECAMoption.type = AdvSync_ECAMType.Repeat
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Set the master and slave axes and define the points for the E-CAM table
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

# Start the E-CAM motion
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()

# Create a command to move master Axis 7 to position 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 7
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the command to move Axis 7
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 7 to reach the target position and stop moving
Wmx3Lib_cm.motion.Wait(7)

# Optionally stop the E-CAM motion for cleanup after operations
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit()
