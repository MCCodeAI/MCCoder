
# Axes = [6, 9]
# Inputs = []
# Outputs = []

# Initialize the advanced motion library
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Set Axis 6 to single-turn mode, single-turn encoder count 360000.
ret = Wmx3Lib_cm.config.SetSingleTurn(6, True, 360000)
if ret != 0:
    print('SetSingleTurn error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define a Periodic type E-CAM table:
#   Master Axis Position      Slave Axis Position
#   50                        100
#   100                       200
#   200                       300

ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# Configure the E-CAM options
ECAMoption.type = AdvSync_ECAMType.Periodic
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Set the E-CAM table
ECAMdata.masterAxis = 6
ECAMdata.slaveAxis = 9
ECAMdata.numPoints = 3
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, 50)
ECAMdata.SetMasterPos(1, 100)
ECAMdata.SetMasterPos(2, 200)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 200)
ECAMdata.SetSlavePos(2, 300)

# Start ECAM
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return

# Create a command value to move to position 300
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 1000
posCommand.profile.dec = 1000

# Execute command to move from current position to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(6)

# Turn off Axis 6 single-turn mode
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(6, False)

ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print('Close SingleTurnMode error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
    return

# Stop ECAM
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
    return
