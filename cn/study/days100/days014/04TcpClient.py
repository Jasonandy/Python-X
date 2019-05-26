from socket import socket
from json import loads
from base64 import b64decode


# def main():
#     while True:
#         # 1.创建套接字对象默认使用IPv4和TCP协议
#         client = socket()
#         # 2.连接到服务器(需要指定IP地址和端口)
#         client.connect(('192.168.0.104', 6789))
#         # 3.从服务器接收数据
#         print(client.recv(1024).decode('utf-8'))
#         #client.close()
#
#
# if __name__ == '__main__':
#     main()


def main():
    client = socket()
    client.connect(('192.168.0.104', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    file_data = my_dict['file_data'].encode('utf-8')
    with open('' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(file_data))
    print('图片已保存.')


if __name__ == '__main__':
    main()
