
# Axes = [4]
# IOInputs = []
# IOOutputs = []

import time

# Create the jog command for Axis 4
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.TimeAccTrapezoidal  # Use the corrected TimeAccTrapezoidal profile
jogCommand.axis = 4
jogCommand.profile.velocity = 90
jogCommand.profile.accTimeMilliseconds = 20
jogCommand.profile.decTimeMilliseconds = 20

# Start jogging Axis 4
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Jog for 120 milliseconds (do not wait in the middle of continuous motion)
time.sleep(0.12)

# Stop Axis 4 after jogging
Wmx3Lib_cm.motion.Stop(4)

# Wait until Axis 4 stops moving before proceeding
Wmx3Lib_cm.motion.Wait(4)
