
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# This script moves Axis 2 to the positions 2, -2, and then 2 sequentially
# using a JerkLimitedSCurve profile with the specified motion parameters.
#
# For each motion command, the script waits for the axis to finish moving 
# before issuing the next command.

def move_axis_jerk_limited(axis, target, velocity, acc, dec, jerkAcc, jerkDec, startingVelocity, endVelocity):
    # Create a motion position command using the JerkLimitedSCurve profile.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedSCurve
    posCommand.axis = axis
    posCommand.target = target
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = acc
    posCommand.profile.dec = dec
    posCommand.profile.jerkAcc = jerkAcc
    posCommand.profile.jerkDec = jerkDec
    posCommand.profile.startingVelocity = startingVelocity
    posCommand.profile.endVelocity = endVelocity

    # Execute command to move from current position to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return False
    
    # Wait until the axis has reached the target position and stopped moving.
    Wmx3Lib_cm.motion.Wait(axis)
    return True

# Motion parameters
axis = 2
velocity = 1000
acc = 10000
dec = 10000
jerkAcc = 1000
jerkDec = 1000
startingVelocity = 0
endVelocity = 0

# Move Axis 2 to position 2
if not move_axis_jerk_limited(axis, 2, velocity, acc, dec, jerkAcc, jerkDec, startingVelocity, endVelocity):
    exit(1)

# Move Axis 2 to position -2
if not move_axis_jerk_limited(axis, -2, velocity, acc, dec, jerkAcc, jerkDec, startingVelocity, endVelocity):
    exit(1)

# Move Axis 2 to position 2
if not move_axis_jerk_limited(axis, 2, velocity, acc, dec, jerkAcc, jerkDec, startingVelocity, endVelocity):
    exit(1)
