import os
import random
import threading
import time


def execute_thread(i):
    print("Thread {} started.".format(i))
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)
    print("Thread {} finished executing.".format(i))


# For simple situations, we can just run a single function
def start_function_threads():
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()
        print('Active Threads:', threading.enumerate())


# Code is more complex and needs to be broken up into multiple functions
class MyWorkerThread(threading.Thread):
    def __init__(self):
        print('Hello World!')
        threading.Thread.__init__(self)

    def run(self):
        print('Thread is now running...')


def start_class_threads():
    my_thread = MyWorkerThread()
    print('Created my Thread object.')
    my_thread.start()
    print('Started my thread.')
    my_thread.join()
    print('My thread finished.')


# We want to create an exact replica of a process
def child():
    print("We are in the child process with PID= %d" % os.getpid())

def parent():
    print("We are in the parent process with PID= %d" % os.getpid())
    new_ref = os.fork()
    if new_ref == 0:
        child()
    else:
        print('We are in the parent process and our child process has PID=%d' % new_ref)


# We want to create a background thread
def daemon_thread():
    while True:
        print('Sending out heartbeat signal...')
        time.sleep(2)

def start_daemon_thread():
    my_daemon_thread = threading.Thread(target=daemon_thread)
    my_daemon_thread.setDaemon(True)
    my_daemon_thread.start()



if __name__ == '__main__':
    # start_function_threads()
    # start_class_threads()
    # parent()
    # start_daemon_thread()
