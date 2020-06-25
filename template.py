
from socket import *
import numpy as np
import string
import struct

# 创建UDP套接字，使用IPv4协议
IPADDR = '192.168.0.119'
PORT = 4010

s = socket(AF_INET, SOCK_DGRAM) 
s.connect((IPADDR, PORT))

# s.connect((IPADDR, PORTNUM))
# s.send('test string'.encode('hex'))
# s.close()

# DATA = 'A5 5A 00 08 04 0C 0D 0A'
# s.send(DATA)
# data = s.recv(4096)
# s.close()
# d = data.encode('hex').upper()
# print 'Received', repr(d)

def case02():
    '''
    读参数
    '''
    global s
    # 将信息发送到解调仪并从服务器接收信息
    s.send(b'12'.encode('hex'))
    data = s.recv(80)
    s.close()

    # 拼装成字典
    info 
    # 创建一个新字典，以序列 key 中元素做字典的键，val 为字典所有键对应的初始值
    key = ['Head', 'Model', 'Series', 'Version', 'IP', 'PORT', 'MAC', 'dest_IP', 'dest_PORT', 'Tmptr', 'isOn', 'Chnl', 'Mask', 'Gate']
    Message = np.arange(80)
    Description = dict(zip(key, Message))

    # 显示服务器返回的信息
    print(modifiedMessage.decode())


def case04():
    print('04')
    a = 0x01
    byt = struct.pack('!B',a)
    print(byt)
    byt = b'\x00\x01\x00\x02'
    # 字节转化数字
    int_a = struct.unpack('!2H',byt)
    print(int_a)


switch = {
    0x0102: case02,
    0x0104: case04,
}


switch[0x0104]()

import struct

info = b'01040123456789ABCDEF1234123456789ABCDEF1234123456789ABCDEF'
infob = b'\x00\x01\x00\x04\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x00\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x00\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
# headinfo, IPaddr, PORTnum, MACaddr, MASKaddr = struct.unpack('57B', info)

a = struct.unpack('2B55s', info)