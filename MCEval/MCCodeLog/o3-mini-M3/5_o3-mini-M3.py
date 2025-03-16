
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Set up the position command using a trapezoidal profile for Axis 5.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 5
# Set default acceleration and deceleration (these values can be adjusted as needed)
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Repeat the motion cycle 3 times.
for cycle in range(3):
    # Move Axis 5 to position 66.6 at a speed of 900.
    posCommand.target = 66.6
    posCommand.profile.velocity = 900
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code while moving Axis 5 to 66.6: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break
    # Wait until Axis 5 stops moving.
    Wmx3Lib_cm.motion.Wait(5)
    
    # Move Axis 5 back to position 0 at a speed of 900.
    posCommand.target = 0
    posCommand.profile.velocity = 900
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code while moving Axis 5 to 0: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break
    # Wait until Axis 5 stops moving.
    Wmx3Lib_cm.motion.Wait(5)
