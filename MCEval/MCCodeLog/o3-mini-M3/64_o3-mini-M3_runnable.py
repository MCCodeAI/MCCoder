
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M3"
    path_0.fileName = f"64_o3-mini-M3_Log.txt"

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

    # The following code performs a 3D path interpolation on axes 4, 5, and 2
    # with a constant motion profile (velocity 300), following a sequence of
    # 21 segments and then the reverse of that sequence (total 42 segments).
    # For circular segments, the center of the arc is defined.
    #
    # NOTE:
    # - "StartPathIntpl3DPos" is assumed to send the entire path command.
    # - After starting the motion, the code waits for all the involved axes to
    #   reach a stopped state.
    # - This code uses a single constant motion profile for all segments.
    #
    # Assumptions: The motion library classes and functions (e.g. AdvancedMotion,
    # AdvMotion_PathIntpl3DCommand, Profile, ProfileType, AdvMotion_PathIntplSegmentType,
    # AxisSelection, etc.) are pre-defined elsewhere.
    #
    # Also, note that we wait for axes to stop only after the entire continuous motion
    # is commanded (i.e. not between individual segments).

    # Initialize the advanced motion command for 3D path interpolation
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    path = AdvMotion_PathIntpl3DCommand()

    # Configure the axes: we use Axis 4, 5, and 2 (in the order provided by the command).
    path.SetAxis(0, 4)
    path.SetAxis(1, 5)
    path.SetAxis(2, 2)

    # Set a constant motion profile for the entire path. Here, velocity is 300.
    path.enableConstProfile = 1
    profile = Profile()
    profile.type = ProfileType.Trapezoidal
    profile.velocity = 300
    profile.acc = 3000
    profile.dec = 3000
    path.SetProfile(0, profile)

    # Define the 21 forward segments in a list of dictionaries.
    # For each segment, 'type' can be 'Linear' or 'Circular'.
    # For circular segments, a 'center' tuple is provided.
    segments_forward = [
        {"type": "Linear",   "target": (90, 0, 0)},
        {"type": "Circular", "target": (100, 10, 0),   "center": (97.071, 2.929, 0)},
        {"type": "Linear",   "target": (100, 90, 0)},
        {"type": "Circular", "target": (90, 100, 0),   "center": (97.071, 97.071, 0)},
        {"type": "Linear",   "target": (10, 100, 0)},
        {"type": "Circular", "target": (0, 90, 0),     "center": (2.929, 97.071, 0)},
        {"type": "Linear",   "target": (0, 0, 0)},
        {"type": "Linear",   "target": (90, 0, 0)},
        {"type": "Circular", "target": (100, 0, -10),  "center": (97.071, 0, -2.929)},
        {"type": "Linear",   "target": (100, 0, -90)},
        {"type": "Circular", "target": (90, 0, -100),  "center": (97.071, 0, -97.071)},
        {"type": "Linear",   "target": (10, 0, -100)},
        {"type": "Circular", "target": (0, 0, -90),    "center": (2.929, 0, -97.071)},
        {"type": "Linear",   "target": (0, 0, 0)},
        {"type": "Linear",   "target": (0, 90, 0)},
        {"type": "Circular", "target": (0, 100, -10),  "center": (0, 97.071, -2.929)},
        {"type": "Linear",   "target": (0, 100, -90)},
        {"type": "Circular", "target": (0, 90, -100),  "center": (0, 97.071, -97.071)},
        {"type": "Linear",   "target": (0, 10, -100)},
        {"type": "Circular", "target": (0, 0, -90),    "center": (0, 2.929, -97.071)},
        {"type": "Linear",   "target": (0, 0, 0)}
    ]

    # To reverse the entire sequence, we simply reverse the forward segments.
    # The reverse sequence follows the same interpolation types with the same target and center parameters.
    segments_reverse = list(reversed(segments_forward))

    # Combine forward and reverse segments into one full path.
    all_segments = segments_forward + segments_reverse

    # Set the total number of segments (points) in the path.
    path.numPoints = len(all_segments)

    # Assign each segment's type, target and (if applicable) circle center.
    for i, seg in enumerate(all_segments):
        if seg["type"] == "Linear":
            path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
        elif seg["type"] == "Circular":
            path.SetType(i, AdvMotion_PathIntplSegmentType.Circular)
        # Set the target coordinates for each axis
        path.SetTarget(0, i, seg["target"][0])
        path.SetTarget(1, i, seg["target"][1])
        path.SetTarget(2, i, seg["target"][2])
        # For circular segments, also set the circle intermediate target (center)
        if seg["type"] == "Circular":
            path.SetCircleIntermediateTarget(0, i, seg["center"][0])
            path.SetCircleIntermediateTarget(1, i, seg["center"][1])
            path.SetCircleIntermediateTarget(2, i, seg["center"][2])

    # Start the 3D path interpolation motion.
    ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
    if ret != 0:
        print("StartPathIntpl3DPos error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
    else:
        # Wait for the motion to complete on all three axes.
        axes = AxisSelection()
        axes.axisCount = 3
        axes.SetAxis(0, 4)
        axes.SetAxis(1, 5)
        axes.SetAxis(2, 2)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
        if ret != 0:
            print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))


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

