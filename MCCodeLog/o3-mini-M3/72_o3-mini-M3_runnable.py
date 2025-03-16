
# Define Axes and IOs
Axes = []
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
    path_0.fileName = f"72_o3-mini-M3_Log.txt"

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


    # -*- coding: utf-8 -*-
    import math
    from time import sleep

    # Assume that the following global objects and classes exist and have been initialized elsewhere:
    #   Wmx3Lib, Wmx3Lib_adv, Wmx3Lib_cm,
    #   AdvancedMotion, AdvMotion_PathIntplLookaheadCommand, AdvMotion_PathIntplLookaheadCommandPoint,
    #   AdvMotion_PathIntplLookaheadSegmentType, AdvMotion_PathIntplLookaheadConfiguration,
    #   AxisSelection

    # --------------------------------------------------------------------
    # COMMAND 1:
    # Execute path interpolation with look-ahead on Axis 2 and Axis 7 at 2200 velocity.
    # The path consists of:
    #   1. A line segment to (50, 0)
    #   2. A circular arc from (50,0) that goes through (50,100) and returns to (50,0)
    #      (approximated by a series of linear segments over a full circle, where the circle has
    #       center (50,50) and radius 50)
    #   3. A line segment to (100, 0)
    #
    # Wait for the axes to be idle after the motion completes.
    # --------------------------------------------------------------------

    # Free any previous look-ahead buffer (channel 0 used arbitrarily)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

    # Create a look-ahead buffer for channel 0 with the commanded composite (linear) velocity of 2200.
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
    if ret != 0:
        print("CreatePathIntplLookaheadBuffer error code is", ret)
        # Handle error as appropriate

    # Configure look-ahead settings for axes 2 and 7.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 2)
    conf.SetAxis(1, 7)
    conf.compositeVel = 2200
    conf.compositeAcc = 10000  # Assumed acceleration value
    conf.sampleDistance = 10   # Chosen sample distance (units as required)
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print("SetPathIntplLookaheadConfiguration error code is", ret)
        # Handle error as appropriate

    # Build the look-ahead command for Command 1.
    # This command is composed of:
    #   - Point 0: Line to (50, 0)
    #   - Points 1 to 10: Approximated circular arc (full circle) starting from (50,0), going through (50,100)
    #                    and returning to (50,0)
    #   - Point 11: Line to (100, 0)
    num_points = 12
    path = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = num_points

    # Point 0: Line to (50, 0)
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 2)
    pt.linear.SetAxis(1, 7)
    pt.linear.SetTarget(0, 50)
    pt.linear.SetTarget(1, 0)
    path.SetPoint(0, pt)

    # Points 1-10: Approximated circular arc
    center_x = 50
    center_y = 50
    radius = 50
    start_angle = -math.pi / 2
    num_circle_pts = 10
    for i in range(num_circle_pts):
        angle = start_angle + (2 * math.pi * (i + 1) / num_circle_pts)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pt = AdvMotion_PathIntplLookaheadCommandPoint()
        pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
        pt.linear.axisCount = 2
        pt.linear.SetAxis(0, 2)
        pt.linear.SetAxis(1, 7)
        pt.linear.SetTarget(0, x)
        pt.linear.SetTarget(1, y)
        path.SetPoint(i + 1, pt)

    # Point 11: Line to (100, 0)
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 2)
    pt.linear.SetAxis(1, 7)
    pt.linear.SetTarget(0, 100)
    pt.linear.SetTarget(1, 0)
    path.SetPoint(num_points - 1, pt)

    # Add the command to the look-ahead buffer.
    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path)
    if ret != 0:
        print("AddPathIntplLookaheadCommand error code is", ret)
        # Handle error as appropriate

    # Start executing the look-ahead path interpolation command.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print("StartPathIntplLookahead error code is", ret)
        # Handle error as appropriate

    # Wait until both Axis 2 and Axis 7 have completed their motion.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 2)
    axes.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is", ret)
        # Handle error as appropriate

    # Free the look-ahead buffer after motion completion.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print("FreePathIntplLookaheadBuffer error code is", ret)
        # Handle error as appropriate

    # --------------------------------------------------------------------
    # End of COMMAND 1
    # --------------------------------------------------------------------

    # Pause for 0.5 seconds.
    sleep(0.5)

    # --------------------------------------------------------------------
    # COMMAND 2:
    # Execute path interpolation with look-ahead on Axis 2 and Axis 7 at 2200 velocity.
    # The path consists of:
    #   1. A line segment to (150, 100)
    #   2. A line segment to (200, 0)
    #
    # Wait for the axes to be idle after the motion completes.
    # --------------------------------------------------------------------

    # Free any previous look-ahead buffer on channel 0.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)

    # Create a look-ahead buffer for channel 0 with velocity of 2200.
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(0, 2200)
    if ret != 0:
        print("CreatePathIntplLookaheadBuffer error code is", ret)
        # Handle error as appropriate

    # Reuse the same configuration for axes 2 and 7.
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 2)
    conf.SetAxis(1, 7)
    conf.compositeVel = 2200
    conf.compositeAcc = 10000
    conf.sampleDistance = 10
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(0, conf)
    if ret != 0:
        print("SetPathIntplLookaheadConfiguration error code is", ret)
        # Handle error as appropriate

    # Build the look-ahead command for Command 2 with 2 points.
    path2 = AdvMotion_PathIntplLookaheadCommand()
    path2.numPoints = 2

    # Point 0: Line to (150, 100)
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 2)
    pt.linear.SetAxis(1, 7)
    pt.linear.SetTarget(0, 150)
    pt.linear.SetTarget(1, 100)
    path2.SetPoint(0, pt)

    # Point 1: Line to (200, 0)
    pt = AdvMotion_PathIntplLookaheadCommandPoint()
    pt.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
    pt.linear.axisCount = 2
    pt.linear.SetAxis(0, 2)
    pt.linear.SetAxis(1, 7)
    pt.linear.SetTarget(0, 200)
    pt.linear.SetTarget(1, 0)
    path2.SetPoint(1, pt)

    # Add the second command to the look-ahead buffer.
    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(0, path2)
    if ret != 0:
        print("AddPathIntplLookaheadCommand error code is", ret)
        # Handle error as appropriate

    # Start executing the Command 2 look-ahead motion.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(0)
    if ret != 0:
        print("StartPathIntplLookahead error code is", ret)
        # Handle error as appropriate

    # Wait until both Axis 2 and Axis 7 have completed their motion.
    axes.SetAxis(0, 2)
    axes.SetAxis(1, 7)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error code is", ret)
        # Handle error as appropriate

    # Free the look-ahead buffer after motion completion.
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(0)
    if ret != 0:
        print("FreePathIntplLookaheadBuffer error code is", ret)
        # Handle error as appropriate


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

