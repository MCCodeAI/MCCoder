
# Axes = [10]
# IOInputs = []
# IOOutputs = []

i = 0
while i < 3:
    # Create a relative position command for Axis 10 with 13.3 distance and 1333 velocity
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = 13.3
    posCommand.profile.velocity = 1333
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute relative movement command
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until axis completes movement
    Wmx3Lib_cm.motion.Wait(10)
    
    i += 1
