
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create a position command object for Axis 7
posCmd = Motion_PosCommand()
posCmd.axis = 7
posCmd.profile.type = ProfileType.Trapezoidal
posCmd.profile.velocity = 1000
posCmd.profile.acc = 10000
posCmd.profile.dec = 10000

# List of target positions for Axis 7
targets = [50, -50, 100, -100]

for target in targets:
    posCmd.target = target
    ret = Wmx3Lib_cm.motion.StartMov(posCmd)
    if ret != 0:
        print("StartMov error code for target", target, "is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))
        break
    # Wait until the motion of Axis 7 is complete before moving to the next target
    ret = Wmx3Lib_cm.motion.Wait(7)
    if ret != 0:
        print("Wait error code for target", target, "is", ret, ":", Wmx3Lib_cm.ErrorToString(ret))
        break
