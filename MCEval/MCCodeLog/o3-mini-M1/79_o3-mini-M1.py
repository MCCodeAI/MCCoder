
# Axes = [3, 6]
# IOInputs = []
# IOOutputs = []

# Establish a Repeat type E-CAM motion for master Axis 6 and slave Axis 3.
# Set master Axis 6 to single-turn mode with a range of 0-360 degrees.
# Set up an E-CAM table with the pairs:
#   Master Axis Position      Slave Axis Position
#   0                         125
#   50                        75
#   100                       150
#   150                       100
#   200                       180
# Then start the E-CAM motion and finally move Axis 6 from position 0 to 1500 at a speed of 1000.
#
# Note: The code waits for the axis to stop after the motion command is executed.

# Assuming the existence of the following classes and methods:
#   AdvancedMotion, Wmx3Lib, Wmx3Lib_cm,
#   AdvSync_ECAMData, AdvSync_ECAMOptions,
#   AdvSync_ECAMType, AdvSync_ECAMSourceType, AdvSync_ECAMClutchType,
#   Motion_PosCommand, ProfileType, Config_AxisParam

# Set Axis 6 to single-turn mode: typically 360 degrees is represented as an encoder count of 360000.
ret = Wmx3Lib_cm.config.SetSingleTurn(6, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Create an instance for advanced motion control.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Set up the E-CAM table with 5 points for a Repeat type motion.
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# Configure the E-CAM options:
ECAMoption.type = AdvSync_ECAMType.Repeat
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Specify master and slave axes and the number of points in the E-CAM table:
ECAMdata.masterAxis = 6
ECAMdata.slaveAxis = 3
ECAMdata.numPoints = 5
ECAMdata.options = ECAMoption

# Define the E-CAM table:
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

# Start E-CAM on channel 0 using the created table.
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit(1)

# Create a positional command to move Axis 6 from position 0 to 1500.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 1500
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 6 reaches the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Turn off single-turn mode for Axis 6 after the motion is complete.
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(6, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    exit(1)

# Stop E-CAM as it is a necessary step to finalize the motion.
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    exit(1)
