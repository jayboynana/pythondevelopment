from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download(filename):
    print('Starting download process, PID:{:d}.'.format(getpid()))
    print('Starting download %s...',filename)
    time_to_download = randint(1,5)
    sleep(time_to_download)
    print('Finished! download cost: {:2f} seconds'.format(time_to_download))

def main():
    start = time()
    p1 = Process(target=download,args=('file1.jpg',))
    p1.start()
    p2 = Process(target=download,args=('file2.jpg',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Total cost time:{:.2f} seconds'.format((end-start)))

if __name__ == '__main__':
    main()