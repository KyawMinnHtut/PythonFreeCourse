# import pickle

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# with open("human.data", "wb") as file:
#     h = Human("Kyaw Min Htut", 30)
#     pickle.dump(h, file)        #write obj state to file
                    
# with open("human.data", "rb") as file:
#     h = pickle.load(file)          #read obj state from file
#     print(h.name, h.age)


#Multithreading
import threading
from threading import *

print("Current Thread : ", threading.current_thread().getName())

# def fun():
#     for i in range(1,40):
#         print("Child Thread ", i)
# thread = Thread(target=fun)      #threadတစ်ခု ခွဲထုတ်လိုက်
# thread.start()
# for i in range(1,40):
#     print("Main method ", i)

#creating thread with inheritance of Thread Class
# class MyThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):    
#         for i in range(1,50):
#             print("Thread ", self.name, " i ", i)            
#     # def fun(self):
#     #     for i in range(1,40):
#     #         print(self.name, i)

# threadA = MyThread("A")
# threadB = MyThread("B")
# threadA.start()
# threadB.start()

# objA = MyThread("Fun1")
# objB = MyThread("Fun2")
# fun_thread_one = Thread(target=objA.fun)
# fun_thread_two = Thread(target=objB.fun)
# fun_thread_one.start()
# fun_thread_two.start()

#thread scheduling
import time
def double(n):
    for i in range(n):
        print("Double value => ", i*2)
        time.sleep(1)
def square(n):
    for i in range(n):
        print("Square value => ", i*i)
        time.sleep(1)

start_time = time.time()
threadA = Thread(target=double, args=(10,))
threadB = Thread(target=square, args=(10,))
threadA.start()
threadB.start()
threadA.join()      #threadA ပီးအောင်  စောင့်မယ်
threadB.join()      #threadB ပီးအောင်  စောင့်မယ်၊ ပီးမှ အောက်က codeတွေဆက်လုပ်မယ်
end_time = time.time()
print("Total time ==> ", end_time-start_time)

#Set thread name
threading.current_thread().name = "My Main Thread"  #set thread name
print("Current thread => ", threading.current_thread().name)    #get thread name
print("Current thread Id => ", threading.current_thread().ident)    #get thread id
print("Current active thread count => ", active_count())        #current running number of thread counts
print("Current thread is alive? => ", threading.current_thread().is_alive())    #check thread is alive or not
print("Current thread is daemon? => ", threading.current_thread().daemon)   #can run in the background