
# Axes = []
# IOInputs = []
# IOOutputs = [1.1]

import time

# Assume Wmx3Lib and Io are already defined in the environment.
Wmx3Lib_Io = Io(Wmx3Lib)

# Define a helper function to set the IO output bit and check for errors.
def set_io_out_bit(byte_addr, bit_addr, value):
    ret = Wmx3Lib_Io.SetOutBit(byte_addr, bit_addr, value)
    if ret != 0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return False
    return True

# Repeat the cycle 5 times: Set IO output bit 1.1 to 1, wait 0.2 seconds, then set it to 0.
for i in range(5):
    # Set output bit 1.1 to 1.
    if not set_io_out_bit(1, 1, 1):
        break

    # Wait 0.2 seconds.
    time.sleep(0.2)
    
    # Set output bit 1.1 to 0.
    if not set_io_out_bit(1, 1, 0):
        break

    # Wait for the cycle to complete before starting the next cycle.
    # (No axis motion is involved so no additional wait is required here.)
