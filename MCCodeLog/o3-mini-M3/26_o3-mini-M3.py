
# Axes = [6, 7]
# IOInputs = []
# IOOutputs = []

# Establish synchronous control between master Axis 6 and slave Axis 7,
# then move Axis 6 to position 120 and afterwards to position 240 with a velocity of 1000.

# Set up synchronous control: Axis 6 is the master, Axis 7 is the slave.
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Create a Motion_PosCommand for Axis 6.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.profile.velocity = 1000
# Set acceleration and deceleration (using typical default values)
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# First motion: move Axis 6 to position 120.
posCommand.target = 120
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 6 has stopped moving.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Second motion: move Axis 6 to position 240.
posCommand.target = 240
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 6 has stopped moving.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Release the synchronization between master Axis 6 and slave Axis 7.
ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
