
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
    path_0.fileName = f"130_o3-mini-M3_Log.txt"

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


    # -*- coding: utf-8 -*-

    import time

    # ------------------------------------------------------------------------
    # The following classes and functions are dummy implementations to
    # emulate the motion and event control API structure shown in the Context.
    # In your real environment, these will be provided by your motion libraries.
    # ------------------------------------------------------------------------

    # Enumerations (dummy values)
    class CoreMotionEventInputType:
        RemainingTime = 0

    class CoreMotionEventOutputType:
        StartMultiplePos = 0

    class ProfileType:
        Trapezoidal = 0

    # Dummy classes for event input and output
    class CoreMotionEventInput:
        pass

    class CoreMotionEventOutput:
        pass

    # Dummy EventControl class
    class EventControl:
        def __init__(self, lib):
            pass
        def SetEvent_ID(self, eventIn, eventOut, eventID):
            # In a real system, this would register the event.
            # Here we simply return success.
            return 0, eventID
        def EnableEvent(self, eventID, enable):
            # Enable (1) or disable (0) the event.
            print(f"Event {eventID} enabled: {enable}")
        def RemoveEvent(self, eventID):
            # Remove the registered event.
            return 0

    # Dummy motion command class
    class Motion_PosCommand:
        def __init__(self):
            self.profile = type('Profile', (), {})()
            self.profile.type = None
            self.profile.velocity = None
            self.profile.acc = None
            self.profile.dec = None
            self.axis = None
            self.target = None

    # Dummy class for selecting axes when waiting for motion completion.
    class AxisSelection:
        def __init__(self):
            self.axisCount = 0
            self.axes = []
        def SetAxis(self, index, axis):
            if len(self.axes) <= index:
                self.axes.extend([None]*(index+1-len(self.axes)))
            self.axes[index] = axis

    # Dummy motion API to simulate movement commands and waiting
    class MotionAPI:
        def StartPos(self, posCommand):
            print(f"Started motion on Axis {posCommand.axis}: Move to {posCommand.target} with velocity {posCommand.profile.velocity}")
            return 0
        def Wait(self, axis):
            # Wait for a given axis to finish its motion.
            print(f"Waiting for Axis {axis} to complete its movement...")
            time.sleep(0.5)
            return 0
        def Wait_AxisSel(self, axisSel):
            # Block until each selected axis is idle.
            print(f"Waiting for axes {axisSel.axes} to stop moving...")
            time.sleep(0.5)
            return 0

    # Dummy library instances (placeholders)
    Wmx3Lib = None
    Wmx3Lib_cm = type('Wmx3Lib_cm', (), {})()
    Wmx3Lib_cm.motion = MotionAPI()
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

    # ------------------------------------------------------------------------
    # Main Code
    # ------------------------------------------------------------------------

    # 1. Set up the event input.
    #    Monitor if the RemainingTime of Axis 2's movement equals 1000ms.
    eventIN_Motion = CoreMotionEventInput()
    eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
    # Using a dummy structure to hold remainingTime parameters.
    eventIN_Motion.remainingTime = type('RemainingTimeParams', (), {})()
    eventIN_Motion.remainingTime.axis = 2
    eventIN_Motion.remainingTime.timeMilliseconds = 1000
    eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

    # 2. Set up the event output.
    #    The event triggers a multi-axis absolute position command:
    #      • Axis 1 moves to position 500 at a speed of 1000.
    #      • Axis 2 moves to position 2000 with a speed of 1000.
    eventOut_Motion = CoreMotionEventOutput()
    eventOut_Motion.type = CoreMotionEventOutputType.StartMultiplePos
    # Create a dummy container for multiple position command parameters.
    eventOut_Motion.startMultiplePos = type('StartMultiplePos', (), {})()
    eventOut_Motion.startMultiplePos.axisCount = 2

    # For convenience, define helper functions to set parameters.
    def SetAxis(index, axis):
        if not hasattr(eventOut_Motion.startMultiplePos, 'axes'):
            eventOut_Motion.startMultiplePos.axes = {}
        eventOut_Motion.startMultiplePos.axes[index] = axis

    def SetType(index, profileType):
        if not hasattr(eventOut_Motion.startMultiplePos, 'types'):
            eventOut_Motion.startMultiplePos.types = {}
        eventOut_Motion.startMultiplePos.types[index] = profileType

    def SetVelocity(index, velocity):
        if not hasattr(eventOut_Motion.startMultiplePos, 'velocities'):
            eventOut_Motion.startMultiplePos.velocities = {}
        eventOut_Motion.startMultiplePos.velocities[index] = velocity

    def SetAcc(index, acc):
        if not hasattr(eventOut_Motion.startMultiplePos, 'accs'):
            eventOut_Motion.startMultiplePos.accs = {}
        eventOut_Motion.startMultiplePos.accs[index] = acc

    def SetDec(index, dec):
        if not hasattr(eventOut_Motion.startMultiplePos, 'decs'):
            eventOut_Motion.startMultiplePos.decs = {}
        eventOut_Motion.startMultiplePos.decs[index] = dec

    def SetTarget(index, target):
        if not hasattr(eventOut_Motion.startMultiplePos, 'targets'):
            eventOut_Motion.startMultiplePos.targets = {}
        eventOut_Motion.startMultiplePos.targets[index] = target

    # Attach helper functions.
    eventOut_Motion.startMultiplePos.SetAxis = SetAxis
    eventOut_Motion.startMultiplePos.SetType = SetType
    eventOut_Motion.startMultiplePos.SetVelocity = SetVelocity
    eventOut_Motion.startMultiplePos.SetAcc = SetAcc
    eventOut_Motion.startMultiplePos.SetDec = SetDec
    eventOut_Motion.startMultiplePos.SetTarget = SetTarget

    # Configure the parameters for the two axes.
    # For Axis 1 (first motion command)
    eventOut_Motion.startMultiplePos.SetAxis(0, 1)
    eventOut_Motion.startMultiplePos.SetType(0, ProfileType.Trapezoidal)
    eventOut_Motion.startMultiplePos.SetVelocity(0, 1000)
    eventOut_Motion.startMultiplePos.SetAcc(0, 10000)
    eventOut_Motion.startMultiplePos.SetDec(0, 10000)
    eventOut_Motion.startMultiplePos.SetTarget(0, 500)

    # For Axis 2 (second motion command)
    eventOut_Motion.startMultiplePos.SetAxis(1, 2)
    eventOut_Motion.startMultiplePos.SetType(1, ProfileType.Trapezoidal)
    eventOut_Motion.startMultiplePos.SetVelocity(1, 1000)  # Assumed same speed as Axis 1
    eventOut_Motion.startMultiplePos.SetAcc(1, 10000)
    eventOut_Motion.startMultiplePos.SetDec(1, 10000)
    eventOut_Motion.startMultiplePos.SetTarget(1, 2000)

    # 3. Register (set) the event with a chosen Event ID.
    eventID = 0
    ret, registeredEventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print("Error: SetEvent_ID returned error code", ret)
        exit()

    # 4. Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    # ------------------------------------------------------------------------
    # At this point the event is set up.
    # It is assumed that Axis 2 is already in motion.
    # When the RemainingTime for Axis 2’s motion reaches 1000ms,
    # the event will trigger and execute a multi-axis absolute command:
    #   - Axis 1 will move to position 500 at speed 1000.
    #   - Axis 2 will move to position 2000.
    # ------------------------------------------------------------------------

    # Wait for the triggered motion commands to be executed.
    # Wait for the event trigger (here we simulate a short delay).
    time.sleep(0.01)

    # Instead of waiting separately for Axis 1 first (which would introduce
    # an unnecessary pause in a continuous multi-axis command),
    # we now only wait for both axes to complete their motions.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print("Error: Wait_AxisSel returned error code", ret)
        exit()

    # 5. Remove the event after execution.
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print("Error: RemoveEvent returned error code", ret)
        exit()

    print("Event-triggered motions executed successfully.")


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

