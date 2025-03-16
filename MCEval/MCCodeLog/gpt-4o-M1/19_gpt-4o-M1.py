
# Axes = []
# IOInputs = []
# IOOutputs = [1.1]

from time import sleep

# Assuming Wmx3Lib and Io are predefined classes in the context
Wmx3Lib_Io = Io(Wmx3Lib)

# Repeat the cycle 5 times
for _ in range(5):
    # Set output bit 1.1 to be 1
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x01, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        break
    
    sleep(0.2)

    # Set output bit 1.1 to be 0
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x01, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        break
    
    sleep(0.2)
