
# Axes = [11]
# IOInputs = []
# IOOutputs = []

def move_axis(axis, target):
    # Create a new motion command using JerkLimitedSCurve profile
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedSCurve
    posCommand.axis = axis
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute command to move axis to the specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(axis)

def main():
    # Move Axis 11 to position 110 and wait until movement stops.
    move_axis(11, 110)
    
    # Move Axis 11 to position -99 and wait until movement stops.
    move_axis(11, -99)
    
    # Move Axis 11 to position 0 and wait until movement stops.
    move_axis(11, 0)

if __name__ == "__main__":
    main()
