
# Axes = [0, 4]
# IOInputs = []
# IOOutputs = []

# Start a relative motion for Axis 0 with a relative distance of 110.
# This motion is used only as the trigger condition reference.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 110
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error on Axis 0, error code:', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed (e.g., exit or return)
else:
    # Wait until Axis 0 completes its relative move.
    Wmx3Lib_cm.motion.Wait(0)

# Set up a triggered relative motion command for Axis 4.
# This command will start once Axis 0 has 30 units remaining to its target.
tgrPosCommand = Motion_TriggerPosCommand()
tgrPosCommand.profile.type = ProfileType.Trapezoidal
tgrPosCommand.axis = 4
tgrPosCommand.target = 100
tgrPosCommand.profile.velocity = 1000
tgrPosCommand.profile.acc = 10000
tgrPosCommand.profile.dec = 10000

# Create and configure the trigger.
trigger = Trigger()
trigger.triggerAxis = 0                # Monitor Axis 0.
trigger.triggerType = TriggerType.RemainingDistance  # Trigger based on remaining distance.
trigger.triggerValue = 30              # Trigger when remaining distance equals 30.
tgrPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartMov_Trigger(tgrPosCommand)
if ret != 0:
    print('StartMov_Trigger error on Axis 4, error code:', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed
else:
    # After starting the triggered motion command, wait for a short period.
    # (Do not wait in the middle of continuous motion.)
    Wmx3Lib_cm.motion.Wait(1)

# Wait for all active motions (Axis 0 and Axis 4) to complete.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 4)

ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code:', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
    # Handle error as needed
