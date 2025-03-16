
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M1"
    path_0.fileName = f"113_o3-mini-M1_Log.txt"

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
    from time import sleep

    # =============================================================================
    # Dummy Classes and Functions for Demonstration Purposes Only.
    # In a real application these would interface with the actual motion control library.
    # =============================================================================

    class AdvancedMotion:
        def __init__(self, lib):
            self.advMotion = self
        def CreatePathIntplLookaheadBuffer(self, channel, size):
            return 0
        def FreePathIntplLookaheadBuffer(self, channel):
            return 0
        def SetPathIntplLookaheadConfiguration(self, channel, conf):
            return 0
        def AddPathIntplLookaheadCommand(self, channel, cmd):
            return 0
        def StartPathIntplLookahead(self, channel):
            return 0
        def CreateSplineBuffer(self, channel, size):
            return 0
        def StartCSplinePos_TotalTime(self, channel, splineCommand, numPoints, splinePoints):
            return 0
        def StartPVTInterpolation(self, pvtCommand):
            return 0
        def ErrorToString(self, ret):
            return "Error code " + str(ret)

    class MotionLibrary:
        def __init__(self):
            self.motion = self
        def StartPos(self, posCmd):
            return 0
        def Wait_AxisSel(self, axes):
            return 0
        def Wait(self, axis):
            return

    class AxisSelection:
        def __init__(self):
            self.axisCount = 0
            self.axes = {}
        def SetAxis(self, index, value):
            self.axes[index] = value

    class Profile:
        pass

    class ProfileType:
        Trapezoidal = 0

    class Motion_PosCommand:
        def __init__(self):
            self.axis = None
            self.target = None
            self.profile = Profile()
            self.profile.type = None
            self.profile.velocity = None
            self.profile.acc = None
            self.profile.dec = None

    # ---- Look-Ahead Path Interpolation Classes ----
    class AdvMotion_PathIntplLookaheadConfiguration:
        def __init__(self):
            self.axisCount = 0
            self.compositeVel = None
            self.compositeAcc = None
            self.sampleDistance = None
            self.stopOnEmptyBuffer = None
            self.axes = {}
        def SetAxis(self, index, value):
            self.axes[index] = value

    class AdvMotion_PathIntplLookaheadCommand:
        def __init__(self):
            self.numPoints = 0
            self.points = {}
        def SetPoint(self, index, point):
            self.points[index] = point

    class AdvMotion_PathIntplLookaheadCommandPoint:
        def __init__(self):
            self.type = None
            self.linear = self.Linear()
        class Linear:
            def __init__(self):
                self.axisCount = 0
                self.targets = {}
                self.smoothRadius = 0
            def SetTarget(self, axis, value):
                self.targets[axis] = value

    # ---- Spline Command Classes ----
    class AdvMotion_TotalTimeSplineCommand:
        def __init__(self):
            self.dimensionCount = 0
            self.totalTimeMilliseconds = 0
            self.axes = {}
        def SetAxis(self, index, value):
            self.axes[index] = value

    class AdvMotion_SplinePoint:
        def __init__(self):
            self.positions = {}
        def SetPos(self, axis, value):
            self.positions[axis] = value

    # ---- PVT Interpolation Classes ----
    class AdvMotion_PVTPoint:
        def __init__(self):
            self.positions = {}
            self.velocities = {}
            self.time = 0
        def SetPos(self, axis, value):
            self.positions[axis] = value
        def SetVel(self, axis, value):
            self.velocities[axis] = value

    class AdvMotion_PVTInterpolationCommand:
        def __init__(self):
            self.axisCount = 0
            self.numPoints = 0
            self.points = []
        def AddPoint(self, point):
            self.points.append(point)

    # =============================================================================
    # End of Dummy Classes
    # =============================================================================

    # Instantiate library objects (placeholders)
    Wmx3Lib = None  # The actual motion controller library handle
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)
    Wmx3Lib_cm = MotionLibrary()

    # =============================================================================
    # 1. Path Interpolation with Look-Ahead Channel 10 for Axes 3 and 5
    #    • Velocity: 1500
    #    • Points: (50, 0), (50, 50), (0, 50), (0, 0)
    #    • Smooth radius: 12 applied on the first three segments
    # =============================================================================
    print("Starting Path Interpolation with Look-Ahead Channel 10 for Axes 3 and 5")

    ret = Wmx3Lib_adv.FreePathIntplLookaheadBuffer(10)
    if ret != 0:
        print("FreePathIntplLookaheadBuffer error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    sleep(0.1)

    ret = Wmx3Lib_adv.CreatePathIntplLookaheadBuffer(10, 1000)
    if ret != 0:
        print("CreatePathIntplLookaheadBuffer error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    conf = AdvMotion_PathIntplLookaheadConfiguration()
    conf.axisCount = 2
    conf.SetAxis(0, 3)
    conf.SetAxis(1, 5)
    conf.compositeVel = 1500
    conf.compositeAcc = 10000
    conf.sampleDistance = 100
    conf.stopOnEmptyBuffer = True

    ret = Wmx3Lib_adv.SetPathIntplLookaheadConfiguration(10, conf)
    if ret != 0:
        print("SetPathIntplLookaheadConfiguration error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    path = AdvMotion_PathIntplLookaheadCommand()
    path.numPoints = 4

    # Point 1: (50, 0) with smooth radius 12
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = "Linear"  # Using a string type indicator for simplicity
    point.linear.axisCount = 2
    point.linear.SetTarget(0, 50)  # For axis 3
    point.linear.SetTarget(1, 0)   # For axis 5
    point.linear.smoothRadius = 12
    path.SetPoint(0, point)

    # Point 2: (50, 50) with smooth radius 12
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = "Linear"
    point.linear.axisCount = 2
    point.linear.SetTarget(0, 50)
    point.linear.SetTarget(1, 50)
    point.linear.smoothRadius = 12
    path.SetPoint(1, point)

    # Point 3: (0, 50) with smooth radius 12
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = "Linear"
    point.linear.axisCount = 2
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 50)
    point.linear.smoothRadius = 12
    path.SetPoint(2, point)

    # Point 4: (0, 0) with no smooth radius specified
    point = AdvMotion_PathIntplLookaheadCommandPoint()
    point.type = "Linear"
    point.linear.axisCount = 2
    point.linear.SetTarget(0, 0)
    point.linear.SetTarget(1, 0)
    path.SetPoint(3, point)

    ret = Wmx3Lib_adv.AddPathIntplLookaheadCommand(10, path)
    if ret != 0:
        print("AddPathIntplLookaheadCommand error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    ret = Wmx3Lib_adv.StartPathIntplLookahead(10)
    if ret != 0:
        print("StartPathIntplLookahead error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 5)
    ret = Wmx3Lib_cm.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error:", ret)
        exit()

    ret = Wmx3Lib_adv.FreePathIntplLookaheadBuffer(10)
    if ret != 0:
        print("FreePathIntplLookaheadBuffer error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # =============================================================================
    # 2. Cubic Spline Motion Command for Axes 3 and 5 (Total Time = 1000ms)
    #    • Points: (0,0), (10,10), (-20,-20), (30,30), (-40,-40),
    #              (50,50), (-60,-60), (70,70), (-80,-80)
    # =============================================================================
    print("Starting Cubic Spline Motion for Axes 3 and 5")

    ret = Wmx3Lib_adv.CreateSplineBuffer(0, 100)
    if ret != 0:
        print("CreateSplineBuffer error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    splineCommand = AdvMotion_TotalTimeSplineCommand()
    splineCommand.dimensionCount = 2
    splineCommand.SetAxis(0, 3)
    splineCommand.SetAxis(1, 5)
    splineCommand.totalTimeMilliseconds = 1000

    splinePoints = []
    points_list = [(0,0), (10,10), (-20,-20), (30,30), (-40,-40), (50,50), (-60,-60), (70,70), (-80,-80)]
    for pt in points_list:
        sp = AdvMotion_SplinePoint()
        sp.SetPos(0, pt[0])
        sp.SetPos(1, pt[1])
        splinePoints.append(sp)

    ret = Wmx3Lib_adv.StartCSplinePos_TotalTime(0, splineCommand, len(splinePoints), splinePoints)
    if ret != 0:
        print("StartCSplinePos_TotalTime error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 5)
    ret = Wmx3Lib_cm.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error:", ret)
        exit()

    # =============================================================================
    # 3. Synchronous Control between Axes 3 and 5
    #    • Move Axis 3 to position 120 and Axis 5 to position 240 with velocity 1000
    # =============================================================================
    print("Starting Synchronous Motion for Axes 3 and 5")

    posCommand_master = Motion_PosCommand()
    posCommand_master.axis = 3
    posCommand_master.target = 120
    posCommand_master.profile.type = ProfileType.Trapezoidal
    posCommand_master.profile.velocity = 1000
    posCommand_master.profile.acc = 10000
    posCommand_master.profile.dec = 10000

    posCommand_slave = Motion_PosCommand()
    posCommand_slave.axis = 5
    posCommand_slave.target = 240
    posCommand_slave.profile.type = ProfileType.Trapezoidal
    posCommand_slave.profile.velocity = 1000
    posCommand_slave.profile.acc = 10000
    posCommand_slave.profile.dec = 10000

    ret = Wmx3Lib_cm.StartPos(posCommand_master)
    if ret != 0:
        print("StartPos (Axis 3) error:", ret)

    ret = Wmx3Lib_cm.StartPos(posCommand_slave)
    if ret != 0:
        print("StartPos (Axis 5) error:", ret)

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 5)
    ret = Wmx3Lib_cm.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error:", ret)
        exit()

    # =============================================================================
    # 4. PVT Interpolation Command for Axes 3 and 5
    #    • Define twenty points on a circle with:
    #         - Diameter = 100 (radius = 50)
    #         - Center = (-50, 0)
    #         - Constant velocities of 100 for both axes.
    #         - Time increments of 100ms per point.
    # =============================================================================
    print("Starting PVT Interpolation for Axes 3 and 5")

    pvtCommand = AdvMotion_PVTInterpolationCommand()
    pvtCommand.axisCount = 2
    pvtCommand.numPoints = 20

    radius = 50         # Because the diameter is 100
    center_x = -50
    center_y = 0
    num_points = 20
    angle_increment = (2 * math.pi) / num_points
    time_increment = 100  # in milliseconds

    for i in range(num_points):
        angle = i * angle_increment
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pvtPoint = AdvMotion_PVTPoint()
        # For Axis 3 (index 0)
        pvtPoint.SetPos(0, x)
        pvtPoint.SetVel(0, 100)
        # For Axis 5 (index 1)
        pvtPoint.SetPos(1, y)
        pvtPoint.SetVel(1, 100)
        pvtPoint.time = (i + 1) * time_increment
        pvtCommand.AddPoint(pvtPoint)

    ret = Wmx3Lib_adv.StartPVTInterpolation(pvtCommand)
    if ret != 0:
        print("StartPVTInterpolation error:", Wmx3Lib_adv.ErrorToString(ret))
        exit()

    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 3)
    axes.SetAxis(1, 5)
    ret = Wmx3Lib_cm.Wait_AxisSel(axes)
    if ret != 0:
        print("Wait_AxisSel error:", ret)
        exit()

    print("All motions completed successfully.")


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

