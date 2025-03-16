
# Define Axes and IOs
Axes = [2, 5]
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
    path_0.fileName = f"62_o3-mini-M3_Log.txt"

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


    # Axes = [2, 5]
    # IOInputs = []
    # IOOutputs = []

    # Create an instance for advanced motion control (assuming AdvancedMotion and related classes are already defined)
    advMotionCtrl = AdvancedMotion(Wmx3Lib)

    # Create a new path interpolation command
    path = AdvMotion_PathIntplCommand()

    # Set the two axes: first coordinate (X) is Axis 2, second coordinate (Y) is Axis 5
    path.SetAxis(0, 2)
    path.SetAxis(1, 5)

    # Specify that a distinct motion profile is used for each segment
    path.enableConstProfile = 0

    # Total number of segments to execute
    path.numPoints = 8

    # 1st segment: linear interpolation to (50, 0) with velocity and end velocity = 1000
    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 50)   # Axis 2 target
    path.SetTarget(1, 0, 0)    # Axis 5 target

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 1000
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 1000
    path.SetProfile(0, profile)

    # 2nd segment: clockwise circular interpolation to (75, 25) with center at (50, 25), velocity and end velocity = 900
    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, 75)   # Axis 2 target
    path.SetTarget(1, 1, 25)   # Axis 5 target
    path.SetCenterPos(0, 1, 50) # Axis 2 center
    path.SetCenterPos(1, 1, 25) # Axis 5 center
    path.SetDirection(1, 1)    # 1 for clockwise

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 900
    path.SetProfile(1, profile)

    # 3rd segment: linear interpolation to (75, 50) with velocity and end velocity = 800
    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 75)   # Axis 2 target
    path.SetTarget(1, 2, 50)   # Axis 5 target

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(2, profile)

    # 4th segment: clockwise circular interpolation to (50, 75) with center at (50, 50), velocity and end velocity = 700
    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, 50)   # Axis 2 target
    path.SetTarget(1, 3, 75)   # Axis 5 target
    path.SetCenterPos(0, 3, 50) # Axis 2 center
    path.SetCenterPos(1, 3, 50) # Axis 5 center
    path.SetDirection(3, 1)    # 1 for clockwise

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(3, profile)

    # 5th segment: linear interpolation to (0, 75) with velocity and end velocity = 600
    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 0)    # Axis 2 target
    path.SetTarget(1, 4, 75)   # Axis 5 target

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 600
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 600
    path.SetProfile(4, profile)

    # 6th segment: clockwise circular interpolation to (-25, 50) with center at (0, 50), velocity and end velocity = 700
    path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 5, -25)  # Axis 2 target
    path.SetTarget(1, 5, 50)   # Axis 5 target
    path.SetCenterPos(0, 5, 0)  # Axis 2 center
    path.SetCenterPos(1, 5, 50) # Axis 5 center
    path.SetDirection(5, 1)    # 1 for clockwise

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 700
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 700
    path.SetProfile(5, profile)

    # 7th segment: linear interpolation to (-25, 25) with velocity and end velocity = 800
    path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 6, -25)  # Axis 2 target
    path.SetTarget(1, 6, 25)   # Axis 5 target

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 800
    profile.acc = 10000
    profile.dec = 10000
    profile.endVelocity = 800
    path.SetProfile(6, profile)

    # 8th segment: clockwise circular interpolation to (0, 0) with center at (0, 25) with velocity = 900
    path.SetType(7, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 7, 0)    # Axis 2 target
    path.SetTarget(1, 7, 0)    # Axis 5 target
    path.SetCenterPos(0, 7, 0)  # Axis 2 center
    path.SetCenterPos(1, 7, 0 + 25) # Axis 5 center (using (0,25))
    path.SetDirection(7, 1)    # 1 for clockwise

    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 900
    profile.acc = 10000
    profile.dec = 10000
    # End velocity is not specified for segment 8, so we'll omit it.
    path.SetProfile(7, profile)

    # Start the path interpolation absolute position motion command
    ret = advMotionCtrl.advMotion.StartPathIntplPos(path)
    if ret != 0:
        print('StartPathIntplPos error code is ' + str(ret) + ': ' + advMotionCtrl.ErrorToString(ret))
        # Early exit on error
        exit(1)

    # Wait for the motion to complete on both Axis 2 and Axis 5
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 2)
    axes.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
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

