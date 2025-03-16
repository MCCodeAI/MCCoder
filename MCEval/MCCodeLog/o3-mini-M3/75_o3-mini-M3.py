
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

# Initialize AdvancedMotion object for E-CAM control
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

# --- Step 1: Move master Axis 2 to -100 with a velocity of 1000 ---
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Acceleration value (example)
posCommand.profile.dec = 10000  # Deceleration value (example)

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
# Wait until Axis 2 stops moving.
Wmx3Lib_cm.motion.Wait(2)

# --- Step 2: Set up Normal type E-CAM motion for master Axis 2 and slave Axis 1 ---
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

# Set up the E-CAM table:
#   Master Axis Position      Slave Axis Position
ECAMdata.SetMasterPos(0, -100)  # Point 0: master position -100
ECAMdata.SetSlavePos(0, 100)    #         slave position 100

ECAMdata.SetMasterPos(1, -50)   # Point 1: master position -50
ECAMdata.SetSlavePos(1, 150)    #         slave position 150

ECAMdata.SetMasterPos(2, 0)     # Point 2: master position 0
ECAMdata.SetSlavePos(2, 100)    #         slave position 100

ECAMdata.SetMasterPos(3, 50)    # Point 3: master position 50
ECAMdata.SetSlavePos(3, 50)     #         slave position 50

ECAMdata.SetMasterPos(4, 100)   # Point 4: master position 100
ECAMdata.SetSlavePos(4, 100)    #         slave position 100

ECAMdata.SetMasterPos(5, 150)   # Point 5: master position 150
ECAMdata.SetSlavePos(5, 50)     #         slave position 50

ECAMdata.SetMasterPos(6, 250)   # Point 6: master position 250
ECAMdata.SetSlavePos(6, 150)    #         slave position 150

# Start the E-CAM motion (channel 0 is used as an example)
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))

# --- Step 3: Move master Axis 2 to 300 ---
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
# Wait until Axis 2 stops moving.
Wmx3Lib_cm.motion.Wait(2)

# --- Step 4: Stop the E-CAM motion ---
ret = Wmx3Lib_adv.advSync.StopECAM(0)
if ret != 0:
    print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
