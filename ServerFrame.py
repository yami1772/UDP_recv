# # FGI-ML-08光纤光栅解调模块RJ45网口	采用UDP通信
# IP及端口设置


'''
用户指令	
    01	02	读参数(设备型号,序列号,软硬件版本号, 本机IP地址、端口号、MAC地址，目的IP地址、端口号，设备温度，启停标志，通道数，子网掩码，默认网关)
	01	04	写本机IP地址，端口号，MAC地址，子网掩码，默认网关
	01	08	读取连续发送状态，波长/强度连续发送帧数
	01	0A	启停
			01 0C：0-7通道（面板通道编号1-8）光栅波长数据
			01 10：0-7通道（面板通道编号1-8）光栅峰值强度数据
			
	01	14	报警
	01	16	读某个通道（0~7/31，面板编号1~8/32）的光谱数据（最后一帧为波长和强度）
	01	17	读波长起始值、波长间隔、数据点数，通道数，返回数据帧数（读单通道光谱）
	01	20	读波长起始值、波长间隔、数据点数，通道数
	01	24	设置波长偏移量
	01	26	读取波长偏移量
'''

from socket import *
import numpy as np
import string

# 创建UDP套接字，使用IPv4协议
IPADDR = '192.168.0.119'
PORT = 4010
SOCKET = (IPADDR, PORT)
global s = socket(AF_INET, SOCK_DGRAM) 

# s.connect((IPADDR, PORTNUM))
# s.send('test string'.encode('hex'))
# s.close()

# DATA = 'A5 5A 00 08 04 0C 0D 0A'
# s.send(DATA)
# data = s.recv(4096)
# s.close()
# d = data.encode('hex').upper()
# print 'Received', repr(d)


# socket.socket([family[, type[, proto]]])
# 参数
#    family: 套接字家族可以使AF_UNIX或者AF_INET
#    type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
#    protocol: 一般不填默认为0

def case02():
    '''
    读参数
    '''
    print('读参数')
    # 将信息发送到解调仪
    HostSocket.sendto(0x0102, SOCKET)

    # 从服务器接收信息
    # 伪代码
    Message = Socket.recvfrom(80) 

    info 
    # 创建一个新字典，以序列 key 中元素做字典的键，val 为字典所有键对应的初始值
    key = ['Head', 'Model', 'Series', 'Version', 'IP', 'PORT', 'MAC', 'dest_IP', 'dest_PORT', 'Tmptr', 'isOn', 'Chnl', 'Mask', 'Gate']
    Message = np.arange(80)
    Description = dict(zip(key, Message))
    print(modifiedMessage.decode()) # 显示服务器返回的信息


def case04():
    print('04')


def case08():
    print('08')


def case0A():
    print('0A')


def case14():
    print('14')


def case16():
    print('16')


def case17():
    print('17')


def case20():
    print('20')


def case24():
    print('24')


def case26():
    print('26')


switch = {
    0x0102: case02,
    0x0104: case04,
    0x0108: case08,
    0x010A: case0A,
    0x0114: case14,
    0x0116: case16,
    0x0117: case17,
    0x0120: case20,
    0x0124: case24,
    0x0126: case26
}


switch[0x0102]()
