
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
    path_0.dirPath = r"\\Mac\\Home\\Documents\\GitHub\\MCCodeLog\\o3-mini-M3"
    path_0.fileName = f"153_o3-mini-M3_Log.txt"

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

    def main():
        # -------------------------------
        # Step 1: Configure an event so that when Axis 10 reaches position 100,
        #         Axis 12 will start an absolute move to -50.
        # -------------------------------
        # Create an event control object (assumes Wmx3Lib is already available).
        Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
        eventIN = CoreMotionEventInput()
        eventOUT = CoreMotionEventOutput()
        # Change the eventID to avoid the "IDInUse" error. Using 2 instead of 1.
        eventID = 2

        # Set the event input: When Axis 10's position equals 100.
        eventIN.inputFunction = CoreMotionEventInputType.EqualPos
        eventIN.equalPos.axis = 10
        eventIN.equalPos.pos = 100

        # Set the event output: Start an absolute position command on Axis 12.
        eventOUT.type = CoreMotionEventOutputType.StartSinglePos
        eventOUT.startSinglePos.axis = 12
        eventOUT.startSinglePos.type = ProfileType.Trapezoidal
        eventOUT.startSinglePos.target = -50
        eventOUT.startSinglePos.velocity = 1000
        eventOUT.startSinglePos.acc = 10000
        eventOUT.startSinglePos.dec = 10000

        ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN, eventOUT, eventID)
        if ret != 0:
            print('SetEvent_ID error code is', ret)
            return
        Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

        # -------------------------------
        # Step 2: Execute Axis 10 absolute triggered position command.
        #         First, command Axis 10 to move to -800 at 600 velocity.
        #         Then, when its remaining distance equals 400, trigger a new command
        #         for Axis 10 to move to 300 at 1000 velocity.
        #         (Do not call a wait() function in between these two commands.)
        # -------------------------------
        # Start the first (absolute) motion command for Axis 10.
        posCommand = Motion_PosCommand()
        posCommand.axis = 10
        posCommand.target = -800
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.profile.velocity = 600
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        if ret != 0:
            print('StartPos error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
            return

        # Immediately set up the triggered command for Axis 10.
        trigCommand = Motion_TriggerPosCommand()
        trigCommand.axis = 10
        trigCommand.target = 300
        trigCommand.profile.type = ProfileType.Trapezoidal
        trigCommand.profile.velocity = 1000
        trigCommand.profile.acc = 10000
        trigCommand.profile.dec = 10000

        # Configure the trigger: When the remaining distance of Axis 10 equals 400.
        trig = Trigger()
        trig.triggerAxis = 10
        trig.triggerType = TriggerType.RemainingDistance
        trig.triggerValue = 400
        trigCommand.trigger = trig

        ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigCommand)
        if ret != 0:
            print('StartPos_Trigger error code is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
            return

        # -------------------------------
        # Step 3: Wait for the motions of each axis to complete.
        #         (Wait for the complete continuous motion of Axis 10,
        #         and then wait (blocking) for the event-triggered move on Axis 12.)
        # -------------------------------
        # Wait for Axis 10 to finish its triggered motion sequence.
        axisSel10 = AxisSelection()
        axisSel10.axisCount = 1
        axisSel10.SetAxis(0, 10)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel10)
        if ret != 0:
            print('Wait_AxisSel error code for Axis 10 is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait for Axis 12 to finish the event-triggered motion.
        axisSel12 = AxisSelection()
        axisSel12.axisCount = 1
        axisSel12.SetAxis(0, 12)
        ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel12)
        if ret != 0:
            print('Wait_AxisSel error code for Axis 12 is', ret, ':', Wmx3Lib_cm.ErrorToString(ret))
            return

        # -------------------------------
        # Step 4: Remove the event after the motion is complete.
        # -------------------------------
        ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
        if ret != 0:
            print('RemoveEvent error code is', ret)
            return

    if __name__ == "__main__":
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

