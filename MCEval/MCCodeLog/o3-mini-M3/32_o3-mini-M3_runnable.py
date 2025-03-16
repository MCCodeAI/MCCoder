
# Define Axes and IOs
Axes = [2, 3]
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
    path_0.fileName = f"32_o3-mini-M3_Log.txt"

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


    # Axes = [2, 3]
    # IOInputs = []
    # IOOutputs = []

    # This function executes a circular interpolation motion command and then waits for the axes to complete the motion.
    def execute_motion(command):
        ret = Wmx3Lib_cm.motion.StartCircularIntplPos_CenterAndLength(command)
        if ret != 0:
            print("StartCircularIntplPos_CenterAndLength error code is " + str(ret) +
                  ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return False

        # Wait for the motion to complete on Axis 2 and 3.
        axisSel = AxisSelection()
        axisSel.axisCount = 2
        axisSel.SetAxis(0, 2)
        axisSel.SetAxis(1, 3)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
        if ret != 0:
            print("Wait_AxisSel error code is " + str(ret) +
                  ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return False

        return True

    # -------------------------------
    # First Motion: Counterclockwise circular interpolation on Axis 2 and 3
    # Center position: (50, 0), Arc length: 180 degrees, Velocity: 1000
    # For counterclockwise motion, we set the "clockwise" flag to 0.
    circularCommand1 = Motion_CenterAndLengthCircularIntplCommand()
    circularCommand1.SetAxis(0, 2)
    circularCommand1.SetAxis(1, 3)
    circularCommand1.SetCenterPos(0, 50)
    circularCommand1.SetCenterPos(1, 0)
    circularCommand1.arcLengthDegree = 180
    circularCommand1.profile.type = ProfileType.Trapezoidal
    circularCommand1.profile.velocity = 1000
    circularCommand1.profile.acc = 10000
    circularCommand1.profile.dec = 10000
    circularCommand1.clockwise = 0  # 0 for counterclockwise

    if not execute_motion(circularCommand1):
        exit(1)

    # -------------------------------
    # Second Motion: Counterclockwise circular interpolation on Axis 2 and 3
    # Center position: (75, 0), Arc length: 180 degrees (velocity remains 1000)
    circularCommand2 = Motion_CenterAndLengthCircularIntplCommand()
    circularCommand2.SetAxis(0, 2)
    circularCommand2.SetAxis(1, 3)
    circularCommand2.SetCenterPos(0, 75)
    circularCommand2.SetCenterPos(1, 0)
    circularCommand2.arcLengthDegree = 180
    circularCommand2.profile.type = ProfileType.Trapezoidal
    circularCommand2.profile.velocity = 1000
    circularCommand2.profile.acc = 10000
    circularCommand2.profile.dec = 10000
    circularCommand2.clockwise = 0  # 0 for counterclockwise

    if not execute_motion(circularCommand2):
        exit(1)

    # -------------------------------
    # Third Motion: Clockwise circular interpolation on Axis 2 and 3
    # Center position: (25, 0), Arc length: 180 degrees (velocity remains 1000)
    circularCommand3 = Motion_CenterAndLengthCircularIntplCommand()
    circularCommand3.SetAxis(0, 2)
    circularCommand3.SetAxis(1, 3)
    circularCommand3.SetCenterPos(0, 25)
    circularCommand3.SetCenterPos(1, 0)
    circularCommand3.arcLengthDegree = 180
    circularCommand3.profile.type = ProfileType.Trapezoidal
    circularCommand3.profile.velocity = 1000
    circularCommand3.profile.acc = 10000
    circularCommand3.profile.dec = 10000
    circularCommand3.clockwise = 1  # 1 for clockwise

    if not execute_motion(circularCommand3):
        exit(1)

    # -------------------------------
    # Fourth Motion: Clockwise circular interpolation on Axis 2 and 3
    # Center position: (50, 0), Arc length: 180 degrees (velocity remains 1000)
    circularCommand4 = Motion_CenterAndLengthCircularIntplCommand()
    circularCommand4.SetAxis(0, 2)
    circularCommand4.SetAxis(1, 3)
    circularCommand4.SetCenterPos(0, 50)
    circularCommand4.SetCenterPos(1, 0)
    circularCommand4.arcLengthDegree = 180
    circularCommand4.profile.type = ProfileType.Trapezoidal
    circularCommand4.profile.velocity = 1000
    circularCommand4.profile.acc = 10000
    circularCommand4.profile.dec = 10000
    circularCommand4.clockwise = 1  # 1 for clockwise

    if not execute_motion(circularCommand4):
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

