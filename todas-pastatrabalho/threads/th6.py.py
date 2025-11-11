import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(3)
item = 0


def consumer(name,u):
    print(name, u)
    
    logging.info('Consumer is waiting')
    print("semaphore=",semaphore)
    semaphore.acquire()

    logging.info('Consumer notify: item number {}'.format(item))



def producer(name,v):
    print(name, v)
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Producer notify: item number {}'.format(item))
    print("semaphore=",semaphore) 
    semaphore.release()


def main():
    for i in range(10):
        print("**************************************")
        t1 = threading.Thread(target=consumer,args=('th-consumer',i))
        t2 = threading.Thread(target=producer,args=('th-producer',i))
        print("testando o for: ",i)
        

        t1.start()
        t2.start()

        #t1.join()
        #t2.join()


if __name__ == "__main__":
    main()