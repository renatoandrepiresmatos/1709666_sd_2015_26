# importing the modules 
from threading import *         
import time         
  
# creating thread instance where count = 3 
# Up to three threads can be active between acquire and release.
obj = Semaphore(3)         
  
# creating instance 
def display(name):     
    
    # calling acquire method 
    print("acquire")
    obj.acquire()                 
    for i in range(5): 
        print('Hello, ', name) 
        time.sleep(1) 
        print(name,i,obj) 
          
        # calling release method 
    obj.release()  
    print("realese")
          
# creating multiple thread  
t1 = Thread(target = display , args = ('Thread-1',)) 
t2 = Thread(target = display , args = ('Thread-2',)) 
t3 = Thread(target = display , args = ('Thread-3',)) 
t4 = Thread(target = display , args = ('Thread-4',)) 
t5 = Thread(target = display , args = ('Thread-5',)) 
  
# calling the threads  
t1.start() 
t2.start() 
t3.start() 
t4.start() 
t5.start()