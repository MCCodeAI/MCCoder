
# Axes = []
# IOInputs = []
# IOOutputs = [0.7]

from time import sleep

def main():
    # Set output bit 0.7 to be 1
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x01)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

    sleep(0.1)

    # Set output bit 0.7 to be 0.
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x07, 0x00)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
