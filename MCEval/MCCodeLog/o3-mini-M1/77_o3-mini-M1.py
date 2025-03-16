
# Axes = [6, 9]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# Set Axis 6 to single-turn mode with an encoder count of 360000.
ret = Wmx3Lib_cm.config.SetSingleTurn(6, True, 360000)
if ret != 0:
    print("SetSingleTurn error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    return

# The following illustrates a Periodic type E-CAM table:
#   Master Axis Position      Slave Axis Position
#       50                      100
#       100                     200
#       200                     300

ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

# Configure the E-CAM option for a Periodic type.
ECAMoption.type = AdvSync_ECAMType.Periodic
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Set the E-CAM table for master Axis 6 and slave Axis 9 with 3 points.
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

# Start the E-CAM on channel 0.
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print("StartECAM error code is " + str(ret) + ": " + Wmx3Lib.ErrorToString(ret))
    return

# Create and configure a position command to move Axis 6 from position 0 to 300 with velocity 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 300
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 completes its motion.
Wmx3Lib_cm.motion.Wait(6)

# Turn off single-turn mode on Axis 6.
AxisParam = Config_AxisParam()
ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
AxisParam.SetSingleTurnMode(6, False)
ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
if ret != 0:
    print("Close SingleTurnMode error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    return

# Stop the E-CAM, which is a necessary step.
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print("StopECAM error code is " + str(ret) + ": " + Wmx3Lib.ErrorToString(ret))
    return
