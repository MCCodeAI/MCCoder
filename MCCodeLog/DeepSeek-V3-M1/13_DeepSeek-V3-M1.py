
# Axes = [13]
# IOInputs = []
# IOOutputs = []

# Jog Axis 13 for 1 second with a velocity of 90, then jog for 1 second with a velocity of -90, repeating this back-and-forth motion 4 times.

# Define the jog command for positive velocity
jogCommandPositive = Motion_JogCommand()
jogCommandPositive.profile.type = ProfileType.Trapezoidal
jogCommandPositive.axis = 13
jogCommandPositive.profile.velocity = 90
jogCommandPositive.profile.acc = 10000
jogCommandPositive.profile.dec = 10000

# Define the jog command for negative velocity
jogCommandNegative = Motion_JogCommand()
jogCommandNegative.profile.type = ProfileType.Trapezoidal
jogCommandNegative.axis = 13
jogCommandNegative.profile.velocity = -90
jogCommandNegative.profile.acc = 10000
jogCommandNegative.profile.dec = 10000

# Repeat the back-and-forth motion 4 times
for i in range(4):
    # Start jogging with positive velocity
    ret = Wmx3Lib_cm.motion.StartJog(jogCommandPositive)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Jogging for 1 second
    sleep(1)
    
    # Stop the axis
    Wmx3Lib_cm.motion.Stop(13)
    
    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(13)
    
    # Start jogging with negative velocity
    ret = Wmx3Lib_cm.motion.StartJog(jogCommandNegative)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Jogging for 1 second
    sleep(1)
    
    # Stop the axis
    Wmx3Lib_cm.motion.Stop(13)
    
    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(13)

print("Back-and-forth motion completed 4 times.")
