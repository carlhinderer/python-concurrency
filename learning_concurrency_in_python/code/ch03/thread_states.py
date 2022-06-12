import threading
import time

# Simple method for thread to execute
def thread_worker():
    print('My thread has entered the Running state.')
    time.sleep(10)
    print('My thread is terminating.')

# Still no resources allocated after this
my_thread = threading.Thread(target=thread_worker)

# Allocate resource and make thread runnable
my_thread.start()