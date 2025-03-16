
# Define Axes and IOs
Axes = [10]
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
    path_0.fileName = f"138_o3-mini-M1_Log.txt"

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


    # Axes = [10]
    # IOInputs = []
    # IOOutputs = []

    def main():
        # Segment 1: Move Axis 10 to -10 using TimeAccAdvancedS profile
        pos1 = Motion_PosCommand()
        pos1.axis = 10
        pos1.target = -10
        pos1.profile.type = ProfileType.TimeAccAdvancedS
        # Set profile parameters (values chosen arbitrarily as an example)
        pos1.profile.velocity = 50
        pos1.profile.acc = 200    # Time acceleration (ms)
        pos1.profile.dec = 200    # Time deceleration (ms)
    
        ret = Wmx3Lib_cm.motion.StartPos(pos1)
        if ret != 0:
            print('StartPos (TimeAccAdvancedS) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        # Wait until axis 10 stops moving after segment 1
        ret = Wmx3Lib_cm.motion.Wait(10)
        if ret != 0:
            print('Wait after segment 1 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Segment 2: Move Axis 10 to 20 using TwoVelocityTrapezoidal profile
        pos2 = Motion_PosCommand()
        pos2.axis = 10
        pos2.target = 20
        pos2.profile.type = ProfileType.TwoVelocityTrapezoidal
        # Set profile parameters (example values)
        pos2.profile.velocity = 100
        pos2.profile.acc = 1000
        pos2.profile.dec = 1000

        ret = Wmx3Lib_cm.motion.StartPos(pos2)
        if ret != 0:
            print('StartPos (TwoVelocityTrapezoidal) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        # Wait until axis 10 stops moving after segment 2
        ret = Wmx3Lib_cm.motion.Wait(10)
        if ret != 0:
            print('Wait after segment 2 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Segment 3: Move Axis 10 to -30 using ConstantDec profile
        pos3 = Motion_PosCommand()
        pos3.axis = 10
        pos3.target = -30
        pos3.profile.type = ProfileType.ConstantDec
        # Set profile parameters (example values)
        pos3.profile.velocity = 80
        pos3.profile.dec = 1200  # constant deceleration value

        ret = Wmx3Lib_cm.motion.StartPos(pos3)
        if ret != 0:
            print('StartPos (ConstantDec) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        # Wait until axis 10 stops moving after segment 3
        ret = Wmx3Lib_cm.motion.Wait(10)
        if ret != 0:
            print('Wait after segment 3 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Segment 4: Move Axis 10 to 40 using ParabolicVelocity profile
        pos4 = Motion_PosCommand()
        pos4.axis = 10
        pos4.target = 40
        pos4.profile.type = ProfileType.ParabolicVelocity
        # Set profile parameters (example values)
        pos4.profile.velocity = 90
        pos4.profile.acc = 800
        pos4.profile.dec = 800

        ret = Wmx3Lib_cm.motion.StartPos(pos4)
        if ret != 0:
            print('StartPos (ParabolicVelocity) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        # Wait until axis 10 stops moving after segment 4
        ret = Wmx3Lib_cm.motion.Wait(10)
        if ret != 0:
            print('Wait after segment 4 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Segment 5: Move Axis 10 to 0 using JerkRatioFixedVelocityS profile
        pos5 = Motion_PosCommand()
        pos5.axis = 10
        pos5.target = 0
        pos5.profile.type = ProfileType.JerkRatioFixedVelocityS
        # Set profile parameters (example values similar to provided example)
        pos5.profile.velocity = 1000
        pos5.profile.acc = 10000
        pos5.profile.dec = 10000
        pos5.profile.jerkAccRatio = 0.5
        pos5.profile.jerkDecRatio = 0.5
        pos5.profile.startingVelocity = 0
        pos5.profile.endVelocity = 0

        ret = Wmx3Lib_cm.motion.StartPos(pos5)
        if ret != 0:
            print('StartPos (JerkRatioFixedVelocityS) error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return
        # Wait until axis 10 stops moving after segment 5
        ret = Wmx3Lib_cm.motion.Wait(10)
        if ret != 0:
            print('Final Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

    if __name__ == '__main__':
        main()


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

