
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to 200
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 200
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 5 stops moving after the motion command completes.
Wmx3Lib_cm.motion.Wait(5)

# Get the status of Axis 5 and check its Pos Cmd value.
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print("GetStatus error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
    exit()

axisStatus = CmStatus.GetAxesStatus(5)
print("Axis 5 Pos Cmd:", axisStatus.posCmd)

# If the axis command position is 200, then command a new move to position 50.
if abs(axisStatus.posCmd - 200) < 1e-5:  # using a small tolerance for comparison
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 50
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        exit()
    
    # Wait until Axis 5 stops moving after this motion command.
    Wmx3Lib_cm.motion.Wait(5)
