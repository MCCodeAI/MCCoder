
# Define Axes and IOs
Axes = [2]
IOInputs = []
IOOutputs = [3.0, 3.1, 3.2]


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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\DeepSeek-R1-M1"
    path_0.fileName = f"90_DeepSeek-R1-M1_Log.txt"

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


    # Axes = [2]
    # IOInputs = []
    # IOOutputs = [3.0, 3.1, 3.2]

    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    PsoStu = EventControl_PSOStatus()
    PsoOut = EventControl_PSOOutput()
    PsoCompSor = EventControl_ComparatorSource()

    # Set the comparison axis 2 command position output to 3.0.
    PsoOut.outputType = EventControl_PSOOutputType.IOOutput
    PsoOut.byteAddress = 3
    PsoOut.bitAddress = 0
    PsoOut.invert = 0
    PsoCompSor.sourceType = EventControl_ComparatorSourceType.PosCommand
    PsoCompSor.axis = 2
    # The comparison position values are: 12, 24, 36.
    point = [12, 24, 36]

    # Create a command value of axis 2 moves a distance of 48 from the current position at a speed of 1000, with an acceleration and deceleration of 10000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 2
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.target = 48

    # Set parameters for a position synchronous output channel 0. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(0, EventControl_ComparisonType.Equal, PsoCompSor, PsoOut, 0)
    # Output to 3.1
    PsoOut.byteAddress = 3
    PsoOut.bitAddress = 1
    # Set parameters for a position synchronous output channel 1. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(1, EventControl_ComparisonType.PositiveDirection, PsoCompSor, PsoOut, 0)
    # Output to 3.2
    PsoOut.byteAddress = 3
    PsoOut.bitAddress = 2
    # Set parameters for a position synchronous output channel 2. A position synchronous output channel is able to output an output signal when certain conditions, such as an axis reaching a certain position, are met.
    Wmx3Lib_EventCtl.SetPSOConfig(2, EventControl_ComparisonType.NegativeDirection, PsoCompSor, PsoOut, 0)

    # Set multiple data points for a position synchronous output channel.
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(0, 3, point)
    if ret != 0:
        print('SetPSOMultipleData0 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(1, 3, point)
    if ret != 0:
        print('SetPSOMultipleData1 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    ret = Wmx3Lib_EventCtl.SetPSOMultipleData(2, 3, point)
    if ret != 0:
        print('SetPSOMultipleData2 to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(0)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(0)
        sleep(0.01)
    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(1)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(1)
        sleep(0.01)
    # Get the channel status
    ret, PsoStu = Wmx3Lib_EventCtl.GetPSOStatus(2)
    # If the channel is already open, execute StopPSO.
    if PsoStu.enabled == 1:
        Wmx3Lib_EventCtl.StopPSO(2)
        sleep(0.01)

    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(0)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(1)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    # StartPSO
    ret = Wmx3Lib_EventCtl.StartPSO(2)
    if ret != 0:
        print('StartPSO to off error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))

    # Execute command to move to a specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    Wmx3Lib_cm.motion.Wait(2)

    # StopPSO
    Wmx3Lib_EventCtl.StopPSO(0)
    Wmx3Lib_EventCtl.StopPSO(1)
    Wmx3Lib_EventCtl.StopPSO(2)


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

