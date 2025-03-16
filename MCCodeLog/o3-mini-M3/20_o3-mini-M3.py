
# Axes = []
# IOInputs = [0.3]
# IOOutputs = [0.3]

def main():
    # Assume Wmx3Lib is the global library handle provided by the system.
    # Create an Io object instance for I/O operations.
    Wmx3Lib_Io = Io(Wmx3Lib)
    
    # Read IO input bit 0.3.
    ret, inValue = Wmx3Lib_Io.GetInBit(0x0, 0x03)
    if ret != 0:
        print('GetInBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    
    # Check the input value and determine the output.
    # If input is 1, set output bit 0.3 to 0; otherwise, set it to 1.
    if inValue == 1:
        outValue = 0
    else:
        outValue = 1

    # Set IO output bit 0.3.
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x03, outValue)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
