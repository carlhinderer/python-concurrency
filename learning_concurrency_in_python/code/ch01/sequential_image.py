import os
import threading
import time
import urllib.request


def downloadImage(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)

def main():
    t0 = time.time()
    for i in range(10):
        directory = os.getcwd() + '/output/'
        imageName = directory + "image-" + str(i) + ".jpg"
        downloadImage("https://picsum.photos/200/300", imageName)
  
    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution Time {}".format(totalTime))

if __name__ == '__main__':
    main()
