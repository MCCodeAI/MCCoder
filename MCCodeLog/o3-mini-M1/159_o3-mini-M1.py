
# Axes = [5]
# IOInputs = []
# IOOutputs = []

def main():
    # Create a command to move Axis 5 to an absolute position of 200.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 5
    posCommand.target = 200
    # Define nominal profile parameters.
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("Error moving Axis 5 to 200: code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis stops moving.
    Wmx3Lib_cm.motion.Wait(5)

    # Get the status of Axis 5
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print("Error getting status for Axis 5: code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Extract the Pos Cmd status.
    axisStatus = CmStatus.GetAxesStatus(5)
    pos_cmd = axisStatus.posCmd
    print("Axis 5 Pos Cmd :", pos_cmd)

    # If the Pos Cmd equals 200, then move Axis 5 to an absolute position of 50.
    if pos_cmd == 200:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 5
        posCommand.target = 50
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 1000
        posCommand.profile.dec = 1000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print("Error moving Axis 5 to 50: code " + str(ret) + " - " + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait until the axis stops moving.
        Wmx3Lib_cm.motion.Wait(5)

if __name__ == '__main__':
    main()
