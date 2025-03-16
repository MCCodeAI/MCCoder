
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Execute an absolute triggered position command for Axis 10.
# First, start an absolute position command for Axis 10 to move to 800 with a velocity of 600.
# When the remaining distance (i.e. distance to target) becomes 200, trigger a motion command for Axis 10 to move to 300 with a velocity of 1000.
# No wait is used between these Axis10 motions.

pos_cmd_10 = Motion_PosCommand()
trig_cmd_10 = Motion_TriggerPosCommand()

# Configure the primary motion command for Axis 10.
pos_cmd_10.axis = 10
pos_cmd_10.profile.type = ProfileType.Trapezoidal
pos_cmd_10.profile.velocity = 600
pos_cmd_10.profile.acc = 10000
pos_cmd_10.profile.dec = 10000
pos_cmd_10.target = 800

ret = Wmx3Lib_cm.motion.StartPos(pos_cmd_10)
if ret != 0:
    print("StartPos error for Axis 10: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally exit or handle the error

# Configure the triggered motion command for Axis 10.
trig_cmd_10.axis = 10
trig_cmd_10.profile.type = ProfileType.Trapezoidal
trig_cmd_10.profile.velocity = 1000
trig_cmd_10.profile.acc = 10000
trig_cmd_10.profile.dec = 10000
trig_cmd_10.target = 300

# Set up trigger: when the remaining distance of Axis 10 reaches 200,
# (i.e. when Axis 10’s current position has advanced enough so that distance to target = 200)
# the triggered command will be executed.
trigger_obj_10 = Trigger()
trigger_obj_10.triggerAxis = 10
trigger_obj_10.triggerType = TriggerType.RemainingDistance
trigger_obj_10.triggerValue = 200

trig_cmd_10.trigger = trigger_obj_10

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trig_cmd_10)
if ret != 0:
    print("StartPos_Trigger error for Axis 10: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally exit or handle the error

# Now, set an event to trigger the movement of Axis 12.
# When Axis 10 moves to the position of 400, trigger Axis 12 to move to position 80.
# Assuming Axis 10’s target is 800, when Axis 10 reaches 400 the remaining distance will be 800 - 400 = 400.
# We use this fact to set the trigger condition.
# This triggered command for Axis 12 uses a blocking wait (via wait(axis)) after the command is issued.

trig_cmd_12 = Motion_TriggerPosCommand()
trig_cmd_12.axis = 12
trig_cmd_12.profile.type = ProfileType.Trapezoidal
# As no velocity was specified for Axis 12, we choose a profile. Here, for demonstration, velocity is set to 600.
trig_cmd_12.profile.velocity = 600
trig_cmd_12.profile.acc = 10000
trig_cmd_12.profile.dec = 10000
trig_cmd_12.target = 80

# Set the trigger so that when Axis 10's remaining distance equals 400 (i.e. its position reaches 400 assuming starting at 0 and target 800),
# the command on Axis 12 is triggered.
trigger_obj_12 = Trigger()
trigger_obj_12.triggerAxis = 10
trigger_obj_12.triggerType = TriggerType.RemainingDistance
trigger_obj_12.triggerValue = 400

trig_cmd_12.trigger = trigger_obj_12

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trig_cmd_12)
if ret != 0:
    print("StartPos_Trigger error for Axis 12: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Optionally exit or handle the error

# Wait until Axis 12 motion completes (blocking wait for Axis 12 to become idle).
ret = Wmx3Lib_cm.motion.Wait(12)
if ret != 0:
    print("Wait error for Axis 12: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
