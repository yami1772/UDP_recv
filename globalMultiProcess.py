import threading
import time
 
num = 100
 
def work1():
    global num
    for i in range(3):
        num += 1
    print("in work1 num is : %d" % num)
 
def work2():
    global num
    print("in work2 num is : %d" % num)
 
if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=work2)
