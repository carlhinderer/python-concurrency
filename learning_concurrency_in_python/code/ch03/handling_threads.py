import random
import threading
import time


# Start a bunch of threads
def execute_thread(i):
    print("Thread {} started".format(i))
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print("Thread {} finished executing".format(i))

def start_some_threads():
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()
        print("Active Threads:", threading.enumerate())


# Gets the total number of active threads
def num_active_threads():
    for i in range(random.randint(2, 50)):
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()

    time.sleep(4)
    print("Total number of active threads: {}".format(threading.active_count()))


# Get the current thread
def thread_target():
    print("Current Thread: {}".format(threading.current_thread()))

def show_current_threads():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=thread_target)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


# Get the main thread
def my_child_thread():
    print("Child Thread Starting")
    time.sleep(5)
    print("Current Thread ----------")
    print(threading.current_thread())
    print("-------------------------")
    print("Main Thread -------------")
    print(threading.main_thread())
    print("-------------------------")
    print("Child Thread Ending")

def get_main_from_child():
    child = threading.Thread(target=my_child_thread)
    child.start()
    child.join()


# Enumerate through all active threads
def my_thread(i):
    print("Thread {}: started".format(i))
    time.sleep(random.randint(1,5))
    print("Thread {}: finished".format(i))

def enumerate_active_threads():
    for i in range(4):
        thread = threading.Thread(target=my_thread, args=(i,))
        thread.start()

    print("Enumerating: {}".format(threading.enumerate()))



if __name__ == '__main__':
    # start_some_threads()
    # num_active_threads()
    # show_current_threads()
    # get_main_from_child()
    enumerate_active_threads()