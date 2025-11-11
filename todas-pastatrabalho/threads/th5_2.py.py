import threading
import time
import os
from threading import Thread
from random import randint

# Lock definition
threadLock=threading.Lock()
counter=0
class MyThreadClass(Thread):
    def __init__(self,name,duration):
        Thread.__init__(self)
        self.name=name
        self.duration=duration

    def run(self):
        global counter   
        # acquire the Lock
        with threadLock:   
            for _ in range(100):        
                counter=counter+1

        print(f'final name={self.name}, duracao={self.duration} ') 
        
def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ",randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))
    thread10 = MyThreadClass("Thread#10 ", randint(1, 10))

    # Thread running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    # End
    print("End")
    print("counter=",counter) 
    # Execution Time
    print("--- %s seconds ---" % (time.time()-start_time))

if __name__ == "__main__":
    main()
