# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:38:26 2016

@author: Administrator
"""

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num 
        time.sleep(5)

        #if mutex.acquire(1):  
        num = num+1
        msg = self.name+' set num to '+str(num)
        print(msg)
         #   mutex.release()


num = 0
mutex = threading.Lock()
def test():
    for i in range(4):
        t = MyThread()
        t.start()
        
        
if __name__ == '__main__':
    test()