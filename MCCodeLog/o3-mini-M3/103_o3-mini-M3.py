
# Axes = [3, 4, 6]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 and Axis 4 to positions 36 and 45 simultaneously at a speed of 900,
# then wait for both axes to stop moving before moving Axis 6.
# Finally, move Axis 6 to position 108 at the same speed of 900.

# Create and configure the position command for Axis 3.
posCommand_axis3 = Motion_PosCommand()
posCommand_axis3.profile.type = ProfileType.Trapezoidal
posCommand_axis3.axis = 3
posCommand_axis3.target = 36
posCommand_axis3.profile.velocity = 900
posCommand_axis3.profile.acc = 10000
posCommand_axis3.profile.dec = 10000

# Create and configure the position command for Axis 4.
posCommand_axis4 = Motion_PosCommand()
posCommand_axis4.profile.type = ProfileType.Trapezoidal
posCommand_axis4.axis = 4
posCommand_axis4.target = 45
posCommand_axis4.profile.velocity = 900
posCommand_axis4.profile.acc = 10000
posCommand_axis4.profile.dec = 10000

# Start the absolute position motion for Axis 3.
ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis3)
if ret != 0:
    print("StartPos error for Axis 3, code: " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Start the absolute position motion for Axis 4.
ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis4)
if ret != 0:
    print("StartPos error for Axis 4, code: " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for both Axis 3 and Axis 4 to complete their motions.
Wmx3Lib_cm.motion.Wait(3)
Wmx3Lib_cm.motion.Wait(4)

# Now move Axis 6 to position 108 with a speed of 900.
posCommand_axis6 = Motion_PosCommand()
posCommand_axis6.profile.type = ProfileType.Trapezoidal
posCommand_axis6.axis = 6
posCommand_axis6.target = 108
posCommand_axis6.profile.velocity = 900
posCommand_axis6.profile.acc = 10000
posCommand_axis6.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis6)
if ret != 0:
    print("StartPos error for Axis 6, code: " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for Axis 6 to finish moving.
Wmx3Lib_cm.motion.Wait(6)
