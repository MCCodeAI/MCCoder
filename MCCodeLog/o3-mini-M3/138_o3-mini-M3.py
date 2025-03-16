
# Axes = [10]
# IOInputs = []
# IOOutputs = []

def wait_until_idle(axis):
    # Poll the controller status for the specified axis until it is idle.
    # Depending on the actual API, adjust the status field and idle check as needed.
    status = Wmx3Lib_cm.GetStatus()
    # Assuming status.axesStatus is a list and each element has an "operationState" field,
    # and that OperationState.Idle is the idle state.
    while status.axesStatus[axis].operationState != OperationState.Idle:
        Wmx3Lib_cm.motion.Wait(10)
        status = Wmx3Lib_cm.GetStatus()

# --------- Correction Start: Ensure the servo for Axis 10 is turned on before issuing any motion command.
ret = Wmx3Lib_cm.axisControl.SetServoOn(10, 1)
if ret != 0:
    print("Failed to set servo on for Axis 10: " + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
# --------- Correction End

# Command 1: Move Axis 10 to position -10 using the TimeAccAdvancedS profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 10
posCommand.target = -10
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error (TimeAccAdvancedS) on Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
wait_until_idle(10)  # Wait until Axis 10 stops moving

# Command 2: Move Axis 10 to position 20 using the TwoVelocityTrapezoidal profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
posCommand.axis = 10
posCommand.target = 20
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error (TwoVelocityTrapezoidal) on Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
wait_until_idle(10)  # Wait until Axis 10 stops moving

# Command 3: Move Axis 10 to position -30 using the ConstantDec profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 10
posCommand.target = -30
# For ConstantDec, only starting and end velocities are needed.
posCommand.profile.startingVelocity = 10000
posCommand.profile.endVelocity = 2000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error (ConstantDec) on Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
wait_until_idle(10)  # Wait until Axis 10 stops moving

# Command 4: Move Axis 10 to position 40 using the ParabolicVelocity profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.axis = 10
posCommand.target = 40
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 150
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 1.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error (ParabolicVelocity) on Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
wait_until_idle(10)  # Wait until Axis 10 stops moving

# Command 5: Move Axis 10 to position 0 using the JerkRatioFixedVelocityS profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
posCommand.axis = 10
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error (JerkRatioFixedVelocityS) on Axis 10: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()
wait_until_idle(10)  # Wait until Axis 10 stops moving
