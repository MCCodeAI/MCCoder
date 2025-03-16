
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
    path_0.fileName = f"67_o3-mini-M3_Log.txt"

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


    from WMX3ApiPython import *
    import time

    # Instantiate the advanced motion control object
    Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

    # Create a path interpolation command with rotation
    path = AdvMotion_PathIntplWithRotationCommand()
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    ret = Wmx3Lib_adv.advMotion.CreatePathIntplWithRotationBuffer(0, 1000)
    if ret != 0:
        print("CreatePathIntplWithRotationBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Configure the path interpolation with rotation channel:
    conf = AdvMotion_PathIntplWithRotationConfiguration()
    conf.SetAxis(0, 5)               # X axis is Axis 5
    conf.SetAxis(1, 6)               # Y axis is Axis 6
    conf.rotationalAxis = 3          # Rotational axis is Axis 3

    # Set the global center of rotation to (80, 80)
    conf.SetCenterOfRotation(0, 80)  # X axis center of rotation
    conf.SetCenterOfRotation(1, 80)  # Y axis center of rotation

    # Set auto smoothing radius to 10.
    conf.autoSmoothingRadius = 10

    # Set rotational axis motion profile parameters (Trapezoidal profile)
    conf.angleCorrectionProfile.type = ProfileType.Trapezoidal
    conf.angleCorrectionProfile.velocity = 1000
    conf.angleCorrectionProfile.acc = 1800
    conf.angleCorrectionProfile.dec = 1800

    # Enable rotation of the X and Y axes around the center of rotation.
    # (By not disabling the XY rotation, the axes rotate about the center)
    ret = Wmx3Lib_adv.advMotion.SetPathIntplWithRotationConfiguration(0, conf)
    if ret != 0:
        print("SetPathIntplWithRotationConfiguration error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Set the rotational axis (Axis 3) to single-turn mode.
    ret = Wmx3Lib_cm.config.SetSingleTurn(3, True, 360000)
    if ret != 0:
        print("SetSingleTurn error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Define 4 path interpolation points with local center of rotation for each segment.
    # Point numbering: 0 to 3

    # Point 0: Move to (160, 0) with local center rotation (50, 40)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)  # X target position
    point.SetTarget(1, 0)    # Y target position
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 50)  # Local center X = 50
    point.SetLocalCenterOfRotation(1, 40)  # Local center Y = 40
    path.SetPoint(0, point)

    # Point 1: Move to (160, 160) with local center rotation (60, 50)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 160)  # X target position
    point.SetTarget(1, 160)  # Y target position
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 60)  # Local center X = 60
    point.SetLocalCenterOfRotation(1, 50)  # Local center Y = 50
    path.SetPoint(1, point)

    # Point 2: Move to (0, 160) with local center rotation (50, 60)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)    # X target position
    point.SetTarget(1, 160)  # Y target position
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 50)  # Local center X = 50
    point.SetLocalCenterOfRotation(1, 60)  # Local center Y = 60
    path.SetPoint(2, point)

    # Point 3: Move to (0, 0) with local center rotation (40, 50)
    point = AdvMotion_PathIntplWithRotationCommandPoint()
    point.type = AdvMotion_PathIntplSegmentType.Linear
    point.profile = Profile()
    point.profile.type = ProfileType.Trapezoidal
    point.profile.velocity = 1000
    point.profile.acc = 2000
    point.profile.dec = 2000
    point.SetTarget(0, 0)    # X target position
    point.SetTarget(1, 0)    # Y target position
    point.useLocalCenterOfRotation = 1
    point.localCenterOfRotationDirection = 1
    point.SetLocalCenterOfRotation(0, 40)  # Local center X = 40
    point.SetLocalCenterOfRotation(1, 50)  # Local center Y = 50
    path.SetPoint(3, point)

    # Specify that the path contains 4 points
    path.numPoints = 4

    ret = Wmx3Lib_adv.advMotion.AddPathIntplWithRotationCommand(0, path)
    if ret != 0:
        print("AddPathIntplWithRotationCommand error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Execute the complete path interpolation with rotation.
    ret = Wmx3Lib_adv.advMotion.StartPathIntplWithRotation(0)
    if ret != 0:
        print("StartPathIntplWithRotation error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    # Wait for the entire path interpolation motion to complete.
    Wmx3Lib_cm.motion.Wait(0)

    # Poll until the path interpolation state is Idle
    timeoutCounter = 0
    pathStatus = AdvMotion_PathIntplWithRotationState()
    ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)
    while True:
        if pathStatus.state == AdvMotion_PathIntplWithRotationState.Idle:
            break
        time.sleep(0.1)
        timeoutCounter += 1
        if timeoutCounter > 500:
            break
        ret, pathStatus = Wmx3Lib_adv.advMotion.GetPathIntplWithRotationStatus(0)

    if timeoutCounter > 500:
        print("PathIntplWithRotation running timeout!")
        exit()

    # Free the interpolation buffer (should normally occur at the end of the application)
    ret = Wmx3Lib_adv.advMotion.FreePathIntplWithRotationBuffer(0)
    if ret != 0:
        print("FreePathIntplWithRotationBuffer error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    time.sleep(1)

    # Turn off single-turn mode for the rotational axis (Axis 3).
    AxisParam = Config_AxisParam()
    ret, AxisParam = Wmx3Lib_cm.config.GetAxisParam()
    AxisParam.SetSingleTurnMode(3, False)
    ret, AxisParamError = Wmx3Lib_cm.config.SetAxisParam(AxisParam)
    if ret != 0:
        print("Close SingleTurnMode error code is " + str(ret) + ": " + Wmx3Lib_adv.ErrorToString(ret))
        exit()

    time.sleep(1.6)


    # Write Python code to perform a soft landing, or torque control.
    INFINITE = int(0xFFFFFFFF)
    class WMX3SoftLand():
        def __init__(self):
            self.wmxApi = WMX3Api()
            self.Wmx3Lib_buf = ApiBuffer(self.wmxApi)
            self.Wmx3Lib_cm = CoreMotion(self.wmxApi)
            self.ApiBuffstu = ApiBufferStatus()
            self.Opsta = ApiBufferOptions()
        def SoftLandInit(self, channel):
            # Create devices.
            ret = self.wmxApi.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)
            if ret != 0:
                return ret
            time.sleep(0.1)
            # Free the buffer of the specified channel.
            ret = self.Wmx3Lib_buf.FreeApiBuffer(channel)
            time.sleep(0.01)
            # Create a buffer for the specified channel.
            ret = self.Wmx3Lib_buf.CreateApiBuffer(channel, 1024 * 1024 * 3)
            if ret != 0:
                return ret
        def SoftLandClose(self, channel):
            self.Wmx3Lib_buf.FreeApiBuffer(channel)
            self.wmxApi.CloseDevice()
        def GetApiBufferStu(self, channel):
            ret, self.ApiBuffstu = self.Wmx3Lib_buf.GetStatus(channel)
            return self.ApiBuffstu.remainingBlockCount
        def SoftLandApibufferData(self, channel, axis, StartPoint, SlowVelPoint, TargetPoint, FastVel, SlowVel, Acc, Trqlimit, SleepTime):
            self.Wmx3Lib_buf.Halt(channel)
            time.sleep(0.01)
            self.Wmx3Lib_buf.Clear(channel)
            time.sleep(0.01)
            # Start recording for the specified channel.
            self.Wmx3Lib_buf.StartRecordBufferChannel(0)
            # Create a command value.
            posCommand = Motion_PosCommand()
            posCommand.profile.type = ProfileType.Trapezoidal
            posCommand.axis = axis
            posCommand.target = StartPoint
            posCommand.profile.velocity = FastVel
            posCommand.profile.acc = Acc
            posCommand.profile.dec = Acc
            # Run to the starting position.
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_buf.Wait(axis)
            posCommand.target = SlowVelPoint
            posCommand.profile.velocity = FastVel
            posCommand.profile.endVelocity = SlowVel
            # Run at high speed to the low-speed point.
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_buf.Wait(axis)
            # Set torque limit.
            self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis, Trqlimit)
            posCommand.target = TargetPoint
            posCommand.profile.velocity = SlowVel
            posCommand.profile.startingVelocity = SlowVel
            posCommand.profile.endVelocity = 0
            # Run to the target point at low speed.
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_buf.Wait(axis)
            # Delay.
            self.Wmx3Lib_buf.Sleep(SleepTime * 1000)
            # Raise the process.
            posCommand.target = SlowVelPoint
            posCommand.profile.velocity = SlowVel
            posCommand.profile.startingVelocity = 0
            posCommand.profile.endVelocity = FastVel
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_buf.Wait(axis)
            # Lift torque restriction.
            self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis, 300)
            posCommand.target = StartPoint
            posCommand.profile.velocity = FastVel
            posCommand.profile.startingVelocity = FastVel
            posCommand.profile.endVelocity = 0
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_buf.Wait(axis)
            # End recording.
            self.Wmx3Lib_buf.EndRecordBufferChannel()
            self.Opsta.stopOnLastBlock = True
            self.Opsta.stopOnError = True
            self.Opsta.autoRewind = False
            self.Wmx3Lib_buf.SetOptions(channel, self.Opsta)
        def SoftLandMovStarPoint(self, axis, StartPoint, SlowVelPoint, FastVel, SlowVel, Acc):
            posCommand = Motion_PosCommand()
            posCommand.profile.type = ProfileType.Trapezoidal
            posCommand.axis = axis
            posCommand.profile.velocity = SlowVel
            posCommand.profile.acc = Acc
            posCommand.profile.dec = Acc
            posCommand.target = SlowVelPoint
            posCommand.profile.startingVelocity = 0
            posCommand.profile.endVelocity = FastVel
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_cm.Wait(axis)
            self.Wmx3Lib_cm.torque.SetMaxTrqLimit(axis, 300)
            posCommand.target = StartPoint
            posCommand.profile.velocity = FastVel
            posCommand.profile.startingVelocity = FastVel
            posCommand.profile.endVelocity = 0
            self.Wmx3Lib_cm.motion.StartPos(posCommand)
            self.Wmx3Lib_cm.Wait(axis)
        def SoftLandStart(self, channel):
            ret = self.Wmx3Lib_buf.Execute(channel)
            return ret

    def main():
        Wmx3Lib = WMX3Api()
        CmStatus = CoreMotionStatus()
        Wmx3Lib_cm = CoreMotion(Wmx3Lib)
        Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
        Wmx_Softland = WMX3SoftLand()
        print('Program begin.')
        time.sleep(1)

        # Create devices.
        ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)
        if ret != 0:
            print('CreateDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        Wmx3Lib.SetDeviceName('ApiBufferMotion')
        axis = 0
        timeoutCounter = 0
        for i in range(100):
            ret = Wmx3Lib.StartCommunication(INFINITE)
            if ret != 0:
                print('StartCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if CmStatus.engineState == EngineState.Communicating:
                break

        ret = Wmx3Lib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
        if ret != 0:
            print('ImportAndSetAll Parameters error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        time.sleep(0.5)

        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 1)
        while True:
            ret, CmStatus = Wmx3Lib_cm.GetStatus()
            if CmStatus.GetAxesStatus(axis).servoOn:
                break
            time.sleep(0.1)
        homeParam = Config_HomeParam()
        ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
        homeParam.homeType = Config_HomeType.CurrentPos
        ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)

        ret = Wmx3Lib_cm.home.StartHome(axis)
        if ret != 0:
            print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        Wmx3Lib_cm.motion.Wait(axis)

        ret = Wmx_Softland.SoftLandInit(0)
        if ret != 0:
            print('SoftLandInit error code is ' + str(ret))
        # Record a soft landing process:
        # Starting point=0, deceleration point=400, target point=500, high speed=1000, low speed=100,
        # acceleration/deceleration=10000, torque limit=30, sleep time=2 seconds.
        Wmx_Softland.SoftLandApibufferData(0, axis, 0, 400, 500, 1000, 100, 10000, 30, 2)
        ret = Wmx_Softland.SoftLandStart(0)
        if ret != 0:
            print('SoftLandStart error code is ' + str(ret))
        while True:
            cutter = Wmx_Softland.GetApiBufferStu(0)
            if cutter <= 0:
                break
            time.sleep(0.01)
        Wmx3Lib_cm.motion.Wait(axis)

        Wmx_Softland.SoftLandClose(0)
        ret = Wmx3Lib_cm.axisControl.SetServoOn(axis, 0)
        if ret != 0:
            print('SetServoOn to off error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        ret = Wmx3Lib.StopCommunication(INFINITE)
        if ret != 0:
            print('StopCommunication error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        ret = Wmx3Lib.CloseDevice()
        if ret != 0:
            print('CloseDevice error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
        print('Program End.')

    if __name__ == '__main__':
        main()

    time.sleep(5)  # Wait five seconds before stopping communication

    err = wmxlib_cm.axisControl.SetServoOn(0, 0)  # Set axis 0 servo off
    if err != ErrorCode.PyNone:
        print('Failed to set servo off %08x %s' % (err, CoreMotion.ErrorToString(wmxlib)))
        wmxlib.StopCommunication()
        wmxlib.CloseDevice()

    err = wmxlib.StopCommunication()
    if err != ErrorCode.PyNone:
        print('Failed StopCommunication %08x %s' % (err, WMX3Api.ErrorToString(wmxlib)))
        wmxlib.CloseDevice()

    err = wmxlib.CloseDevice()
    if err != ErrorCode.PyNone:
        print('Failed CloseDevice %08x %s' % (err, WMX3Api.ErrorToString(wmxlib)))

    print('Press any key to exit.')
    input()

    # Set output bit 0.2 to 1, sleep for 0.15 seconds, then set it to 0.
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    else:
        time.sleep(0.15)
        ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x00)
        if ret != 0:
            print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))


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

