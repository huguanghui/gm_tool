import socket
import struct
# 创建TCP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
server_address = ('10.10.10.1', 1080)
sock.connect(server_address)
# 定义结构体格式
format_string = 'iifii'
data = (1, 2, 3.14, 4, 5)
message = "wakeup"
# 打包数据
packed_data = struct.pack(format_string, *data)
# 发送数据
# sock.sendall(packed_data)
sock.sendall(message.encode())
received_data = b''
received_data = sock.recv(1024)
print(received_data)
# 关闭套接字
sock.close()
