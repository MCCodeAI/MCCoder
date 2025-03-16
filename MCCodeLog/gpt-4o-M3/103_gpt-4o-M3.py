
# Axes = [3, 4, 6]
# Inputs = []
# Outputs = []

# Move Axis 3 and 4 to position 36 and 45 at the same time with a speed of 900
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 3
posCommand1.target = 36
posCommand1.profile.velocity = 900
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.Trapezoidal
posCommand2.axis = 4
posCommand2.target = 45
posCommand2.profile.velocity = 900
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000

# Execute command to move Axis 3 and 4 simultaneously
ret1 = Wmx3Lib_cm.motion.StartPos(posCommand1)
ret2 = Wmx3Lib_cm.motion.StartPos(posCommand2)

if ret1 != 0:
    print('StartPos error code for Axis 3 is ' + str(ret1) + ': ' + Wmx3Lib_cm.ErrorToString(ret1))
    return

if ret2 != 0:
    print('StartPos error code for Axis 4 is ' + str(ret2) + ': ' + Wmx3Lib_cm.ErrorToString(ret2))
    return

# Wait until both axes have finished moving
Wmx3Lib_cm.motion.Wait(3)
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 6 to position 108 with a speed of 900
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 6
posCommand3.target = 108
posCommand3.profile.velocity = 900
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

# Execute command to move Axis 6
ret3 = Wmx3Lib_cm.motion.StartPos(posCommand3)

if ret3 != 0:
    print('StartPos error code for Axis 6 is ' + str(ret3) + ': ' + Wmx3Lib_cm.ErrorToString(ret3))
    return

# Wait until Axis 6 has finished moving
Wmx3Lib_cm.motion.Wait(6)
