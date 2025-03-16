
# Axes = []
# IOInputs = []
# IOOutputs = [1.1]

# Write Python code to set IO output bit 1.1 to 1, wait 0.2 seconds, then set it to 0, repeating this cycle 5 times.
Wmx3Lib_Io = Io(Wmx3Lib)

for i in range(5):
    # Set output bit 1.1 to be 1
    ret = Wmx3Lib_Io.SetOutBit(0x1, 0x1, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    
    sleep(0.2)

    # Set output bit 1.1 to be 0
    ret = Wmx3Lib_Io.SetOutBit(0x1, 0x1, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
