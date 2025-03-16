
# Axes = [5, 8]
# IOInputs = []
# IOOutputs = []

def main():
    # ---------------------------
    # Step 1: Move Axis 5 to 200
    # ---------------------------
    # Create an absolute position command for Axis 5 with target 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal  # Using a trapezoidal profile for this motion.
    posCommand.axis = 5
    posCommand.target = 200
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos (Axis 5 to 200) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 5 finishes moving.
    Wmx3Lib_cm.motion.Wait(5)

    # --------------------------------------------------
    # Step 2: Read status of Axis 5 and conditionally move
    #         to position 50 if Pos Cmd equals 200
    # --------------------------------------------------
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus (for Axis 5) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Checking Axis 5 "Pos Cmd" value from the status.
    currentPosCmd = CmStatus.GetAxesStatus(5).posCmd
    print('Axis 5 Pos Cmd:', currentPosCmd)

    if currentPosCmd == 200:
        # Create an absolute position command for Axis 5 to move to 50.
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 5
        posCommand.target = 50
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos (Axis 5 to 50) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until Axis 5 finishes moving.
        Wmx3Lib_cm.motion.Wait(5)
    else:
        print('Axis 5 Pos Cmd is not 200; no further move command issued.')

    # ---------------------------------------------------------------
    # Step 3: Move Axis 8 to position 99 at speed 1000 using a 
    #         TimeAccJerkRatio profile.
    # ---------------------------------------------------------------
    posCommand = Motion_PosCommand()
    # Note: ProfileType.TimeAccJerkRatio is used per question specification.
    posCommand.profile.type = ProfileType.TimeAccJerkRatio
    posCommand.axis = 8
    posCommand.target = 99
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 5000    # Acceleration value chosen arbitrarily
    posCommand.profile.dec = 5000    # Deceleration value chosen arbitrarily

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos (Axis 8 to 99) error code:', ret, Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 8 finishes moving.
    Wmx3Lib_cm.motion.Wait(8)

if __name__ == '__main__':
    main()
