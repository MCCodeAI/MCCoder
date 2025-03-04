# Write python code to Set output bit 0.2 to be 1, sleep for 0.15 seconds, and then set it to be 0.
    # Axes = []

    # Set output bit 0.2 to be 1, 
    Wmx3Lib_Io = Io(Wmx3Lib)
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x01)
    if ret!=0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
    
    sleep(0.15)

    # Set output bit 0.2 to be 0.
    ret = Wmx3Lib_Io.SetOutBit(0x0, 0x02, 0x00)
    if ret!=0:
        print('SetOutBit error code is ' + str(ret) + ': ' + Wmx3Lib_Io.ErrorToString(ret))
        return
