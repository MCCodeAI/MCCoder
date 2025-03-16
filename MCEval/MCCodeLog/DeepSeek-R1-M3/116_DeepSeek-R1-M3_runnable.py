
# Define Axes and IOs
Axes = [6, 7, 8]
IOInputs = []
IOOutputs = [6.7]


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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\DeepSeek-R1-M3"
    path_0.fileName = f"116_DeepSeek-R1-M3_Log.txt"

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


    # Axes = [6, 7, 8]
    # IOInputs = []
    # IOOutputs = [6.7]

    # Task 1: Move Axis 6 to 20 with trapezoidal profile
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 20
    posCommand.profile.velocity = 900
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error code for Axis 6: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    Wmx3Lib_cm.motion.Wait(6)

    # Task 2: Set output 6.7 to 1, sleep, then 0
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(6, 7, 1)
    if ret != 0:
        print(f'SetOutBit error setting 6.7 to 1: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
        return

    sleep(0.1)

    ret = Wmx3Lib_Io.SetOutBit(6, 7, 0)
    if ret != 0:
        print(f'SetOutBit error setting 6.7 to 0: {ret} - {Wmx3Lib_Io.ErrorToString(ret)}')
        return

    # Task 3: Move Axis 7 to 30
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 7
    posCommand.target = 30
    posCommand.profile.velocity = 1000  # Default assumption
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error code for Axis 7: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    Wmx3Lib_cm.motion.Wait(7)

    # Task 4: Linear interpolate Axis 7 & 8 to (40, 50)
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 2
    lin.SetAxis(0, 7)
    lin.SetAxis(1, 8)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1000  # Default assumption
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    lin.SetTarget(0, 40)
    lin.SetTarget(1, 50)

    ret = Wmx3Lib_cm.motion.StartLinearIntplPos(lin)
    if ret != 0:
        print(f'StartLinearIntplPos error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 7)
    axisSel.SetAxis(1, 8)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    # Task 5: Clockwise circular interpolation for Axis 6 & 7
    cir = Motion_CenterAndLengthCircularIntplCommand()
    cir.SetAxis(0, 6)
    cir.SetAxis(1, 7)
    cir.SetCenterPos(0, 50)
    cir.SetCenterPos(1, 50)
    cir.clockwise = 1
    cir.arcLengthDegree = 360
    cir.profile.type = ProfileType.Trapezoidal
    cir.profile.velocity = 1000  # Default assumption
    cir.profile.acc = 10000
    cir.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(cir)
    if ret != 0:
        print(f'StartCircularIntplPos error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 6)
    axisSel.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print(f'Wait_AxisSel error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    # Task 6: Establish sync control and move Axis 6 to 60
    ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
    if ret != 0:
        print(f'SetSyncMasterSlave error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 60
    posCommand.profile.velocity = 900  # Same as Task 1
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error for Axis 6 sync move: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return

    Wmx3Lib_cm.motion.Wait(6)

    ret = Wmx3Lib_cm.sync.ResolveSync(7)
    if ret != 0:
        print(f'ResolveSync error: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
        return


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

