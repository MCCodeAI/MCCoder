
# Define Axes and IOs
Axes = [1, 3, 8, 9]
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
    path_0.fileName = f"166_o3-mini-M1_Log.txt"

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


    # Axes = [1, 3, 8, 9]
    # IOInputs = []
    # IOOutputs = []

    # --- Execute a PVT command for Axis 1 with 6 points ---
    pvt = Motion_PVTCommand()
    pvt.axis = 1
    pvt.pointCount = 6

    # Define PVT points: (Position, Velocity, Time)
    pvtPoint = Motion_PVTPoint()

    # Point 0: (0, 0, 0)
    pvtPoint.pos = 0
    pvtPoint.velocity = 0
    pvtPoint.timeMilliseconds = 0
    pvt.SetPoints(0, pvtPoint)

    # Point 1: (50, 1000, 100)
    pvtPoint.pos = 50
    pvtPoint.velocity = 1000
    pvtPoint.timeMilliseconds = 100
    pvt.SetPoints(1, pvtPoint)

    # Point 2: (100, 2000, 200)
    pvtPoint.pos = 100
    pvtPoint.velocity = 2000
    pvtPoint.timeMilliseconds = 200
    pvt.SetPoints(2, pvtPoint)

    # Point 3: (200, 3000, 300)
    pvtPoint.pos = 200
    pvtPoint.velocity = 3000
    pvtPoint.timeMilliseconds = 300
    pvt.SetPoints(3, pvtPoint)

    # Point 4: (300, 1000, 400)
    pvtPoint.pos = 300
    pvtPoint.velocity = 1000
    pvtPoint.timeMilliseconds = 400
    pvt.SetPoints(4, pvtPoint)

    # Point 5: (200, 0, 500)
    pvtPoint.pos = 200
    pvtPoint.velocity = 0
    pvtPoint.timeMilliseconds = 500
    pvt.SetPoints(5, pvtPoint)

    ret = Wmx3Lib_cm.motion.StartPVT(pvt)
    if ret != 0:
        print("StartPVT error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait until Axis 1 stops moving
    ret = Wmx3Lib_cm.motion.Wait(1)
    if ret != 0:
        print("Wait error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)


    # --- Execute an absolute linear interpolation for Axes 1 and 3 to position (100, 100) with velocity 1000 ---
    # Set up a position command for Axis 1
    posCommand1 = Motion_PosCommand()
    posCommand1.profile.type = ProfileType.Trapezoidal
    posCommand1.axis = 1
    posCommand1.target = 100
    posCommand1.profile.velocity = 1000
    posCommand1.profile.acc = 10000
    posCommand1.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand1)
    if ret != 0:
        print("StartPos (Axis 1) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Set up a position command for Axis 3
    posCommand3 = Motion_PosCommand()
    posCommand3.profile.type = ProfileType.Trapezoidal
    posCommand3.axis = 3
    posCommand3.target = 100
    posCommand3.profile.velocity = 1000
    posCommand3.profile.acc = 10000
    posCommand3.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand3)
    if ret != 0:
        print("StartPos (Axis 3) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait until both Axes 1 and 3 stop moving
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Wait_AxisSel error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)


    # --- Execute a cubic spline motion command for Axes 8 and 9 ---
    # Total motion time: 1000ms
    # Spline points for both axes are given as pairs:
    #   Index:    Axis 8   Axis 9
    #   0:        0        0
    #   1:        10       10
    #   2:       -20      -20
    #   3:        30       30
    #   4:       -40      -40
    #   5:        50       50
    #   6:       -60      -60
    #   7:        70       70
    #   8:       -80      -80

    cubicSpline = Motion_CubicSplineCommand()
    cubicSpline.axisCount = 2
    cubicSpline.SetAxis(0, 8)
    cubicSpline.SetAxis(1, 9)
    cubicSpline.pointCount = 9

    # Set the total time for the cubic spline motion
    cubicSpline.totalTimeMilliseconds = 1000

    # List of points for the cubic spline motion
    spline_points = [
        (0, 0),
        (10, 10),
        (-20, -20),
        (30, 30),
        (-40, -40),
        (50, 50),
        (-60, -60),
        (70, 70),
        (-80, -80)
    ]

    # Assume the command object has a method SetPoint(axisIndex, pointIndex, position)
    for pt_index, (pos8, pos9) in enumerate(spline_points):
        cubicSpline.SetPoint(0, pt_index, pos8)
        cubicSpline.SetPoint(1, pt_index, pos9)

    ret = Wmx3Lib_cm.motion.StartCubicSpline(cubicSpline)
    if ret != 0:
        print("StartCubicSpline error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit(1)

    # Wait until both Axes 8 and 9 stop moving
    axisSelSpline = AxisSelection()
    axisSelSpline.axisCount = 2
    axisSelSpline.SetAxis(0, 8)
    axisSelSpline.SetAxis(1, 9)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSelSpline)
    if ret != 0:
        print("Wait_AxisSel (Spline) error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
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

