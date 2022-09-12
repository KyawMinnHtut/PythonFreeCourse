from glob import glob
from multiprocessing import Condition, Event, Lock, RLock, Semaphore
import queue
from random import Random, randint, random
from threading import Thread
from time import sleep, time

# counter = 0
# lock = Lock()   #lock ကို ယူ
# def increment():
#     global counter
#     for i in range(0,20000):
#         lock.acquire()  #lockကို ခတ်   blockingလုပ်တာလို့လည်းခေါ်
#         counter += 1    #critical session
#         lock.release()  #lockကို ပြန်ဖွင် ပေး

# def decrement():
#     global counter
#     for i in range(0,20000):
#         lock.acquire()  #acuqireလုပ်ချင်ရင် ရှေ့က lock.release()ဖြစ်တာကို wait
#         counter -= 1
#         lock.release()

# threadA = Thread(target=increment)
# threadB = Thread(target=decrement)
# threadA.start()     #=> read counter, incre counter, write counter
# threadB.start()
# threadA.join()      #threadA ပီးအောင်  စောင့်မယ်
# threadB.join()      #threadB ပီးအောင်  စောင့်မယ်၊ ပီးမှ အောက်က codeတွေဆက်လုပ်မယ်

# print("Counter ==> ", counter)

# #Deak Lock
# lock =RLock()       #reentrant lock for same code/thread/recursive ရိုးရိုး Lock()ဆို dead lockဖြစ်စေ
# def factorial(n):
#     print("Try to get lock for ", n)
#     lock.acquire()
#     print("Get lock for ", n)
#     if n ==1:
#         return 1
#     else:
#         result = n * factorial(n-1)
#         lock.release()
#         return result
# print("Factorial ==> ", factorial(5))

# #Semaphore
# sem = Semaphore(2)
# def one(thre_name):
#     sem.acquire()
#     print("Get lock for ", thre_name)
#     for i in range(1,100):
#         print("Process ", thre_name, " ==> ", i)
#     print("Release lock for ", thre_name, " sem : ", sem)
#     sem.release()

# t1 = Thread(target=one, args=("one",))
# t2 = Thread(target=one, args=("two",))
# t3 = Thread(target=one, args=("three",))
# t1.start()
# t2.start()
# t3.start()

# Producer-Consumer Problem
# items = []
# class Producer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             item = randint(0, 256)
#             items.append(item)
#             print("Produce ", item)
#             sleep(1)
# class Consumer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             item = items.pop()  #IndexError: pop from empty list
#             print("Item consume ", item)
#             sleep(1)
# producer = Producer()
# consumer = Consumer()
# producer.start()
# consumer.start()

# #Solving producer-consumer problem by Event object
# items = []
# event = Event()
# class Producer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             item = randint(0, 256)
#             items.append(item)
#             print("Produce ", item)
#             sleep(1)
#             event.set() #produceတာကို eventထဲကို ထည့်လိုက်
#             event.clear()   #produceမရရင် eventထဲမှာ ဘာမှ မရှိဘူးလို့ signalလုပ်
# class Consumer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             event.wait()    #eventထဲမှာ produceမရှိရင် စောင့်
#             item = items.pop()
#             print("Item consume ", item)

# producer = Producer()
# consumer = Consumer()
# producer.start()
# consumer.start()

#Solving producer-consumer problem by Condition object
# items = []
# condition = Condition()
# class Producer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             sleep(1)
#             with condition:
#                 item = randint(0, 256)
#                 condition.acquire()
#                 items.append(item)
#                 print("Produce ", item)
#                 condition.notify()
#                 condition.release()
# class Consumer(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for i in range(10):
#             with condition:
#                 condition.acquire()
#                 condition.wait()
#                 item = items.pop()
#                 print("Item consume ", item)
#                 condition.release()

# producer = Producer()
# consumer = Consumer()

# consumer.start()
# producer.start()

#Solving producer-consumer problem by Queue object
items = queue.Queue()
#items = queue.LifoQueue()      #queueထဲ တန်းထည့် တန်းထုတ်မို့ ခုprogramမှာ မထူး
#items = queue.PriorityQueue()
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(10):
            item = randint(0, 256)
            items.put(item)
            print("Produce ", item)
            sleep(1)
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(10):
            item = items.get()
            print("Item consume ", item)

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
