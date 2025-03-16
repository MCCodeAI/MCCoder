
# Axes = [4]
# IOInputs = []
# IOOutputs = []

if XYZ == 0:
    # Create position command for XYZ=0 condition
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = 88
    posCommand.profile.velocity = 1100
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute absolute position command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until axis completes motion
    Wmx3Lib_cm.motion.Wait(4)
else:
    # Create position command for XYZ≠0 condition
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = 90
    posCommand.profile.velocity = 1100  # Maintain same speed per question
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute absolute position command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until axis completes motion
    Wmx3Lib_cm.motion.Wait(4)
