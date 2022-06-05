import os
import threading
import time
import urllib.request


def downloadImage(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Completed Download")

def executeThread(i): 
    directory = os.getcwd() + '/output/'
    imageName = directory + "image-" + str(i) + ".jpg"
    downloadImage("https://picsum.photos/200/300", imageName)

def main():
    t0 = time.time()
    threads = []

    # Create 10 threads, append them to our array of threads, and start them off
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()
  
    # ensure that all the threads in our array have completed
    # their execution before we log the total time to complete
    for i in threads:
        i.join()

    # calculate the total execution time
    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution Time {}".format(totalTime))


if __name__ == '__main__':
    main()
