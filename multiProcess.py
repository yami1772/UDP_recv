import threading #导入threading库
import time
 
def run(n):
    print("task", n)
    time.sleep(1) #延时一秒
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)
 
if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1",))#创建线程1，取名为t1
    t2 = threading.Thread(target=run, args=("t2",))#创建线程2，取名为t2
    t1.start() #开启线程t1
    t2.start() #开启线程t2
