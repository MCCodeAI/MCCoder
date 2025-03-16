
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M1"
    path_0.fileName = f"64_o3-mini-M1_Log.txt"

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

    # This script executes a 3D path interpolation for axes 4, 5, and 2 (sorted as [2, 4, 5])
    # with a constant velocity of 300. The path consists of a forward sequence of 21 segments
    # (a mix of linear and circular interpolations) followed by the reverse of that sequence.
    # After starting the motion, the script waits for all axes to stop moving before ending.

    # Note: This script assumes that the AdvancedMotion library and its related API objects
    # (e.g., AdvMotion_PathIntpl3DCommand, Profile, AxisSelection, etc.) are defined elsewhere.
    # No motion libraries are imported here as per instructions.

    def execute_3d_path_interpolation():
        # Create an instance of AdvancedMotion and a new 3D path interpolation command object.
        Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
        path = AdvMotion_PathIntpl3DCommand()

        # Set the axes in sorted order: 2, 4, and 5.
        path.SetAxis(0, 2)  # X coordinate mapped to Axis 2
        path.SetAxis(1, 4)  # Y coordinate mapped to Axis 4
        path.SetAxis(2, 5)  # Z coordinate mapped to Axis 5

        # Use a constant profile for the entire path.
        path.enableConstProfile = 1
        profile = Profile()
        profile.type = ProfileType.Trapezoidal
        profile.velocity = 300
        profile.acc = 2000
        profile.dec = 2000
        path.SetProfile(0, profile)  # Applies to all segments when using constant profile.

        # Define the forward segments (21 segments)
        # Each segment is defined as a dictionary with 'type', 'target', and, if circular, a 'center'
        forward_segments = [
            { "type": "Linear",   "target": (90, 0, 0) },
            { "type": "Circular", "target": (100, 10, 0),    "center": (97.071, 2.929, 0) },
            { "type": "Linear",   "target": (100, 90, 0) },
            { "type": "Circular", "target": (90, 100, 0),    "center": (97.071, 97.071, 0) },
            { "type": "Linear",   "target": (10, 100, 0) },
            { "type": "Circular", "target": (0, 90, 0),      "center": (2.929, 97.071, 0) },
            { "type": "Linear",   "target": (0, 0, 0) },
            { "type": "Linear",   "target": (90, 0, 0) },
            { "type": "Circular", "target": (100, 0, -10),   "center": (97.071, 0, -2.929) },
            { "type": "Linear",   "target": (100, 0, -90) },
            { "type": "Circular", "target": (90, 0, -100),   "center": (97.071, 0, -97.071) },
            { "type": "Linear",   "target": (10, 0, -100) },
            { "type": "Circular", "target": (0, 0, -90),     "center": (2.929, 0, -97.071) },
            { "type": "Linear",   "target": (0, 0, 0) },
            { "type": "Linear",   "target": (0, 90, 0) },
            { "type": "Circular", "target": (0, 100, -10),   "center": (0, 97.071, -2.929) },
            { "type": "Linear",   "target": (0, 100, -90) },
            { "type": "Circular", "target": (0, 90, -100),   "center": (0, 97.071, -97.071) },
            { "type": "Linear",   "target": (0, 10, -100) },
            { "type": "Circular", "target": (0, 0, -90),     "center": (0, 2.929, -97.071) },
            { "type": "Linear",   "target": (0, 0, 0) }
        ]

        # Create the complete sequence including the reverse.
        # The reverse sequence is obtained by reversing the forward segments.
        # In this case, we duplicate the entire forward sequence in reverse order so that the
        # path goes from step 21 back to step 1.
        reverse_segments = forward_segments[::-1]
        full_segments = forward_segments + reverse_segments
        num_segments = len(full_segments)
        path.numPoints = num_segments

        # Helper function to set a segment in the path command.
        def set_segment(i, segment):
            # Determine segment type.
            if segment["type"] == "Linear":
                path.SetType(i, AdvMotion_PathIntplSegmentType.Linear)
            elif segment["type"] == "Circular":
                path.SetType(i, AdvMotion_PathIntplSegmentType.Circular)
            else:
                raise ValueError("Unknown segment type at index {}.".format(i))

            # Set target positions for X, Y, and Z.
            # Here, target values are extracted from the tuple.
            path.SetTarget(0, i, segment["target"][0])
            path.SetTarget(1, i, segment["target"][1])
            path.SetTarget(2, i, segment["target"][2])

            # If the segment is circular, set the circle intermediate (center) targets.
            if segment["type"] == "Circular":
                path.SetCircleIntermediateTarget(0, i, segment["center"][0])
                path.SetCircleIntermediateTarget(1, i, segment["center"][1])
                path.SetCircleIntermediateTarget(2, i, segment["center"][2])

        # Loop over the complete (forward + reverse) segments and set each one.
        for idx, seg in enumerate(full_segments):
            set_segment(idx, seg)

        # Start the 3D path interpolation motion.
        ret = Wmx3Lib_adv.advMotion.StartPathIntpl3DPos(path)
        if ret != 0:
            print('StartPathIntpl3DPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
            return

        # Wait until motion is complete.
        # Waiting is done after the entire continuous path (all segments) completes.
        axes = AxisSelection()
        axes.axisCount = 3
        axes.SetAxis(0, 2)
        axes.SetAxis(1, 4)
        axes.SetAxis(2, 5)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
        if ret != 0:
            print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
            return

    # Execute the path interpolation command.
    execute_3d_path_interpolation()


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

