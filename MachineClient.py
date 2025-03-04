import socket

def SendCodetoMachine(code_data_raw):
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    server_addr = ("169.254.112.152", 7777)  #("115.236.153.172", 50871)
    tcp_socket.connect(server_addr)

    # 3. 发送数据
    # send_data = Codetest
    # tcp_socket.send(send_data.encode("utf-8"))

    import time
    
    send_data = code_data_raw
    tcp_socket.send(send_data.encode("utf-8"))

    time.sleep(0.1)
    send_data = 'exit'
    tcp_socket.send(send_data.encode("utf-8"))

    #4.从服务器接收数据
    tcp_remsg = tcp_socket.recv(1024) #注意这个1024byte，大小根据需求自己设置
    print(tcp_remsg.decode("utf-8"))  #如果要乱码可以使用tcp_remsg.decode("gbk")
    
    # 4. 关闭套接字
    tcp_socket.close()
    print("end")

    return tcp_remsg.decode("utf-8")

# SendCodetoMachine('code_data_raw')