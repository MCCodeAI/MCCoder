
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Absolute triggered position command for Axis 10:
#
# 1. Start an absolute position command for Axis 10 to move to -800 with a velocity of 600.
# 2. Without waiting (i.e. no wait(axis) here), set up a trigger so that when the remaining distance 
#    for Axis 10 reaches 400, it automatically moves to 300 with a velocity of 1000.
#
# Then:
#
# 3. Set an event that monitors when Axis 10 reaches the position of 100. When that condition is 
#    met, the event triggers an absolute position command for Axis 12 to move to -50. In this case,
#    a wait is used to block further execution until Axis 12 stops moving.
#
# Note: It is assumed that all necessary classes, enumerations, and global objects such as 
# Wmx3Lib_cm, Wmx3Lib_EventCtl, ProfileType, TriggerType, CoreMotionEventInputType, 
# CoreMotionEventOutputType, Motion_PosCommand, Motion_TriggerPosCommand, and CoreMotionEventInput 
# are already defined and available in the runtime environment.

# ----- Absolute Triggered Motion for Axis 10 (No intermediate waiting) -----
# Create the absolute motion command for Axis 10 to move to -800.
posCmd10 = Motion_PosCommand()
posCmd10.axis = 10
posCmd10.profile.type = ProfileType.Trapezoidal
posCmd10.profile.velocity = 600
posCmd10.profile.acc = 10000  # Assumed acceleration value
posCmd10.profile.dec = 10000  # Assumed deceleration value
posCmd10.target = -800

ret = Wmx3Lib_cm.motion.StartPos(posCmd10)
if ret != 0:
    print("StartPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Exit or handle error as needed

# Create the triggered motion command for Axis 10.
# This command sets up a trigger that when the remaining distance for Axis 10 equals 400,
# Axis 10 will move to 300 with a velocity of 1000.
trigPosCmd10 = Motion_TriggerPosCommand()
trigPosCmd10.axis = 10
trigPosCmd10.profile.type = ProfileType.Trapezoidal
trigPosCmd10.profile.velocity = 1000
trigPosCmd10.profile.acc = 10000  # Assumed acceleration value
trigPosCmd10.profile.dec = 10000  # Assumed deceleration value
trigPosCmd10.target = 300
trigPosCmd10.trigger.triggerType = TriggerType.RemainingDistance
trigPosCmd10.trigger.triggerAxis = 10
trigPosCmd10.trigger.triggerValue = 400

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCmd10)
if ret != 0:
    print("StartPos_Trigger error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Exit or handle error as needed

# ----- Event Triggered Motion for Axis 12 (Using wait(axis)) -----
# Create an event input that monitors when Axis 10 reaches the absolute position 100.
eventIN = CoreMotionEventInput()
eventIN.inputFunction = CoreMotionEventInputType.EqualPos
eventIN.equalPos.axis = 10
eventIN.equalPos.pos = 100

# Create the motion command for Axis 12 to move to -50.
posCmd12 = Motion_PosCommand()
posCmd12.axis = 12
posCmd12.profile.type = ProfileType.Trapezoidal
posCmd12.profile.velocity = 600    # Chosen velocity for Axis 12 motion
posCmd12.profile.acc = 10000        # Assumed acceleration value
posCmd12.profile.dec = 10000        # Assumed deceleration value
posCmd12.target = -50

# Create the event output that will start the motion command for Axis 12.
# It is assumed that the event output can be configured to launch a motion command.
eventOut = CoreMotionEventOutput()
eventOut.type = CoreMotionEventOutputType.StartMov
# The motion command associated with the event output is set to posCmd12.
eventOut.posCommand = posCmd12

# Set the event (using event ID 0).
ret, evID = Wmx3Lib_EventCtl.SetEvent(eventIN, eventOut, 0)
if ret != 0:
    print("SetEvent error code: " + str(ret))
    # Exit or handle error as needed

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(0, 1)

# Now wait for Axis 12 to complete its motion.
Wmx3Lib_cm.motion.Wait(12)
