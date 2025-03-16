
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # -----------------------------------------------------------------
    # Step 1: Move Axis 2 to position 2000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 2
    posCommand.target = 2000
    # Set a default velocity; adjust acceleration and deceleration as needed.
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error for Axis 2: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 2 stops. (Blocking wait after a single motion command)
    Wmx3Lib_cm.motion.Wait(2)
    
    # -----------------------------------------------------------------
    # Step 2: Set the input event to monitor if the RemainingTime of Axis 2's movement is 1000ms.
    # (Although the event is configured, in this example we simulate the event by polling.)
    eventIN_Motion = CoreMotionEventInput()
    eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
    eventIN_Motion.remainingTime.axis = 2
    eventIN_Motion.remainingTime.timeMilliseconds = 1000
    eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

    # Polling loop to simulate waiting for the RemainingTime condition.
    # (Assuming that Wmx3Lib_cm.motion.GetRemainingTime(axis) returns the remaining time in ms.)
    while True:
        current_remaining_time = Wmx3Lib_cm.motion.GetRemainingTime(2)
        if current_remaining_time <= 1000:
            break
        time.sleep(0.01)

    # -----------------------------------------------------------------
    # Step 3: Move Axis 1 to position 500 at a speed of 1000.
    posCommand1 = Motion_PosCommand()
    posCommand1.profile.type = ProfileType.Trapezoidal
    posCommand1.axis = 1
    posCommand1.target = 500
    posCommand1.profile.velocity = 1000
    posCommand1.profile.acc = 10000
    posCommand1.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
    if ret != 0:
        print("StartPos error for Axis 1: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 1 stops moving.
    Wmx3Lib_cm.motion.Wait(1)

if __name__ == "__main__":
    main()
