
# Define Axes and IOs
Axes = [2, 4, 5]
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\gpt-4o-M1"
    path_0.fileName = f"64_gpt-4o-M1_Log.txt"

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


    # Axes = [2, 4, 5]
    # IOInputs = []
    # IOOutputs = []

    class AdvancedMotion:
        def __init__(self, lib):
            self.lib = lib

    class AdvMotion_PathIntpl3DCommand:
        def __init__(self):
            self.numPoints = 0
            self.enableConstProfile = 0

        def SetAxis(self, index, axis):
            pass

        def SetProfile(self, index, profile):
            pass

        def SetType(self, index, segment_type):
            pass

        def SetTarget(self, axis, index, value):
            pass

        def SetCircleIntermediateTarget(self, axis, index, value):
            pass

    class Profile:
        def __init__(self):
            self.type = None
            self.velocity = 0
            self.acc = 0
            self.dec = 0

    class ProfileType:
        Trapezoidal = 0

    class AdvMotion_PathIntplSegmentType:
        Linear = 0
        Circular = 1

    class AxisSelection:
        def __init__(self):
            self.axisCount = 0

        def SetAxis(self, index, axis):
            pass

    class Wmx3Lib:
        pass

    class Wmx3Lib_cm:
        class motion:
            @staticmethod
            def Wait_AxisSel(axes):
                return 0

    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    path = AdvMotion_PathIntpl3DCommand()

    path.SetAxis(0, 2)
    path.SetAxis(1, 4)
    path.SetAxis(2, 5)

    # Use single motion profile for entire path
    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 300
    profile.acc = 2000
    profile.dec = 2000
    path.SetProfile(0, profile)

    # Define linear and circular segments
    path.numPoints = 21

    # Segment 1: Linear to (90, 0, 0)
    path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 0, 90)
    path.SetTarget(1, 0, 0)
    path.SetTarget(2, 0, 0)

    # Segment 2: Circular to (100, 10, 0) with center (97.071, 2.929, 0)
    path.SetType(1, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 1, 100)
    path.SetTarget(1, 1, 10)
    path.SetTarget(2, 1, 0)
    path.SetCircleIntermediateTarget(0, 1, 97.071)
    path.SetCircleIntermediateTarget(1, 1, 2.929)
    path.SetCircleIntermediateTarget(2, 1, 0)

    # Segment 3: Linear to (100, 90, 0)
    path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 2, 100)
    path.SetTarget(1, 2, 90)
    path.SetTarget(2, 2, 0)

    # Segment 4: Circular to (90, 100, 0) with center (97.071, 97.071, 0)
    path.SetType(3, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 3, 90)
    path.SetTarget(1, 3, 100)
    path.SetTarget(2, 3, 0)
    path.SetCircleIntermediateTarget(0, 3, 97.071)
    path.SetCircleIntermediateTarget(1, 3, 97.071)
    path.SetCircleIntermediateTarget(2, 3, 0)

    # Segment 5: Linear to (10, 100, 0)
    path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 4, 10)
    path.SetTarget(1, 4, 100)
    path.SetTarget(2, 4, 0)

    # Segment 6: Circular to (0, 90, 0) with center (2.929, 97.071, 0)
    path.SetType(5, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 5, 0)
    path.SetTarget(1, 5, 90)
    path.SetTarget(2, 5, 0)
    path.SetCircleIntermediateTarget(0, 5, 2.929)
    path.SetCircleIntermediateTarget(1, 5, 97.071)
    path.SetCircleIntermediateTarget(2, 5, 0)

    # Segment 7: Linear to (0, 0, 0)
    path.SetType(6, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 6, 0)
    path.SetTarget(1, 6, 0)
    path.SetTarget(2, 6, 0)

    # Segment 8: Linear to (90, 0, 0)
    path.SetType(7, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 7, 90)
    path.SetTarget(1, 7, 0)
    path.SetTarget(2, 7, 0)

    # Segment 9: Circular to (100, 0, -10) with center (97.071, 0, -2.929)
    path.SetType(8, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 8, 100)
    path.SetTarget(1, 8, 0)
    path.SetTarget(2, 8, -10)
    path.SetCircleIntermediateTarget(0, 8, 97.071)
    path.SetCircleIntermediateTarget(1, 8, 0)
    path.SetCircleIntermediateTarget(2, 8, -2.929)

    # Segment 10: Linear to (100, 0, -90)
    path.SetType(9, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 9, 100)
    path.SetTarget(1, 9, 0)
    path.SetTarget(2, 9, -90)

    # Segment 11: Circular to (90, 0, -100) with center (97.071, 0, -97.071)
    path.SetType(10, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 10, 90)
    path.SetTarget(1, 10, 0)
    path.SetTarget(2, 10, -100)
    path.SetCircleIntermediateTarget(0, 10, 97.071)
    path.SetCircleIntermediateTarget(1, 10, 0)
    path.SetCircleIntermediateTarget(2, 10, -97.071)

    # Segment 12: Linear to (10, 0, -100)
    path.SetType(11, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 11, 10)
    path.SetTarget(1, 11, 0)
    path.SetTarget(2, 11, -100)

    # Segment 13: Circular to (0, 0, -90) with center (2.929, 0, -97.071)
    path.SetType(12, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 12, 0)
    path.SetTarget(1, 12, 0)
    path.SetTarget(2, 12, -90)
    path.SetCircleIntermediateTarget(0, 12, 2.929)
    path.SetCircleIntermediateTarget(1, 12, 0)
    path.SetCircleIntermediateTarget(2, 12, -97.071)

    # Segment 14: Linear to (0, 0, 0)
    path.SetType(13, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 13, 0)
    path.SetTarget(1, 13, 0)
    path.SetTarget(2, 13, 0)

    # Segment 15: Linear to (0, 90, 0)
    path.SetType(14, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 14, 0)
    path.SetTarget(1, 14, 90)
    path.SetTarget(2, 14, 0)

    # Segment 16: Circular to (0, 100, -10) with center (0, 97.071, -2.929)
    path.SetType(15, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 15, 0)
    path.SetTarget(1, 15, 100)
    path.SetTarget(2, 15, -10)
    path.SetCircleIntermediateTarget(0, 15, 0)
    path.SetCircleIntermediateTarget(1, 15, 97.071)
    path.SetCircleIntermediateTarget(2, 15, -2.929)

    # Segment 17: Linear to (0, 100, -90)
    path.SetType(16, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 16, 0)
    path.SetTarget(1, 16, 100)
    path.SetTarget(2, 16, -90)

    # Segment 18: Circular to (0, 90, -100) with center (0, 97.071, -97.071)
    path.SetType(17, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 17, 0)
    path.SetTarget(1, 17, 90)
    path.SetTarget(2, 17, -100)
    path.SetCircleIntermediateTarget(0, 17, 0)
    path.SetCircleIntermediateTarget(1, 17, 97.071)
    path.SetCircleIntermediateTarget(2, 17, -97.071)

    # Segment 19: Linear to (0, 10, -100)
    path.SetType(18, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 18, 0)
    path.SetTarget(1, 18, 10)
    path.SetTarget(2, 18, -100)

    # Segment 20: Circular to (0, 0, -90) with center (0, 2.929, -97.071)
    path.SetType(19, AdvMotion_PathIntplSegmentType.Circular)
    path.SetTarget(0, 19, 0)
    path.SetTarget(1, 19, 0)
    path.SetTarget(2, 19, -90)
    path.SetCircleIntermediateTarget(0, 19, 0)
    path.SetCircleIntermediateTarget(1, 19, 2.929)
    path.SetCircleIntermediateTarget(2, 19, -97.071)

    # Segment 21: Linear to (0, 0, 0)
    path.SetType(20, AdvMotion_PathIntplSegmentType.Linear)
    path.SetTarget(0, 20, 0)
    path.SetTarget(1, 20, 0)
    path.SetTarget(2, 20, 0)

    # Start path interpolation
    ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
    if ret != 0:
        print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Wait for the spline motion to complete
    axes = AxisSelection()
    axes.axisCount = 3
    axes.SetAxis(0, 2)
    axes.SetAxis(1, 4)
    axes.SetAxis(2, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Reverse the sequence from step 21 back to step 1
    # This part of the code would involve reversing the path commands and executing them again.
    # For brevity, this is left as an exercise to implement based on the specific motion library's API.


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

