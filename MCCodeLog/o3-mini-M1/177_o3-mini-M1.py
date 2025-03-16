
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

def main():
    # --- Part 1: Axis 10 absolute move to -800 with velocity 600 ---
    # Create and configure the absolute motion command for Axis 10
    pos_cmd = Motion_PosCommand()
    pos_cmd.axis = 10
    pos_cmd.target = -800
    pos_cmd.profile.type = ProfileType.Trapezoidal
    pos_cmd.profile.velocity = 600
    pos_cmd.profile.acc = 10000
    pos_cmd.profile.dec = 10000
    pos_cmd.profile.endVelocity = 600

    ret = Wmx3Lib_cm.motion.StartPos(pos_cmd)
    if ret != 0:
        print("StartPos error for Axis 10 moving to -800:", Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 10 stops moving
    Wmx3Lib_cm.motion.Wait(10)  

    # --- Part 2: Trigger on Axis 10: When DistanceToTarget equals 200, move to 300 at velocity 1000 ---
    # Create and configure the triggered motion command for Axis 10 to change target position to 300
    trig_cmd = Motion_TriggerPosCommand()
    trig_cmd.axis = 10
    trig_cmd.target = 300
    trig_cmd.profile.type = ProfileType.Trapezoidal
    trig_cmd.profile.velocity = 1000
    trig_cmd.profile.acc = 10000
    trig_cmd.profile.dec = 10000
    trig_cmd.profile.endVelocity = 1000

    # Set trigger condition: when the remaining distance to target (DistanceToTarget) on Axis 10 is 200.
    trig_cmd.trigger.triggerType = TriggerType.DistanceToTarget
    trig_cmd.trigger.triggerAxis = 10
    trig_cmd.trigger.triggerValue = 200

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trig_cmd)
    if ret != 0:
        print("StartPos_Trigger error for Axis 10 moving to 300:", Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 10 completes the triggered motion
    Wmx3Lib_cm.motion.Wait(10)

    # --- Part 3: Event for Axis 12: When Axis 10 reaches position 100, move Axis 12 to -50 ---
    # Create and configure the triggered motion command for Axis 12
    trig_cmd_axis12 = Motion_TriggerPosCommand()
    trig_cmd_axis12.axis = 12
    trig_cmd_axis12.target = -50
    trig_cmd_axis12.profile.type = ProfileType.Trapezoidal
    trig_cmd_axis12.profile.velocity = 1000  # chosen velocity; adjust as needed
    trig_cmd_axis12.profile.acc = 10000
    trig_cmd_axis12.profile.dec = 10000
    trig_cmd_axis12.profile.endVelocity = 1000

    # Set trigger condition: when Axis 10 reaches the absolute position of 100.
    # Assuming TriggerType.EqualPos is defined and behaves as required.
    trig_cmd_axis12.trigger.triggerType = TriggerType.EqualPos
    trig_cmd_axis12.trigger.triggerAxis = 10
    trig_cmd_axis12.trigger.triggerValue = 100

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trig_cmd_axis12)
    if ret != 0:
        print("StartPos_Trigger error for Axis 12 moving to -50:", Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait until Axis 12 stops moving
    Wmx3Lib_cm.motion.Wait(12)

if __name__ == "__main__":
    main()
