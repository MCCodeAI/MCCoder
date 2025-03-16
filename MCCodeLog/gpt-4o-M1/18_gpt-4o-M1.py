
# Axes = []
# IOInputs = []
# IOOutputs = [0.7]

from time import sleep

# Assuming Wmx3Lib and Io are defined elsewhere in the code
Wmx3Lib_Io = Io(Wmx3Lib)

# Set output bit 0.7 to be 1
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x01)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return

sleep(0.1)

# Set output bit 0.7 to be 0
ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x00)
if ret != 0:
    print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
    return
