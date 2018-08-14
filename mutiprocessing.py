from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下載完成! 耗費了%d秒' % (filename, time_to_download))

def noMult():
    start = time()
    download_task('Python從入門到住院.pdf')
    download_task('Peking hot.avi')
    end = time()
    print('總共耗費了%.2f秒.' %(end - start))

def download_task_multi(filename):
    print('總共下載進程，進程號[%d].' % getpid())
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下載完成! 耗費了%d秒' % (filename, time_to_download))

def multiPro():
    start = time()
    p1 = Process(target=download_task_multi, args=('Python從入門到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task_multi, args=('Peking hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('總共耗費了%.2f秒.' % (end - start))

def main():
    print("使用mutiprocess前.....")
    noMult()
    print("使用後................")
    multiPro()


if __name__ == '__main__':
    main()