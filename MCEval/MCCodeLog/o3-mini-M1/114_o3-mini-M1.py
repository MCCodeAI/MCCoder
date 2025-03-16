
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

# ----- Section 1: Absolute Position Path Interpolation Motion Command (Axis 4 and 6) -----
# Create an absolute position path interpolation command for Axis 4 and 6 with auto-smoothing.
Wmx3Lib_adv = AdvancedMotion(Wmx3Lib)

path = AdvMotion_PathIntplCommand()

# Define the two axes: Axis 4 and Axis 6
path.SetAxis(0, 4)
path.SetAxis(1, 6)

# Use a single motion profile for the entire path.
path.enableConstProfile = 1
profile = Profile()
profile.type = ProfileType.Trapezoidal
profile.velocity = 1000
profile.acc = 10000
profile.dec = 10000
path.SetProfile(0, profile)

# Enable auto smoothing for the path.
path.enableAutoSmooth = 1

# Define 6 segments for the path interpolation.
path.numPoints = 6

# Segment 0: Move to (-40, -30) with autoSmoothRadius 10.
path.SetType(0, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 0, -40)   # Axis 4 target
path.SetTarget(1, 0, -30)   # Axis 6 target
path.SetAutoSmoothRadius(0, 10)

# Segment 1: Move to (10, -50) with autoSmoothRadius 20.
path.SetType(1, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 1, 10)    # Axis 4 target
path.SetTarget(1, 1, -50)   # Axis 6 target
path.SetAutoSmoothRadius(1, 20)

# Segment 2: Move to (-40, -70) with autoSmoothRadius 30.
path.SetType(2, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 2, -40)
path.SetTarget(1, 2, -70)
path.SetAutoSmoothRadius(2, 30)

# Segment 3: Move to (10, -90) with autoSmoothRadius 40.
path.SetType(3, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 3, 10)
path.SetTarget(1, 3, -90)
path.SetAutoSmoothRadius(3, 40)

# Segment 4: Move to (-40, -110) with autoSmoothRadius 50.
path.SetType(4, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 4, -40)
path.SetTarget(1, 4, -110)
path.SetAutoSmoothRadius(4, 50)

# Segment 5: Move to (10, -130) (no auto smoothing radius specified).
path.SetType(5, AdvMotion_PathIntplSegmentType.Linear)
path.SetTarget(0, 5, 10)
path.SetTarget(1, 5, -130)

# Start the absolute position path interpolation motion command.
ret = Wmx3Lib_adv.advMotion.StartPathIntplPos(path)
if ret != 0:
    print('StartPathIntplPos error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))
else:
    # Wait until both axes (4 and 6) have stopped moving.
    axes = AxisSelection()
    axes.axisCount = 2
    axes.SetAxis(0, 4)
    axes.SetAxis(1, 6)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axes)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_adv.ErrorToString(ret))


# ----- Section 2: API Buffer Execution for Sequential Position Commands on Axis 4 -----
# This section “records” a series of motion commands that will be executed in sequence.
# The sequence is:
#   1. Move Axis 4 to 111 at velocity 1000.
#   2. When remaining time is 8 ms (simulated wait), move Axis 4 to 222 at velocity 2000.
#   3. When remaining time is 9 ms (simulated wait), move Axis 4 to 333 at velocity 3000.

# Define a list to hold the API buffer commands.
apiBuffer = []

# Command 1: Immediate motion command.
cmd1 = {
    'axis': 4,
    'target': 111,
    'velocity': 1000,
    'triggerTime': None  # No delay trigger for the first command.
}
# Command 2: Motion command triggered when remaining time is 8 ms.
cmd2 = {
    'axis': 4,
    'target': 222,
    'velocity': 2000,
    'triggerTime': 8
}
# Command 3: Motion command triggered when remaining time is 9 ms.
cmd3 = {
    'axis': 4,
    'target': 333,
    'velocity': 3000,
    'triggerTime': 9
}

apiBuffer.extend([cmd1, cmd2, cmd3])

# Execute the buffered commands sequentially.
for cmd in apiBuffer:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = cmd['axis']
    posCommand.target = cmd['target']
    posCommand.profile.velocity = cmd['velocity']
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait for the axis to stop moving.
    # If a trigger time is specified, wait for that duration (simulating the API buffered action trigger)
    # Otherwise, wait with a default interval.
    if cmd['triggerTime'] is not None:
        Wmx3Lib_cm.motion.Wait(cmd['triggerTime'])
    else:
        # Use 8 ms as a default wait time for the first command.
        Wmx3Lib_cm.motion.Wait(8)


# ----- Section 3: Normal Type E-CAM Motion for Master Axis 4 and Slave Axis 6 -----
# First, move Axis 4 to -100 with a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = -100
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 4 stops moving.
    Wmx3Lib_cm.motion.Wait(8)

# Set up a Normal type E-CAM motion.
ECAMdata = AdvSync_ECAMData()
ECAMoption = AdvSync_ECAMOptions()

ECAMoption.type = AdvSync_ECAMType.Normal
ECAMoption.source.type = AdvSync_ECAMSourceType.MasterCommandPos
ECAMoption.clutch.type = AdvSync_ECAMClutchType.PyNone
ECAMoption.clutch.simpleCatchUpVelocity = 1000
ECAMoption.clutch.simpleCatchUpAcc = 10000

# Configure the E-CAM table with 7 points.
ECAMdata.masterAxis = 4
ECAMdata.slaveAxis = 6
ECAMdata.numPoints = 7
ECAMdata.options = ECAMoption

ECAMdata.SetMasterPos(0, -100)
ECAMdata.SetMasterPos(1, -50)
ECAMdata.SetMasterPos(2, 0)
ECAMdata.SetMasterPos(3, 50)
ECAMdata.SetMasterPos(4, 100)
ECAMdata.SetMasterPos(5, 150)
ECAMdata.SetMasterPos(6, 250)

ECAMdata.SetSlavePos(0, 100)
ECAMdata.SetSlavePos(1, 150)
ECAMdata.SetSlavePos(2, 100)
ECAMdata.SetSlavePos(3, 50)
ECAMdata.SetSlavePos(4, 100)
ECAMdata.SetSlavePos(5, 50)
ECAMdata.SetSlavePos(6, 150)

# Start the Normal type E-CAM motion on channel 0.
ret = Wmx3Lib_adv.advSync.StartECAM(0, ECAMdata)
if ret != 0:
    print('StartECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
else:
    # After starting ECAM, move Axis 4 to 300.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = 300
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
        # Wait until Axis 4 stops moving.
        Wmx3Lib_cm.motion.Wait(8)

    # Stop the E-CAM motion (this is a necessary step).
    ret = Wmx3Lib_adv.advSync.StopECAM(0)
    if ret != 0:
        print('StopECAM error code is ' + str(ret) + ': ' + Wmx3Lib.ErrorToString(ret))
