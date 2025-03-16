
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Write Python code to move Axis 6 to 50, -50, 100, and -100, respectively, with blocking waits.

# Initialize position command
pos = Motion_PosCommand()

# Set position command parameters
pos.axis = 6
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Execute motion to move Axis 6 to 50
pos.target = 50
ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute motion to move Axis 6 to -50
pos.target = -50
ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute motion to move Axis 6 to 100
pos.target = 100
ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute motion to move Axis 6 to -100
pos.target = -100
ret = Wmx3Lib_cm.motion.StartMov(pos)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until motion is finished
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
