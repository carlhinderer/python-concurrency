import time
from multiprocessing import Process


def my_worker():
    t1 = time.time()
    print("Process started at: {}".format(t1))
    time.sleep(20)

def start_and_end_process():
    myProcess = Process(target=my_worker)
    print("Process {}".format(myProcess))
    myProcess.start()
    print("Terminating Process...")
    myProcess.terminate()
    myProcess.join()
    print("Process Terminated: {}".format(myProcess))


if __name__ == '__main__':
    start_and_end_process()
