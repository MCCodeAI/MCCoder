
# Axes = []
# IOInputs = []
# IOOutputs = [0.7]

import time

def main():
    # Create an IO instance
    Wmx3Lib_Io = Io(Wmx3Lib)  # Assumes that Io and Wmx3Lib have been defined elsewhere in the system

    # Set IO output bit 0.7 to 1
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

    time.sleep(0.1)

    # Set IO output bit 0.7 to 0
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

if __name__ == '__main__':
    main()
