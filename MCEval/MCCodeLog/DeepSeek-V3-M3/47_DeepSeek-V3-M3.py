
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Define the positions to move Axis 7 to
positions = [50, -50, 100, -100]

# Create a position command object
pos = Motion_PosCommand()

# Set position command parameters
pos.axis = 7
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Loop through each position and move Axis 7
for target in positions:
    pos.target = target
    
    # Execute motion to move Axis 7 to the target position
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait until the motion is finished before moving to the next position
    ret = Wmx3Lib_cm.motion.Wait(7)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
