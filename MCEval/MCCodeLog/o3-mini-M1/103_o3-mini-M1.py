
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

# --- Simultaneous motion for Axis 3 and Axis 4 ---
# Create and configure the position command for Axis 3.
posCommand3 = Motion_PosCommand()
posCommand3.profile.type = ProfileType.Trapezoidal
posCommand3.axis = 3
posCommand3.target = 36
posCommand3.profile.velocity = 900
posCommand3.profile.acc = 10000
posCommand3.profile.dec = 10000

# Create and configure the position command for Axis 4.
posCommand4 = Motion_PosCommand()
posCommand4.profile.type = ProfileType.Trapezoidal
posCommand4.axis = 4
posCommand4.target = 45
posCommand4.profile.velocity = 900
posCommand4.profile.acc = 10000
posCommand4.profile.dec = 10000

# Execute the absolute position commands for Axis 3 and 4 at the same time.
ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
if ret != 0:
    print('StartPos error for Axis 3: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

ret = Wmx3Lib_cm.motion.StartPos(posCommand4)
if ret != 0:
    print('StartPos error for Axis 4: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until both Axis 3 and 4 have stopped moving.
Wmx3Lib_cm.motion.Wait(3)
Wmx3Lib_cm.motion.Wait(4)

# --- Motion for Axis 6 ---
# Create and configure the position command for Axis 6.
posCommand6 = Motion_PosCommand()
posCommand6.profile.type = ProfileType.Trapezoidal
posCommand6.axis = 6
posCommand6.target = 108
posCommand6.profile.velocity = 900
posCommand6.profile.acc = 10000
posCommand6.profile.dec = 10000

# Execute the absolute position command for Axis 6.
ret = Wmx3Lib_cm.motion.StartPos(posCommand6)
if ret != 0:
    print('StartPos error for Axis 6: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 6 has stopped moving.
Wmx3Lib_cm.motion.Wait(6)
