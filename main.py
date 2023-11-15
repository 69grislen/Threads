# import threading
# import time
#
# lock = threading.Lock()
#
# def print_numbers():
#     lock.acquire()
#     for i in range(5):
#         print(i)
#         time.sleep(1)
#     lock.release()
#
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_numbers)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# import threading
#
# def consuver():
#     with condition:
#         condition.wait()
#         print("Consumer consumed the utem")
#         condition.notify()
#
# def producer():
#     with condition:
#         condition.wait()
#         print("Producer produced the item")
#         condition.notify()
#
# condition = threading.Condition()

# import datetime
# from threading import Semaphore, Thread
# from time import sleep
#
# s = Semaphore(3)
#
# def semaphore_func():
#     s.acquire()
#     now = datetime.datetime.now().strftime('%H:%M:%S')
#     print(f'{now}, {payload}')
#     sleep(2)
#     s.release()
#
# #генератор потоков
# threads = [Thread(target=semaphore_func, args=(1,)) for i in range(7)]
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()



# from queue import  Queue
# from threading import Thread
#
# def worker(q):
#     while True:
#         item = q.get
#
#     q.task_done()
#
# q = Queue
# num_threads = 4
#
# for i in range(num_threads):
#     t = Thread(target=worker, args=(q,))
# t.daemon = True
# t.start()


#Реализация программы, которая создает 3 потока и каждый поток выводит свое имя 5 раз
# from threading import Thread
#
# def func(a: int):
#     for i in range(5):
#         print(f'It is {a} thread')
#
# t1 = Thread(target=func, args=(1,))
# t2 = Thread(target=func, args=(2,))
# t3 = Thread(target=func, args=(3,))
#
# threads = []
# threads.append(t1)
# threads.append(t2)
# threads.append(t3)
#
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()


