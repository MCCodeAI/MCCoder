
# Define Axes and IOs
Axes = [3, 5]
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
    path_0.fileName = f"113_DeepSeek-R1-M3_Log.txt"

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


    # Axes = [3, 5]
    # IOInputs = []
    # IOOutputs = []

    import math

    # Task 1: Path interpolation with look-ahead channel 10
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Free and create buffer for look-ahead channel 10
    ret = Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)
    sleep(0.1)
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplLookaheadBuffer(10, 1000)
    if ret != 0:
        print(f'CreatePathIntplLookaheadBuffer error: {ret}')
        exit()

    # Configure look-ahead parameters
    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 3)
    conf.SetAxis(1, 5)
    conf.compositeVel = 1500
    conf.compositeAcc = 10000
    conf.sampleDistance = 10
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.advMotion.SetPathIntplLookaheadConfiguration(10, conf)
    if ret != 0:
        print(f'SetPathIntplLookaheadConfiguration error: {ret}')
        exit()

    # Add path points with smooth transitions
    path = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = 4
    points = [(50, 0), (50, 50), (0, 50), (0, 0)]

    for i in range(4):
        point = AdvMotion_PathIntplLookaheadCommandPoint()
        point.type = AdvMotion_PathIntplLookaheadSegmentType.Linear
        point.linear.axisCount = 2
        point.linear.SetAxis(0, 3)
        point.linear.SetAxis(1, 5)
        point.linear.SetTarget(0, points[i][0])
        point.linear.SetTarget(1, points[i][1])
        if i < 3:  # Apply smooth radius to first three segments
            point.linear.smoothRadius = 12
        path.SetPoint(i, point)

    ret = Wmx3Lib_adv.advMotion.AddPathIntplLookaheadCommand(10, path)
    if ret != 0:
        print(f'AddPathIntplLookaheadCommand error: {ret}')
        exit()

    # Execute motion
    ret = Wmx3Lib_adv.advMotion.StartPathIntplLookahead(10)
    if ret != 0:
        print(f'StartPathIntplLookahead error: {ret}')
        exit()

    # Wait for completion
    axis_sel = AxisSelection()
    axis_sel.axisCount = 2
    axis_sel.SetAxis(0, 3)
    axis_sel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
    if ret != 0:
        print(f'Wait_AxisSel error: {ret}')
        exit()

    # Free buffer
    Wmx3Lib_adv.advMotion.FreePathIntplLookaheadBuffer(10)


    # Task 2: Cubic spline motion
    ret = Wmx3Lib_adv.advMotion.CreateSplineBuffer(0, 100)
    if ret != 0:
        print(f'CreateSplineBuffer error: {ret}')
        exit()

    spline_command = AdvMotion_TotalTimeSplineCommand()
    spline_command.dimensionCount = 2
    spline_command.SetAxis(0, 3)
    spline_command.SetAxis(1, 5)
    spline_command.totalTimeMilliseconds = 1000

    # Define spline points
    spline_points = [
        (0, 0), (10, 10), (-20, -20), (30, 30),
        (-40, -40), (50, 50), (-60, -60), (70, 70), (-80, -80)
    ]

    spline_objects = []
    for pt in spline_points:
        sp = AdvMotion_SplinePoint()
        sp.SetPos(0, pt[0])
        sp.SetPos(1, pt[1])
        spline_objects.append(sp)

    # Execute spline motion
    ret = Wmx3Lib_adv.advMotion.StartCSplinePos_TotalTime(0, spline_command, 9, spline_objects)
    if ret != 0:
        print(f'StartCSplinePos_TotalTime error: {ret}')
        exit()

    # Wait for completion
    axis_sel = AxisSelection()
    axis_sel.axisCount = 2
    axis_sel.SetAxis(0, 3)
    axis_sel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
    if ret != 0:
        print(f'Wait_AxisSel error: {ret}')
        exit()

    # Free spline buffer
    Wmx3Lib_adv.advMotion.FreeSplineBuffer(0)


    # Task 3: Synchronous control
    # Establish master-slave relationship
    ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(3, 5)
    if ret != 0:
        print(f'SetSyncMasterSlave error: {ret}')
        exit()

    # First movement to 120
    pos_command = Motion_PosCommand()
    pos_command.profile.type = ProfileType.Trapezoidal
    pos_command.axis = 3
    pos_command.target = 120
    pos_command.profile.velocity = 1000
    pos_command.profile.acc = 10000
    pos_command.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(pos_command)
    if ret != 0:
        print(f'First StartPos error: {ret}')
        exit()
    Wmx3Lib_cm.motion.Wait(3)

    # Second movement to 240
    pos_command.target = 240
    ret = Wmx3Lib_cm.motion.StartPos(pos_command)
    if ret != 0:
        print(f'Second StartPos error: {ret}')
        exit()
    Wmx3Lib_cm.motion.Wait(3)

    # Release synchronization
    Wmx3Lib_cm.sync.ResolveSync(5)


    # Task 4: PVT interpolation
    pvti = Motion_PVTIntplCommand()
    pvti.axisCount = 2
    pvti.SetAxis(0, 3)
    pvti.SetAxis(1, 5)
    pvti.SetPointCount(0, 20)
    pvti.SetPointCount(1, 20)

    # Generate circular points
    center = (-50, 0)
    radius = 50
    for i in range(20):
        theta = 2 * math.pi * i / 20
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)
    
        # Axis 3 parameters
        pvt_axis3 = Motion_PVTPoint()
        pvt_axis3.pos = x
        pvt_axis3.velocity = 100
        pvt_axis3.timeMilliseconds = i * 100
        pvti.SetPoints(0, i, pvt_axis3)
    
        # Axis 5 parameters
        pvt_axis5 = Motion_PVTPoint()
        pvt_axis5.pos = y
        pvt_axis5.velocity = 100
        pvt_axis5.timeMilliseconds = i * 100
        pvti.SetPoints(1, i, pvt_axis5)

    # Execute PVT command
    ret = Wmx3Lib_cm.motion.StartPVT_Intpl(pvti)
    if ret != 0:
        print(f'StartPVT_Intpl error: {ret}')
        exit()

    # Final wait for motion completion
    axis_sel = AxisSelection()
    axis_sel.axisCount = 2
    axis_sel.SetAxis(0, 3)
    axis_sel.SetAxis(1, 5)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axis_sel)
    if ret != 0:
        print(f'Final Wait_AxisSel error: {ret}')
        exit()


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

