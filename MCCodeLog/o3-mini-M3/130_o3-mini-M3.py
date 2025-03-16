
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
