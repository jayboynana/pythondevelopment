from multiprocessing import Process, Queue,Value

def worker1(queue,string,count):

    while count.value < 10:
        with count.get_lock():
            if count.value % 2 == 0:
                queue.put(string)
                # print(string,end=' ')
                count.value += 1

def worker2(queue,string,count):

    while count.value < 10:
        with count.get_lock():
            if count.value % 2 !=0:
                queue.put(string)
                # print(string,end=' ')
                count.value += 1

def main():

    count = Value('i',0)
    queue = Queue()

    p1 = Process(target=worker1,args=(queue,'ping',count))
    p2 = Process(target=worker2,args=(queue,'pong',count))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    for _ in range(10):
        print(queue.get(),end=' ')


if __name__ == '__main__':
    main()