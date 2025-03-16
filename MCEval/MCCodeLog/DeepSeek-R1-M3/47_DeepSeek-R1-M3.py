
# Axes = [7]
# IOInputs = []
# IOOutputs = []

pos = Motion_PosCommand()

# Set position command parameters
pos.axis = 7
pos.profile.type = ProfileType.Trapezoidal
pos.profile.velocity = 1000
pos.profile.acc = 10000
pos.profile.dec = 10000

# Execute motion sequence
targets = [50, -50, 100, -100]
for target in targets:
    pos.target = target
    ret = Wmx3Lib_cm.motion.StartMov(pos)
    if ret != 0:
        print(f'StartMov error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        return
    
    ret = Wmx3Lib_cm.motion.Wait(7)
    if ret != 0:
        print(f'Wait error code {ret}: {Wmx3Lib_cm.ErrorToString(ret)}')
        return
