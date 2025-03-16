
# Define Axes and IOs
Axes = [1, 2, 3, 4, 5, 6]
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
    path_0.fileName = f"111_gpt-4o-M1_Log.txt"

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


    # Axes = [1, 2, 3, 4, 5, 6]
    # IOInputs = []
    # IOOutputs = []

    # Create and execute a cyclic buffer memory space for Axis 1
    cyclic_buffer_axis_1 = CyclicBuffer(Wmx3Lib)
    ret = cyclic_buffer_axis_1.OpenCyclicBuffer(1, 1024)
    if ret != 0:
        print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    ret = cyclic_buffer_axis_1.Execute(1)
    if ret != 0:
        print('Execute error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    # Move to position 60 within 100 cycles
    command = CyclicBufferSingleAxisCommand()
    command.type = CyclicBufferCommandType.AbsolutePos
    command.intervalCycles = 100
    command.command = 60
    ret = cyclic_buffer_axis_1.AddCommand(1, command)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    # Move a relative distance of 140 within 100 cycles
    command.type = CyclicBufferCommandType.RelativePos
    command.intervalCycles = 100
    command.command = 140
    ret = cyclic_buffer_axis_1.AddCommand(1, command)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    # Move to position -100 within 200 cycles
    command.type = CyclicBufferCommandType.AbsolutePos
    command.intervalCycles = 200
    command.command = -100
    ret = cyclic_buffer_axis_1.AddCommand(1, command)
    if ret != 0:
        print('AddCommand error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    # Wait for cyclic buffer execution to end
    while True:
        ret, status = cyclic_buffer_axis_1.GetStatus(1)
        if status.remainCount <= 0:
            break
        sleep(0.1)

    # Close the cyclic buffer memory space
    ret = cyclic_buffer_axis_1.CloseCyclicBuffer(1)
    if ret != 0:
        print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + cyclic_buffer_axis_1.ErrorToString(ret))
        return

    # Execute a PVT command for Axis 2
    pvt = Motion_PVTCommand()
    pvt.axis = 2
    pvt.pointCount = 6

    points = [
        (0, 0, 0),
        (50, 1000, 100),
        (100, 2000, 200),
        (200, 3000, 300),
        (300, 1000, 400),
        (200, 0, 500)
    ]

    for i, (pos, vel, time) in enumerate(points):
        pvt_point = Motion_PVTPoint()
        pvt_point.pos = pos
        pvt_point.velocity = vel
        pvt_point.timeMilliseconds = time
        pvt.SetPoints(i, pvt_point)

    ret = Wmx3Lib_cm.motion.StartPVT(pvt)
    if ret != 0:
        print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute a PT command for Axis 3
    pt = Motion_PTCommand()
    pt.axis = 3
    pt.pointCount = 5

    points = [
        (50, 0),
        (-50, 100),
        (50, 200),
        (-50, 300),
        (0, 400)
    ]

    for i, (pos, time) in enumerate(points):
        pt_point = Motion_PTPoint()
        pt_point.pos = pos
        pt_point.timeMilliseconds = time
        pt.SetPoints(i, pt_point)

    ret = Wmx3Lib_cm.motion.StartPT(pt)
    if ret != 0:
        print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(3)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute a VT command for Axis 4
    vt = Motion_VTCommand()
    vt.axis = 4
    vt.pointCount = 5

    points = [
        (60, 0),
        (-60, 100),
        (60, 200),
        (-60, 300),
        (0, 400)
    ]

    for i, (vel, time) in enumerate(points):
        vt_point = Motion_VTPoint()
        vt_point.velocity = vel
        vt_point.timeMilliseconds = time
        vt.SetPoints(i, vt_point)

    ret = Wmx3Lib_cm.motion.StartVT(vt)
    if ret != 0:
        print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(4)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Move Axis 5 by a distance of 60 with a velocity of 1400
    move_command = Motion_MoveCommand()
    move_command.axis = 5
    move_command.distance = 60
    move_command.velocity = 1400

    ret = Wmx3Lib_cm.motion.StartMove(move_command)
    if ret != 0:
        print('StartMove error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Execute a cubic spline for Axis 5 and Axis 6
    spline = Motion_CubicSplineCommand()
    spline.axisCount = 2
    spline.SetAxis(0, 5)
    spline.SetAxis(1, 6)
    spline.totalTimeSeconds = 1.5

    points = [
        (0, 0),
        (25, 50),
        (50, 0),
        (75, -50),
        (100, 0)
    ]

    for i, (pos5, pos6) in enumerate(points):
        spline.SetPoint(i, 0, pos5)
        spline.SetPoint(i, 1, pos6)

    ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
    if ret != 0:
        print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 5)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


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

