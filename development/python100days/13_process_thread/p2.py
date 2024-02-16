from time import time
from multiprocessing import Process,Queue

def sum_func():
    number_list = [i for i in range(1,100000001)]
    total = 0
    start = time()
    for num in number_list:
        total += num
    print(total)
    end = time()
    print('Execution time: {:.2f} s'.format((end - start)))

def task_handler(curr_list,result_queue):
    total = 0
    for num in curr_list:
        total += num
    print('current total is',total,sep=' ')
    result_queue.put(total)

def main():
    processes = []
    result_queue = Queue()
    number_list = [i for i in range(1,100000001)]
    index = 0
    for _ in range(8):
        p = Process(target=task_handler,args=(number_list[index:index+12500000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: {:.2f} s'.format((end-start)))

if __name__ == '__main__':
    main()
    sum_func()