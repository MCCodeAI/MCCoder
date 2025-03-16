
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Repeat the cycle 3 times.
for cycle in range(3):

    # Move Axis 5 to position 66.6 at a speed of 900.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 66.6
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("Error moving Axis 5 to 66.6. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 5 stops moving after reaching 66.6.
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print("Wait error on Axis 5 after moving to 66.6. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        break

    # Move Axis 5 back to position 0 at a speed of 900.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 0
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("Error moving Axis 5 to 0. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until Axis 5 stops moving after reaching 0.
    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print("Wait error on Axis 5 after moving to 0. Error code:", ret, Wmx3Lib_cm.ErrorToString(ret))
        break
