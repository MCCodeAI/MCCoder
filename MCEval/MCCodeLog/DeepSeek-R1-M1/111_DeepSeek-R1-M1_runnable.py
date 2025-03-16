
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\DeepSeek-R1-M1"
    path_0.fileName = f"111_DeepSeek-R1-M1_Log.txt"

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

    # Task 1: Cyclic Buffer for Axis 1
    Wmx3Lib_cyc = CyclicBuffer(Wmx3Lib)

    # Create cyclic buffer with 1024 cycles
    ret = Wmx3Lib_cyc.OpenCyclicBuffer(1, 1024)
    if ret != 0:
        print('OpenCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Start execution
    ret = Wmx3Lib_cyc.Execute(1)
    if ret != 0:
        print('Execute error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return

    # Add commands
    cyclicBufferSingleAxisCommand = CyclicBufferSingleAxisCommand()

    # Move to position 60 in 100 cycles
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicBufferSingleAxisCommand.intervalCycles = 100
    cyclicBufferSingleAxisCommand.command = 60
    ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

    # Move relative 140 in 100 cycles
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.RelativePos
    cyclicBufferSingleAxisCommand.intervalCycles = 100
    cyclicBufferSingleAxisCommand.command = 140
    ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

    # Move to position -100 in 200 cycles
    cyclicBufferSingleAxisCommand.type = CyclicBufferCommandType.AbsolutePos
    cyclicBufferSingleAxisCommand.intervalCycles = 200
    cyclicBufferSingleAxisCommand.command = -100
    ret = Wmx3Lib_cyc.AddCommand(1, cyclicBufferSingleAxisCommand)

    # Wait for completion
    while True:
        ret, cyc_Status = Wmx3Lib_cyc.GetStatus(1)
        if cyc_Status.remainCount <= 0:
            break
        sleep(0.1)

    # Close cyclic buffer
    ret = Wmx3Lib_cyc.CloseCyclicBuffer(1)
    if ret != 0:
        print('CloseCyclicBuffer error code is ' + str(ret) + ': ' + Wmx3Lib_cyc.ErrorToString(ret))
        return


    # Task 2: PVT Command for Axis 2
    pvt = Motion_PVTCommand()
    pvtparameter = Motion_PVTPoint()

    pvt.axis = 2
    pvt.pointCount = 5

    # Define points
    pvtparameter.pos = 0
    pvtparameter.velocity = 0
    pvtparameter.timeMilliseconds = 0
    pvt.SetPoints(0, pvtparameter)

    pvtparameter.pos = 50
    pvtparameter.velocity = 1000
    pvtparameter.timeMilliseconds = 100
    pvt.SetPoints(1, pvtparameter)

    pvtparameter.pos = 100
    pvtparameter.velocity = 2000
    pvtparameter.timeMilliseconds = 200
    pvt.SetPoints(2, pvtparameter)

    pvtparameter.pos = 200
    pvtparameter.velocity = 3000
    pvtparameter.timeMilliseconds = 300
    pvt.SetPoints(3, pvtparameter)

    pvtparameter.pos = 300
    pvtparameter.velocity = 1000
    pvtparameter.timeMilliseconds = 400
    pvt.SetPoints(4, pvtparameter)

    ret = Wmx3Lib_cm.motion.StartPVT(pvt)
    if ret != 0:
        print('StartPVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


    # Task 3: PT Command for Axis 3
    pt = Motion_PTCommand()
    ptparameter = Motion_PTPoint()

    pt.axis = 3
    pt.pointCount = 5

    # Define points
    ptparameter.pos = 50
    ptparameter.timeMilliseconds = 0
    pt.SetPoints(0, ptparameter)

    ptparameter.pos = -50
    ptparameter.timeMilliseconds = 100
    pt.SetPoints(1, ptparameter)

    ptparameter.pos = 50
    ptparameter.timeMilliseconds = 200
    pt.SetPoints(2, ptparameter)

    ptparameter.pos = -50
    ptparameter.timeMilliseconds = 300
    pt.SetPoints(3, ptparameter)

    ptparameter.pos = 0
    ptparameter.timeMilliseconds = 400
    pt.SetPoints(4, ptparameter)

    ret = Wmx3Lib_cm.motion.StartPT(pt)
    if ret != 0:
        print('StartPT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(3)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


    # Task 4: VT Command for Axis 4
    vt = Motion_VTCommand()
    vtparameter = Motion_VTPoint()

    vt.axis = 4
    vt.pointCount = 5

    # Define points
    vtparameter.velocity = 60
    vtparameter.timeMilliseconds = 0
    vt.SetPoints(0, vtparameter)

    vtparameter.velocity = -60
    vtparameter.timeMilliseconds = 100
    vt.SetPoints(1, vtparameter)

    vtparameter.velocity = 60
    vtparameter.timeMilliseconds = 200
    vt.SetPoints(2, vtparameter)

    vtparameter.velocity = -60
    vtparameter.timeMilliseconds = 300
    vt.SetPoints(3, vtparameter)

    vtparameter.velocity = 0
    vtparameter.timeMilliseconds = 400
    vt.SetPoints(4, vtparameter)

    ret = Wmx3Lib_cm.motion.StartVT(vt)
    if ret != 0:
        print('StartVT error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(4)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


    # Task 5: Move Axis 5 by distance
    lin = Motion_LinearIntplCommand()
    lin.axisCount = 1
    lin.SetAxis(0, 5)
    lin.profile.type = ProfileType.Trapezoidal
    lin.profile.velocity = 1400
    lin.profile.acc = 10000
    lin.profile.dec = 10000
    lin.SetTarget(0, 60)

    ret = Wmx3Lib_cm.motion.StartLinearIntplDist(lin)
    if ret != 0:
        print('StartLinearIntplDist error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.motion.Wait(5)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return


    # Task 6: Cubic Spline for Axes 5 and 6
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)

    # Clear and create buffer
    Wmx3Lib_buf.Clear(0)
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 5)
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    spline = Motion_CubicSplineCommand()
    spline.axisCount = 2
    spline.SetAxis(0, 5)
    spline.SetAxis(1, 6)
    spline.pointCount = 5

    # Define points
    spline.SetPoint(0, 0, 0)
    spline.SetPoint(1, 25, 50)
    spline.SetPoint(2, 50, 0)
    spline.SetPoint(3, 75, -50)
    spline.SetPoint(4, 100, 0)

    ret = Wmx3Lib_cm.motion.StartCubicSpline(spline)
    if ret != 0:
        print('StartCubicSpline error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # End recording and execute
    Wmx3Lib_buf.EndRecordBufferChannel()
    Wmx3Lib_buf.Execute(0)

    # Wait for completion
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 5)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Cleanup
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)


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

