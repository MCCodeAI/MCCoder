
# Axes = []
# IOInputs = []
# IOOutputs = [1.1]

Wmx3Lib_Io = Io(Wmx3Lib)

for _ in range(5):
    # Set output bit 1.1 to 1
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x01, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    
    sleep(0.2)
    
    # Set output bit 1.1 to 0
    ret = Wmx3Lib_Io.SetOutBit(0x01, 0x01, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
