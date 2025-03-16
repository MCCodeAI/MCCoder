
# Define Axes and IOs
Axes = [2, 9]
IOInputs = []
IOOutputs = []


#WMX3 python library
from WMX3ApiPython import *
from time import *


INFINITE = int(0xFFFFFFFF)

def main():
    Wmx3Lib = WMX3Api()
    CmStatus = CoreMotionStatus()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    print('Program begin.')
    sleep(0.1)

    # Create devices. 
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret!=0:
        print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Set Device Name.
    Wmx3Lib.SetDeviceName('WMX3initTest')

    # Start Communication.
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret!=0:
        print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        return

    # Import and set all the preset motion parameters.
    ret=Wmx3Lib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
    if ret != 0:
        print('ImportAndSetAll Parameters error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    sleep(0.5)
 
    # Clear alarms, set servos on, and perform homing for Axes
    for axis in Axes:
        # Clear the amplifier alarm
        timeoutCounter = 0
        while True:
            # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if not CmStatus.GetAxesStatus(axis).ampAlarm:
                break
            ret = Wmx3Lib_cm.axisControl.ClearAmpAlarm(axis)
            sleep(0.5)
            timeoutCounter += 1
            if timeoutCounter > 5:
                break
        if timeoutCounter > 5:
            print(f'Clear axis {axis} alarm fails!')
            return

        # Set servo on for Axis
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 1)
        timeoutCounter = 0
        while True:
            # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if (CmStatus.GetAxesStatus(axis).servoOn):
                break
            sleep(0.4)
            timeoutCounter += 1
            if (timeoutCounter > 5):
                break
        if (timeoutCounter > 5):
            print('Set servo on for axis {axis} fails!')
            return

        # Sleep is a must between SetServoOn and Homing
        sleep(0.1)

        # Homing
        homeParam = Config_HomeParam()
        ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)

        homeParam.homeType = Config_HomeType.CurrentPos

        # SetHomeParam -> First return value: Error code, Second return value: param error
        ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)

        ret = Wmx3Lib_cm.home.StartHome(axis)
        if ret != 0:
            print(f'StartHome before log error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        Wmx3Lib_cm.motion.Wait(axis)

    # <logon---------------------------------------------------------------------------                                                                 
    WMX3Log = Log(Wmx3Lib)
                                 
    # Stop log just in case logging is on.
    ret = WMX3Log.StopLog(0)
    sleep(0.2)
                                     
    axislist = Axes                           
    num = len(axislist)

    # Set Axis numbers and control variables of log
    cmLogIn_0 = CoreMotionLogInput()
    cmLogIn_0.axisSelection.axisCount = num
    for i in range(0, num):
        cmLogIn_0.axisSelection.SetAxis(i, axislist[i])

    # Control variables to log
    cmLogIn_0.axisOptions.commandPos = 1
    cmLogIn_0.axisOptions.feedbackPos = 0
    cmLogIn_0.axisOptions.commandVelocity = 0
    cmLogIn_0.axisOptions.feedbackVelocity = 0

    # Set up log time
    option = LogChannelOptions()
    option.samplingPeriodInCycles = 1
    option.samplingTimeMilliseconds = 60000
    option.precision = 3

    ret=WMX3Log.SetLogOption(0, option)
    if ret!=0:
        print('SetLogOption error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        ret = WMX3Log.StopLog(0)
        sleep(0.2)
        ret=WMX3Log.SetLogOption(0, option)
    sleep(0.1)

    ret = WMX3Log.SetCustomLog(0,cmLogIn_0)
    if ret!=0:
        print('SetCustomLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)

    
    # IOInputs and IOOutputs
    Inputslist = IOInputs
    Outputslist = IOOutputs

    # Initialize lists to hold IOAddress instances
    InputIOAddresses = [IOAddress() for _ in range(len(Inputslist))]
    OutputIOAddresses = [IOAddress() for _ in range(len(Outputslist))]

    # Set properties for InputIOAddresses
    for i in range(len(Inputslist)):
        integer_part, fractional_part = str(Inputslist[i]).split('.')
        InputIOAddresses[i].byte = int(integer_part)
        InputIOAddresses[i].bit = int(fractional_part)
        InputIOAddresses[i].size = 1
        inputSize = 1 #temp
        break

    # Set properties for OutputIOAddresses
    for i in range(len(Outputslist)):
        integer_part, fractional_part = str(Outputslist[i]).split('.')
        OutputIOAddresses[i].byte = int(integer_part)
        OutputIOAddresses[i].bit = int(fractional_part)
        OutputIOAddresses[i].size = 1
        outputSize = 1 #temp
        break

    if len(Inputslist) == 0:      #temp
        InputIOAddresses = [IOAddress() for _ in range(1)]
        InputIOAddresses[0].byte = 0
        InputIOAddresses[0].bit = 0
        InputIOAddresses[0].size = 1
        inputSize = 1
    if len(Outputslist) == 0:
        OutputIOAddresses = [IOAddress() for _ in range(1)]
        OutputIOAddresses[0].byte = 0
        OutputIOAddresses[0].bit = 0
        OutputIOAddresses[0].size = 1
        outputSize = 1


    # Call SetIOLog function
    ret = WMX3Log.SetIOLog(0, InputIOAddresses[0], inputSize, OutputIOAddresses[0], outputSize) 
    if ret != 0:
        print('SetIOLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
        
    # Set log file address
    path_0 = LogFilePath()
    WMX3Log.GetLogFilePath(0)
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M1"
    path_0.fileName = f"109_o3-mini-M1_Log.txt"

    ret = WMX3Log.SetLogFilePath(0, path_0)
    if ret!=0:
        print('SetLogFilePath error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return


    # Start log
    ret = WMX3Log.StartLog(0)
    if ret!=0:
        print('StartLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
        return
    sleep(0.1)
    # --------------------------------------------------------------------------- 
    # logon>  


    # Axes = [2, 9]
    # IOInputs = []
    # IOOutputs = []

    # -----------------------------------------------------------------------------
    # This script executes a series of motion commands:
    # 1. An absolute path interpolation that includes 4 segments on Axes 2 and 9.
    #    • Segment 0: Linear interpolation to (-50, -50)
    #    • Segment 1: Clockwise circular interpolation to (-100, -100) with center (0, 0)
    #    • Segment 2: Linear interpolation to (50, 50)
    #    • Segment 3: Counterclockwise circular interpolation to (-100, -100) with center (0, 0)
    #
    # 2. An absolute linear interpolation command to move Axes 2 and 9 to (100, 200)
    #    with a velocity of 1000.
    #
    # 3. A single clockwise circular interpolation command for Axes 2 and 9 with a center
    #    at (100, 100), an arc length of 180, and a velocity of 1200.
    #
    # 4. A direct move (e.g. point-to-point) command to move Axes 2 and 9 to (100, 200).
    #
    # Each independent motion command is followed by waiting for the involved axes to become idle.
    # -----------------------------------------------------------------------------

    # Step 1: Absolute position path interpolation on Axes 2 and 9 with velocity 1200.
    adv = AdvancedMotion(Wmx3Lib)
    path = AdvMotion_PathIntplCommand()

    # Set the axes (order: axis index 0 is axis 2, index 1 is axis 9)
    path.SetAxis(0, 2)
    path.SetAxis(1, 9)

    # Use a single (constant) motion profile for the entire path.
    path.enableConstProfile = 1
    path.profile = Profile()
    path.profile.type = ProfileType.Trapezoidal
    path.profile.velocity = 1200
    path.profile.acc = 10000
    path.profile.dec = 10000

    path.numPoints = 4

    # Segment 0: Linear interpolation to (-50, -50)
    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, -50)  # For axis index 0 (axis 2): -50
    path.SetTarget(1, 0, -50)  # For axis index 1 (axis 9): -50

    # Segment 1: Clockwise circular interpolation to (-100, -100) with center (0,0)
    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, -100)
    path.SetTarget(1, 1, -100)
    path.SetCenterPos(0, 1, 0)
    path.SetCenterPos(1, 1, 0)
    # Clockwise: use -1 for direction
    path.SetDirection(1, -1)

    # Segment 2: Linear interpolation to (50, 50)
    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 50)
    path.SetTarget(1, 2, 50)

    # Segment 3: Counterclockwise circular interpolation to (-100, -100) with center (0,0)
    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, -100)
    path.SetTarget(1, 3, -100)
    path.SetCenterPos(0, 3, 0)
    path.SetCenterPos(1, 3, 0)
    # Counterclockwise: use 1 for direction
    path.SetDirection(3, 1)

    ret = adv.advMotion.StartPathIntplPos(path)
    if ret != 0:
        print('StartPathIntplPos error code is ' + str(ret) + ': ' + adv.ErrorToString(ret))
        exit(1)

    # Wait until Axes 2 and 9 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Step 2: Absolute position linear interpolation to (100, 200) on Axes 2 and 9 with velocity 1000.
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    lin.SetAxis(0, 2)
    lin.SetAxis(1, 9)

    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000
    lin.profile.acc = 10000
    lin.profile.dec = 10000

    # Set absolute targets: Axis 2 to 100, Axis 9 to 200.
    lin.SetTarget(0, 100)
    lin.SetTarget(1, 200)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print('StartLinearIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait for this move to complete.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Step 3: Clockwise circular interpolation on Axes 2 and 9.
    # Assume there exists a command class for circular interpolation.
    circ = Motion_CircularIntplCommand()
    circ.axisCount = 2
    circ.SetAxis(0, 2)
    circ.SetAxis(1, 9)

    # Set the center position to (100, 100) and arc length to 180.
    circ.centerX = 100  # For axis index 0 (axis 2)
    circ.centerY = 100  # For axis index 1 (axis 9)
    circ.arcLength = 180

    circ.profile.type = ProfileType.Trapezoidal
    circ.profile.velocity = 1200
    circ.profile.acc = 10000
    circ.profile.dec = 10000

    # Direction: Clockwise interpolation implies using -1 for the direction inside the command.
    circ.direction = -1

    ret = Wmx3Lib_cm.motion.StartCircularIntplPos(circ)
    if ret != 0:
        print('StartCircularIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait for the circular interpolation motion to complete.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Step 4: Move Axes 2 and 9 to (100, 200) using a point-to-point (PTP) command.
    ptp = Motion_PTPCommand()
    ptp.axisCount = 2
    ptp.SetAxis(0, 2)
    ptp.SetAxis(1, 9)

    # Set the target positions.
    ptp.SetTarget(0, 100)
    ptp.SetTarget(1, 200)

    # Start the point-to-point move.
    ret = Wmx3Lib_cm.motion.StartPTPPos(ptp)
    if ret != 0:
        print('StartPTPPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait for the final motion to complete.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 2)
    axisSel.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)


# <logoff --------------------------------------------------------------------------- 
    sleep(0.1)                                                                    
    # Stop log
    ret = WMX3Log.StopLog(0)
    if ret!=0:
        print('StopLog error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))       
    sleep(0.1) 

    # for axisNo in axislist:                                
    #     ret = Wmx3Lib_cm.home.StartHome(axisNo)
    #     if ret!=0:
    #         print('StartHome after log error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            
    #     Wmx3Lib_cm.motion.Wait(axisNo)      
    #  -----------------------------------                                   
    # logoff>    
                                     
                
    # Set servo off for Axes
    for axis in Axes:
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
        if ret != 0:
            print(f'SetServoOn to off error code for axis {axis} is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            

    # Stop Communication.
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret!=0:
        print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        

    # Close Device.
    ret = Wmx3Lib.CloseDevice()
    if ret!=0:
        print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        

    print('Program End.')

if __name__ == '__main__':
    main()

