
# Define Axes and IOs
Axes = [4, 6]
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\DeepSeek-R1-M3"
    path_0.fileName = f"114_DeepSeek-R1-M3_Log.txt"

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


    # Axes = [4, 6]
    # IOInputs = []
    # IOOutputs = []

    # Task 1: Absolute position path interpolation motion for Axis 4 and 6
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntplCommand()

    path.SetAxis(0, 4)
    path.SetAxis(1, 6)

    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 1000
    profile.acc = 10000
    profile.dec = 10000
    path.SetProfile(0, profile)

    path.enableAutoSmooth = 1

    path.numPoints = 6

    positions = [
        (-40, -30, 10),
        (10, -50, 20),
        (-40, -70, 30),
        (10, -90, 40),
        (-40, -110, 50),
        (10, -130, 0)
    ]

    for i in range(6):
        path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
        path.SetTarget(0, i, positions[i][0])
        path.SetTarget(1, i, positions[i][1])
        if i < 5:
            path.SetAutoSmoothRadius(i, positions[i][2])

    ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
    if ret != 0:
        print(f'StartPathIntplPos error: {Wmx3Lib_adv.ErrorToString(ret)}')
        exit()

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 4)
    axes.SetAxis(1, 6)
    Wmx3Lib_cm.motion.Wait_AxisSel(axes)

    # Task 2: API buffer sequence for Axis 4
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    Wmx3Lib_buf.Clear(0)
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # First move
    posCommand.target = 111
    posCommand.profile.velocity = 1000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()

    cond = ApiBufferCondition()
    cond.bufferConditionType = ApiBufferConditionType.RemainingTime
    cond.arg_remainingTime.axis = 4
    cond.arg_remainingTime.timeMilliseconds = 8
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    # Second move
    posCommand.target = 222
    posCommand.profile.velocity = 2000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()

    cond.arg_remainingTime.timeMilliseconds = 9
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    # Third move
    posCommand.target = 333
    posCommand.profile.velocity = 3000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()

    Wmx3Lib_buf.EndRecordBufferChannel()
    Wmx3Lib_buf.Execute(0)
    Wmx3Lib_cm.motion.Wait(4)
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

    # Task 3: E-CAM motion for Axis 4 and 6
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Move Axis 4 to -100
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = -100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()
    Wmx3Lib_cm.motion.Wait(4)

    # Setup E-CAM
    ECAMdata = AdvSync_ECAMData()
    ECAMoption = AdvSync_ECAMOptions()
    ECAMoption.type = AdvSync_ECAMType.Normal
    ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
    ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone

    ECAMdata.masterAxis = 4
    ECAMdata.slaveAxis = 6
    ECAMdata.numPoints = 7
    ECAMdata.options = ECAMoption

    master_pos = [-100, -50, 0, 50, 100, 150, 250]
    slave_pos = [100, 150, 100, 50, 100, 50, 150]

    for i in range(7):
        ECAMdata.SetMasterPos(i, master_pos[i])
        ECAMdata.SetSlavePos(i, slave_pos[i])

    ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
    if ret != 0:
        print(f'StartECAM error: {Wmx3Lib.ErrorToString(ret)}')
        exit()

    # Move Axis 4 to 300
    posCommand.target = 300
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print(f'StartPos error: {Wmx3Lib_cm.ErrorToString(ret)}')
        exit()
    Wmx3Lib_cm.motion.Wait(4)

    # Stop E-CAM
    ret = Wmx3Lib_adv.advSync.StopECAM(0)
    if ret != 0:
        print(f'StopECAM error: {Wmx3Lib.ErrorToString(ret)}')


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

