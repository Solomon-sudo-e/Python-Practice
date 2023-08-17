from multiprocessing import Process, Value, Array, Lock, Pool
import os
import time
#MULTIPROCESSING

def cube(number):
    return number*number*number

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()

    #map, apply, join, close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
#
# def square_numbers():
#     for i in range(1000):
#         i * i
#
# def add_100(num, lock):
#     with lock:
#         for i in range(100):
#             time.sleep(0.01)
#             for i in range(len(num)):
#                 num[i] += 1
#
# if __name__ == '__main__':
#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print("array at beginning is ", shared_array[:])
#
#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=(shared_array, lock))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print('array at end is ', shared_array[:])
#
#
#     processes = []
#     num_processes = os.cpu_count()
#     # Create processes
#     for i in range(num_processes):
#         p = Process(target=square_numbers())
#         processes.append(p)
#
#     # start process
#     for p in processes:
#         p.start()
#
#     # join processes
#     for p in processes:
#         p.join()
#
#     print('end main')
#


#THREADS
from threading import Thread, Lock, current_thread
from queue import Queue


# database_value = 0
# def increase(lock):
#     global database_value
#
#     with lock:
#         local_copy = database_value
#
#         #processing
#         local_copy += 1
#         database_value = local_copy
#
# if __name__ == "__main__":
#     lock = Lock()
#     print('start value', database_value)
#
#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#     print('end value', database_value)
#
#     print('end main')

# def square_numbers():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)
#
# threads = []
# num_threads = 10
#
# for i in range(num_threads):
#     t = Thread(target=square_numbers())
#     threads.append(t)
#
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
#
#
# print('end main')
# #Why is activity manager showing only one thread when I init 10?

# def worker(q, lock):
#     while True:
#         value = q.get()
#
#         #processing
#         with lock:
#             print(f"in {current_thread().name} got {value}")
#         q.task_done()
#
#
# if __name__ ==  "__main__":
#     lock = Lock()
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)
#
#     # 3 2 1 -->
#     first = q.get()
#     # print(first)
#     q.task_done()
#     # q.join()
#
#     num_threads = 10
#
#     for i in range(num_threads):
#         thread = Thread(target=worker, args=(q,lock))
#         thread.daemon = True
#         thread.start()
#
#     for i in range(1, 21):
#         q.put(i)
#
#     q.join()
#
#     print('end main')