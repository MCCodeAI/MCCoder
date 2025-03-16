
# Define Axes and IOs
Axes = [3, 6]
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M3"
    path_0.fileName = f"53_o3-mini-M3_Log.txt"

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


    # Axes = [3, 6]
    # IOInputs = []
    # IOOutputs = []

    # Create a PVT interpolation command for Axis 3 and Axis 6 with 5 points.
    # Each point is provided in the format:
    # (Position for Axis 3, Velocity for Axis 3, Time for Axis 3, Position for Axis 6, Velocity for Axis 6, Time for Axis 6)
    #
    # Point definitions:
    #   Point 0: (0, 0, 0) and (0, 0, 0)
    #   Point 1: (10, 100, 100) and (20, 200, 100)
    #   Point 2: (20, 200, 200) and (60, 400, 200)
    #   Point 3: (30, 100, 300) and (100, 200, 300)
    #   Point 4: (60, 0, 400) and (80, 0, 400)

    # Create a PVT interpolation command object (assumed to be provided by the motion control library)
    pvti = Motion_PVTIntplCommand()

    # Two separate PVT point structures for Axis 3 and Axis 6
    pvtparameter_axis3 = Motion_PVTPoint()
    pvtparameter_axis6 = Motion_PVTPoint()

    # Set up the command for two axes: Axis 3 and Axis 6
    pvti.axisCount = 2
    pvti.SetAxis(0, 3)  # Map index 0 to Axis 3
    pvti.SetAxis(1, 6)  # Map index 1 to Axis 6

    # Specify that there will be 5 points for each axis
    pvti.SetPointCount(0, 5)  # For Axis 3
    pvti.SetPointCount(1, 5)  # For Axis 6

    # -- Define each PVT point --
    # Point 0
    pvtparameter_axis3.pos = 0
    pvtparameter_axis3.velocity = 0
    pvtparameter_axis3.timeMilliseconds = 0
    pvtparameter_axis6.pos = 0
    pvtparameter_axis6.velocity = 0
    pvtparameter_axis6.timeMilliseconds = 0
    pvti.SetPoints(0, 0, pvtparameter_axis3)
    pvti.SetPoints(1, 0, pvtparameter_axis6)

    # Point 1
    pvtparameter_axis3.pos = 10
    pvtparameter_axis3.velocity = 100
    pvtparameter_axis3.timeMilliseconds = 100
    pvtparameter_axis6.pos = 20
    pvtparameter_axis6.velocity = 200
    pvtparameter_axis6.timeMilliseconds = 100
    pvti.SetPoints(0, 1, pvtparameter_axis3)
    pvti.SetPoints(1, 1, pvtparameter_axis6)

    # Point 2
    pvtparameter_axis3.pos = 20
    pvtparameter_axis3.velocity = 200
    pvtparameter_axis3.timeMilliseconds = 200
    pvtparameter_axis6.pos = 60
    pvtparameter_axis6.velocity = 400
    pvtparameter_axis6.timeMilliseconds = 200
    pvti.SetPoints(0, 2, pvtparameter_axis3)
    pvti.SetPoints(1, 2, pvtparameter_axis6)

    # Point 3
    pvtparameter_axis3.pos = 30
    pvtparameter_axis3.velocity = 100
    pvtparameter_axis3.timeMilliseconds = 300
    pvtparameter_axis6.pos = 100
    pvtparameter_axis6.velocity = 200
    pvtparameter_axis6.timeMilliseconds = 300
    pvti.SetPoints(0, 3, pvtparameter_axis3)
    pvti.SetPoints(1, 3, pvtparameter_axis6)

    # Point 4
    pvtparameter_axis3.pos = 60
    pvtparameter_axis3.velocity = 0
    pvtparameter_axis3.timeMilliseconds = 400
    pvtparameter_axis6.pos = 80
    pvtparameter_axis6.velocity = 0
    pvtparameter_axis6.timeMilliseconds = 400
    pvti.SetPoints(0, 4, pvtparameter_axis3)
    pvti.SetPoints(1, 4, pvtparameter_axis6)

    # Send the PVT interpolation command to start the motion.
    ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
    if ret != 0:
        print('StartPVT_Intpl error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
        # Wait until motion is complete for both Axis 3 and Axis 6.
        axisSel = AxisSelection()
        axisSel.axisCount = 2
        axisSel.SetAxis(0, 3)
        axisSel.SetAxis(1, 6)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
        if ret != 0:
            print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        else:
            print('PVT interpolation motion on Axis 3 and Axis 6 completed successfully.')


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

