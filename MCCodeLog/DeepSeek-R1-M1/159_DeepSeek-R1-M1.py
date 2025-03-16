
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to 200
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
posCommand.target = 200
posCommand.profile.velocity = 1000  # Example velocity value
posCommand.profile.acc = 10000      # Example acceleration value
posCommand.profile.dec = 10000      # Example deceleration value

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(5)

# Get the axis status of Pos Cmd
ret, CmStatus = Wmx3Lib_cm.GetStatus()
if ret != 0:
    print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

posCmd = CmStatus.GetAxesStatus(5).posCmd
print('Pos Cmd : ' + str(posCmd))

# If Pos Cmd is 200, move to 50
if posCmd == 200:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 50
    posCommand.profile.velocity = 1000  # Example velocity value
    posCommand.profile.acc = 10000      # Example acceleration value
    posCommand.profile.dec = 10000      # Example deceleration value

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(5)
