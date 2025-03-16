
# Axes = [6]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()

# Set position command parameters for Axis 6
pos.axis = 6
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Define target positions in specified sequence
targets = [50, -50, 100, -100]

for target in targets:
    pos.target = target
    
    # Execute motion command
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print(f'StartMov error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        return
    
    # Wait until motion completes
    ret = Wmx3Lib_cm.motion.Wait(6)
    if ret != 0:
        print(f'Wait error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        return
