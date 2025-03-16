
# Axes = [4]
# IOInputs = []
# IOOutputs = []

import time

# Create a jog command for Axis 4 using the TimeaccTrapezoidal profile.
jogCommand = Motion_JogCommand()
jogCommand.profile.type = ProfileType.TimeaccTrapezoidal  # Use TimeaccTrapezoidal profile
jogCommand.axis = 4
jogCommand.profile.velocity = 90
jogCommand.profile.accTimeMilliseconds = 20
jogCommand.profile.decTimeMilliseconds = 20

# Start jogging Axis 4.
ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
if ret != 0:
    print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Jog for 120 milliseconds.
    time.sleep(0.12)
    
    # Stop jogging on Axis 4.
    ret = Wmx3Lib_cm.motion.Stop(4)
    if ret != 0:
        print('Stop error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
        # Wait until the axis stops moving.
        ret = Wmx3Lib_cm.motion.Wait(4)
        if ret != 0:
            print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
