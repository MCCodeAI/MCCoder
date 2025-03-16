
# Define Axes and IOs
Axes = [10, 12]
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
    path_0.fileName = f"153_o3-mini-M1_Log.txt"

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


    # Axes = [10, 12]
    # IOInputs = []
    # IOOutputs = []

    # Absolute triggered position command for Axis 10:
    #
    # 1. Start an absolute position command for Axis 10 to move to -800 with a velocity of 600.
    # 2. Without waiting (i.e. no wait(axis) here), set up a trigger so that when the remaining distance 
    #    for Axis 10 reaches 400, it automatically moves to 300 with a velocity of 1000.
    #
    # Then:
    #
    # 3. Set an event that monitors when Axis 10 reaches the position of 100. When that condition is 
    #    met, the event triggers an absolute position command for Axis 12 to move to -50. In this case,
    #    a wait is used to block further execution until Axis 12 stops moving.
    #
    # Note: It is assumed that all necessary classes, enumerations, and global objects such as 
    # Wmx3Lib_cm, Wmx3Lib_EventCtl, ProfileType, TriggerType, CoreMotionEventInputType, 
    # CoreMotionEventOutputType, Motion_PosCommand, Motion_TriggerPosCommand, and CoreMotionEventInput 
    # are already defined and available in the runtime environment.

    # ----- Absolute Triggered Motion for Axis 10 (No intermediate waiting) -----
    # Create the absolute motion command for Axis 10 to move to -800.
    posCmd10 = Motion_PosCommand()
    posCmd10.axis = 10
    posCmd10.profile.type = ProfileType.Trapezoidal
    posCmd10.profile.velocity = 600
    posCmd10.profile.acc = 10000  # Assumed acceleration value
    posCmd10.profile.dec = 10000  # Assumed deceleration value
    posCmd10.target = -800

    ret = Wmx3Lib_cm.motion.StartPos(posCmd10)
    if ret != 0:
        print("StartPos error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        # Exit or handle error as needed

    # Create the triggered motion command for Axis 10.
    # This command sets up a trigger that when the remaining distance for Axis 10 equals 400,
    # Axis 10 will move to 300 with a velocity of 1000.
    trigPosCmd10 = Motion_TriggerPosCommand()
    trigPosCmd10.axis = 10
    trigPosCmd10.profile.type = ProfileType.Trapezoidal
    trigPosCmd10.profile.velocity = 1000
    trigPosCmd10.profile.acc = 10000  # Assumed acceleration value
    trigPosCmd10.profile.dec = 10000  # Assumed deceleration value
    trigPosCmd10.target = 300
    trigPosCmd10.trigger.triggerType = TriggerType.RemainingDistance
    trigPosCmd10.trigger.triggerAxis = 10
    trigPosCmd10.trigger.triggerValue = 400

    ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCmd10)
    if ret != 0:
        print("StartPos_Trigger error code: " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        # Exit or handle error as needed

    # ----- Event Triggered Motion for Axis 12 (Using wait(axis)) -----
    # Create an event input that monitors when Axis 10 reaches the absolute position 100.
    eventIN = CoreMotionEventInput()
    eventIN.inputFunction = CoreMotionEventInputType.EqualPos
    eventIN.equalPos.axis = 10
    eventIN.equalPos.pos = 100

    # Create the motion command for Axis 12 to move to -50.
    posCmd12 = Motion_PosCommand()
    posCmd12.axis = 12
    posCmd12.profile.type = ProfileType.Trapezoidal
    posCmd12.profile.velocity = 600    # Chosen velocity for Axis 12 motion
    posCmd12.profile.acc = 10000        # Assumed acceleration value
    posCmd12.profile.dec = 10000        # Assumed deceleration value
    posCmd12.target = -50

    # Create the event output that will start the motion command for Axis 12.
    # It is assumed that the event output can be configured to launch a motion command.
    eventOut = CoreMotionEventOutput()
    eventOut.type = CoreMotionEventOutputType.StartMov
    # The motion command associated with the event output is set to posCmd12.
    eventOut.posCommand = posCmd12

    # Set the event (using event ID 0).
    ret, evID = Wmx3Lib_EventCtl.SetEvent(eventIN, eventOut, 0)
    if ret != 0:
        print("SetEvent error code: " + str(ret))
        # Exit or handle error as needed

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(0, 1)

    # Now wait for Axis 12 to complete its motion.
    Wmx3Lib_cm.motion.Wait(12)


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

