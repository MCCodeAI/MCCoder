
# Define Axes and IOs
Axes = [5, 6, 3]
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\gpt-4o-M3"
    path_0.fileName = f"65_gpt-4o-M3_Log.txt"

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


    # Axes = [5, 6, 3]
    # Inputs = []
    # Outputs = []

    class AdvancedMotion:
        def __init__(self, lib):
            self.lib = lib

    class AdvMotion_PathIntplWithRotationCommand:
        def __init__(self):
            self.numPoints = 0

        def SetPoint(self, index, point):
            pass

    class AdvMotion_PathIntplWithRotationCommandPoint:
        def __init__(self):
            self.type = None
            self.profile = Profile()
            self.useLocalCenterOfRotation = 0
            self.localCenterOfRotationDirection = 0

        def SetTarget(self, axis, value):
            pass

        def SetLocalCenterOfRotation(self, axis, value):
            pass

    class Profile:
        def __init__(self):
            self.type = None
            self.velocity = 0
            self.acc = 0
            self.dec = 0

    class ProfileType:
        Trapezoidal = 0

    class AdvMotion_PathIntplWithRotationConfiguration:
        def __init__(self):
            self.rotationalAxis = 0
            self.angleCorrectionProfile = Profile()
            self.disableXYRotationalMotion = 0

        def SetAxis(self, axis, value):
            pass

        def SetCenterOfRotation(self, axis, value):
            pass

    class AdvMotion_PathIntplWithRotationState:
        Idle = 0

    def execute_path_interpolation():
        Wmx3Lib_adv = AdvancedMotion(None)

        path = AdvMotion_PathIntplWithRotationCommand()

        conf = AdvMotion_PathIntplWithRotationConfiguration()
        conf.SetAxis(0, 5)  # Axis 5
        conf.SetAxis(1, 6)  # Axis 6
        conf.rotationalAxis = 3  # Rotational axis
        conf.SetCenterOfRotation(0, 80)  # X axis center of rotation position
        conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation position
        conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
        conf.angleCorrectionProfile.velocity = 1000
        conf.angleCorrectionProfile.acc = 2000
        conf.angleCorrectionProfile.dec = 2000
        conf.disableXYRotationalMotion = 1

        path.numPoints = 4

        point = AdvMotion_PathIntplWithRotationCommandPoint()
        point.type = AdvMotion_PathIntplSegmentType.Linear
        point.profile.type = ProfileType.Trapezoidal
        point.profile.velocity = 1000
        point.profile.acc = 2000
        point.profile.dec = 2000
        point.SetTarget(0, 160)
        point.SetTarget(1, 0)
        path.SetPoint(0, point)

        point = AdvMotion_PathIntplWithRotationCommandPoint()
        point.type = AdvMotion_PathIntplSegmentType.Linear
        point.profile.type = ProfileType.Trapezoidal
        point.profile.velocity = 1000
        point.profile.acc = 2000
        point.profile.dec = 2000
        point.SetTarget(0, 160)
        point.SetTarget(1, 160)
        path.SetPoint(1, point)

        point = AdvMotion_PathIntplWithRotationCommandPoint()
        point.type = AdvMotion_PathIntplSegmentType.Linear
        point.profile.type = ProfileType.Trapezoidal
        point.profile.velocity = 1000
        point.profile.acc = 2000
        point.profile.dec = 2000
        point.SetTarget(0, 0)
        point.SetTarget(1, 160)
        path.SetPoint(2, point)

        point = AdvMotion_PathIntplWithRotationCommandPoint()
        point.type = AdvMotion_PathIntplSegmentType.Linear
        point.profile.type = ProfileType.Trapezoidal
        point.profile.velocity = 1000
        point.profile.acc = 2000
        point.profile.dec = 2000
        point.SetTarget(0, 0)
        point.SetTarget(1, 0)
        path.SetPoint(3, point)

        timeoutCounter = 0
        pathStatus = AdvMotion_PathIntplWithRotationState()
        while True:
            if pathStatus == AdvMotion_PathIntplWithRotationState.Idle:
                break
            sleep(0.1)
            timeoutCounter += 1
            if timeoutCounter > 500:
                break
        if timeoutCounter > 500:
            print('PathIntplWithRotation Running timeout.!')
            return

    execute_path_interpolation()


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

