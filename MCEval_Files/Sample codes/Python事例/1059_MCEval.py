#Get the System statuses for the entire system. Get the ‘Cycle Time Milliseconds ’ and ‘Cycle Counter’ for Master 0.
    # Axes = [0]

    # Invalid License Error     TRUE: The detected license is invalid. Communication cannot be started with an invalid license.
    # Variable Name:   invalidLicenseError
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Invalid License Error : ' + str(CmStatus.invalidLicenseError))

    # Engine State      Status of the engine.
    # Variable Name:   engineState
    # Type:            EngineState::T
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Engine State : ' + str(CmStatus.engineState))

    # Number of Interrupts      The number of interrupts (cyclic handlers) that are currently running on the engine.
    # Variable Name:   numOfInterrupts
    # Type:            int
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Number of Interrupts : ' + str(CmStatus.numOfInterrupts))

    # Example of Master 0 Cycle Time Milliseconds
    master = 0
    # Cycle Time Milliseconds       The time between each communication cycle. The first index of the array corresponds to the first interrupt (cyclic handler), and the second index corresponds to the second interrupt. If only one interrupt is running on the engine, the second index will contain 0.
    # Variable Name:   cycleTimeMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cycle Time Milliseconds : ' + str(CmStatus.GetCycleTimeMilliseconds(master)))

    # Example of Master 0 Cycle Counter
    master = 0
    # Cycle Counter     A 64-bit integer containing the number of communication cycles that have elapsed since communication was last started. The first index of the array corresponds to the first interrupt (cyclic handler), and the second index corresponds to the second interrupt.
    # Variable Name:   cycleCounter
    # Type:            long long
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cycle Counter : ' + str(CmStatus.GetCycleCounter(master)))

    # Emergency Stop        TRUE: The system is in emergency stop state. FALSE: The system is not in emergency stop state.
    # Variable Name:   emergencyStop
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Emergency Stop : ' + str(CmStatus.emergencyStop))

    # Emergency Stop Level      The emergency stop level of the system, if Emergency Stop is TRUE
    # Variable Name:   emergencyStopLevel
    # Type:            EStopLevel::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Emergency Stop Level : ' + str(CmStatus.emergencyStopLevel))

