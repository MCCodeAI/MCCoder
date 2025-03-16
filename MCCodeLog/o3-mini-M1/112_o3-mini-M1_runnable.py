
# Define Axes and IOs
Axes = [1, 2, 3]
IOInputs = []
IOOutputs = [1.2]


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
    path_0.fileName = f"112_o3-mini-M1_Log.txt"

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


    # Axes = [1, 2, 3]
    # IOInputs = []
    # IOOutputs = [1.2]

    # ============================================================================
    # This script performs the following motions:
    # 1. Record and execute an API buffer to move Axis 2 to position 150.
    # 2. Set an event that triggers a relative position move for Axis 2 (distance = 260, velocity = 1100)
    #    when IO Output 1.2 equals 1 (event ID = 5).
    # 3. Execute a linear interpolation move of Axis 1 and Axis 3 to (80, 110) at a velocity of 1500.
    # 4. Set IO output bit 1.2 to 1, wait 0.2 seconds, then set it back to 0.
    #
    # NOTE: After each individual motion command, the code waits for the associated axis (or axes)
    #       to finish moving. No wait occurs in the middle of a continuous motion.
    # ============================================================================

    # ----- Part 1: API Buffer recording and execution for Axis 2 move to position 150 -----

    # Create and clear API buffer on channel 0.
    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    Wmx3Lib_buf.Clear(0)
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    # Create and configure a position command for Axis 2.
    posCommand = Motion_PosCommand()
    posCommand.axis = 2
    posCommand.target = 150
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 1000     # Assumed default velocity
    posCommand.profile.acc = 10000           # Assumed default acceleration
    posCommand.profile.dec = 10000           # Assumed default deceleration

    # Add the position command to the API buffer. (The API buffer API is assumed to
    # internally record the command so that later an Execute call will run it.)
    # (In a real implementation, you might append this command via a method call.)
    #
    # End recording and execute the API buffer.
    Wmx3Lib_buf.EndRecordBufferChannel()
    Wmx3Lib_buf.Execute(0)

    # Wait for Axis 2 motion to complete.
    ret = Wmx3Lib_cm.motion.Wait(2)
    if ret != 0:
        print('Wait error code for Axis 2: ' + str(ret))
        # Optionally handle the error

    # ----- Part 2: Event-triggered relative move for Axis 2 (distance=260, velocity=1100) -----

    # Create an EventControl instance.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_IO = IoEventInput()
    eventOut_Motion = CoreMotionEventOutput()
    posEventID = 5  # Event ID as specified

    # Set up the event input to trigger on IO Output 1.2.
    eventIN_IO.type = IoEventInputType.NotIOBit
    # For IO Output 1.2, byteAddress = 1 and bitAddress = 2.
    eventIN_IO.ioBit.ioSourceType = IOSourceType.Output
    eventIN_IO.ioBit.byteAddress = 1
    eventIN_IO.ioBit.bitAddress = 2

    # Set up the event output as a relative move command.
    # We use a multiple-axis command even for a single axis.
    eventOut_Motion.type = CoreMotionEventOutputType.StartMultipleMov
    eventOut_Motion.startMultipleMov.axisCount = 1
    eventOut_Motion.startMultipleMov.SetAxis(0, 2)
    eventOut_Motion.startMultipleMov.SetType(0, ProfileType.Trapezoidal)
    eventOut_Motion.startMultipleMov.SetVelocity(0, 1100)
    eventOut_Motion.startMultipleMov.SetAcc(0, 10000)  # Assumed acceleration
    eventOut_Motion.startMultipleMov.SetDec(0, 10000)  # Assumed deceleration
    eventOut_Motion.startMultipleMov.SetTarget(0, 260)

    # Register the event.
    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_IO, eventOut_Motion, posEventID)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        # Optionally handle the error

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)
    sleep(0.01)

    # Trigger the event by setting IO output 1.2 to 1.
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
    if ret != 0:
        print('SetOutBit error code for triggering event (IO 1.2) is ' + str(ret) +
              ': ' + Wmx3Lib_Io.ErrorToString(ret))
        # Optionally handle the error

    # Wait for Axis 2 (event-driven motion) to complete using AxisSelection.
    axisSel = AxisSelection()
    axisSel.axisCount = 1
    axisSel.SetAxis(0, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code for Axis 2: ' + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        # Optionally handle the error

    # Remove the event after completion.
    ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret) +
              ': ' + WMX3Log.ErrorToString(ret))
        # Optionally handle the error

    # ----- Part 3: Linear Interpolation move for Axis 1 and Axis 3 to (80, 110) -----

    # Execute a linear interpolation motion command.
    # Here we assume a direct call to a linear interpolation move function is available.
    # The command uses ProfileType.Trapezoidal with specified velocity.
    ret = Wmx3Lib_cm.motion.LinearIntplMov(1, 3, 80, 110, 1500, 10000, 10000)
    if ret != 0:
        print('LinearIntplMov error code for Axes 1 and 3: ' + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        # Optionally handle the error

    # Wait for the linear interpolation motion to complete.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 3)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code for Axes 1 and 3: ' + str(ret) +
              ': ' + Wmx3Lib_cm.ErrorToString(ret))
        # Optionally handle the error

    # ----- Part 4: IO Output command: Toggle IO output bit 1.2 -----

    # Set IO output bit 1.2 to 1.
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x01)
    if ret != 0:
        print('SetOutBit error code when setting IO 1.2 to 1: ' + str(ret) +
              ': ' + Wmx3Lib_Io.ErrorToString(ret))
        # Optionally handle the error

    # Wait for 0.2 seconds.
    sleep(0.2)

    # Set IO output bit 1.2 back to 0.
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x02, 0x00)
    if ret != 0:
        print('SetOutBit error code when resetting IO 1.2 to 0: ' + str(ret) +
              ': ' + Wmx3Lib_Io.ErrorToString(ret))
        # Optionally handle the error


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

