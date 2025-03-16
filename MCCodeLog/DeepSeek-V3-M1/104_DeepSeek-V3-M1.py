
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a command value for the first motion.
posCommand1 = Motion_PosCommand()
posCommand1.profile.type = ProfileType.Trapezoidal
posCommand1.axis = 2
posCommand1.target = 80
posCommand1.profile.velocity = 900
posCommand1.profile.endVelocity = 800
posCommand1.profile.acc = 10000
posCommand1.profile.dec = 10000

# Execute command to move to the first target position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(2)

# Create a command value for the second motion.
posCommand2 = Motion_PosCommand()
posCommand2.profile.type = ProfileType.Trapezoidal
posCommand2.axis = 2
posCommand2.target = 100
posCommand2.profile.velocity = 900
posCommand2.profile.startVelocity = 800
posCommand2.profile.acc = 10000
posCommand2.profile.dec = 10000

# Execute command to move to the second target position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand2)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(2)
