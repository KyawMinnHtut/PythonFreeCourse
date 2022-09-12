# Solving producer-consumer problem by Event object
from multiprocessing import Event
from random import randint
from threading import Thread
from time import sleep


items = []
event = Event()
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(10):
            item = randint(0, 256)
            items.append(item)
            print("Produce ", item)
            sleep(1)
            event.set() #produceတာကို eventထဲကို ထည့်လိုက်
            event.clear()   #produceမရရင် eventထဲမှာ ဘာမှ မရှိဘူးလို့ signalလုပ်
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(10):
            event.wait()    #eventထဲမှာ produceမရှိရင် စောင့်
            item = items.pop()
            print("Item consume ", item)

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()