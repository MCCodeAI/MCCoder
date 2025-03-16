
# Axes = [1, 3]
# IOInputs = []
# IOOutputs = []

from time import sleep

def main():
    # ------------------------------
    # 1. Jog Axis 3 for 0.5 seconds with a velocity of 90.
    # ------------------------------
    jogCommand = Motion_JogCommand()
    jogCommand.profile.type = ProfileType.Trapezoidal
    jogCommand.axis = 3
    jogCommand.profile.velocity = 90
    jogCommand.profile.acc = 10000
    jogCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartJog(jogCommand)
    if ret != 0:
        print('StartJog error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Jog for 0.5 seconds.
    sleep(0.5)
    Wmx3Lib_cm.motion.Stop(3)
    Wmx3Lib_cm.motion.Wait(3)

    # ------------------------------
    # 2. Get Axis 3 status and check the Actual Position.
    # ------------------------------
    # Assuming GetStatus returns (ret, status) where status.actualPos is available.
    ret, status = Wmx3Lib_cm.motion.GetStatus(3)
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Determine target based on the actual position.
    if status.actualPos > 20:
        targetPos = 150
    else:
        targetPos = -150

    # Move Axis 3 to the corresponding target position.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 3
    posCommand.target = targetPos
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(3)

    # ------------------------------
    # 3. Start an absolute linear interpolation for Axes 1 and 3 
    #    to position (100, 0) with a velocity of 1000.
    # ------------------------------
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    # Map command indices to actual axis numbers:
    #   index 0 -> Axis 1, index 1 -> Axis 3.
    lin.SetAxis(0, 1)
    lin.SetAxis(1, 3)

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    # Set the absolute target positions:
    #   For Axis 1: 100, and for Axis 3: 0.
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 0)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until both Axis 1 and Axis 3 have completed their motion.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
