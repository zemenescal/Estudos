
'''
num = [2, 5, 9, 11]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 2)
print(num)
if 5 in num:
    num.remove(5)
else:
    print("Não achei este número")
# print(num)
print((num),f" <- Esta lista tem {len(num)} elementos.")
'''


'''
valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)
# for v in valores:
# print(f" {v} ...", end="")

for cont in range(0,6):
    valores.append(int(input("Digite um número: ")))
for c, v in enumerate(valores):
    print(f"Encontrei {v} na posição {c}")
print("Cheguei ao final da lista")
'''



import numpy as np

for i in range(1, 10):
    j = np.arange(1, 10)

    for idx, ans in enumerate(i * j):
        if idx != 8:
            print(f'{ans:02d}  ', end='')
        else:
            print(f'{ans:02d}  ')

        if idx == 0:
            print('|', end='')

    if i == 1:
        print('{}'.format('-' * (4 * 9)))


'''

# Taken from the matplotlib examples gallery: https://matplotlib.org/gallery/ (full url below)
# https://matplotlib.org/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-pym
# https://matplotlib.org/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
axs[0].set_title('The coherence of two signals')

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('coherence')

# fig.tight_layout()
plt.show() 
'''

'''
# print(Este é um parágrafo e pode
# ser feito em muitas linhas,
# bastando colocar as 3 aspas
'''
'''
def printme(str):
    print(str)
    return


printme(str="My String")
'''
'''
def printinfo(name, age):
    print('Name:', name)
    print('Age:', age)
    return


printinfo(name='miki', age=50)
printinfo(age=35, name='chico')
printinfo(age=110, name='Ana')
'''
'''
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        self.threadID = threadID
        self.name = name
        self.counter = counter
        threading.Thread.__init__(self)

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1


# Create new Threads

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads

thread1.start()
thread2.run()

while thread2.isAlive():
    if not thread1.isAlive():
        exitFlag = 1
pass
print("Exiting Main Thread")
'''
'''
# Using thread
import _thread


#
# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# # Create two threads
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error:unable to start thread")

while 1:
    pass

# Using threading
import threading
import time

#
exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting", self.name)
        print_me(self.name, 5, self.counter)
        print("Exiting", self.name)


def print_me(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# #Create two threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()
#
print("Exiting Main thread")

import threading


class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number

    def run(self):
        counter = 2
        while counter * counter < self.Number:
            if self.Number % counter == 0:
                print("%d is not a prime number, because %d = %d * %d" % (
                    self.Number, self.Number, counter, self.Number / counter))
                return
            counter += 1
            print("%d is a prime number" % self.Number)


#
threads = []
while True:
    input_var = int(input("number: "))
    if input_var < 1:
        break
    thread = PrimeNumber(input_var)
    threads += [thread]
    print(threads)
    thread.start()
#
for x in threads:
    x.join()

# Synchronizing threads while using critical section
import threading


#
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting" + self.name)
        # Get lock to synchronize thread
        threadLock.acquire()
        print_me(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()


def print_me(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []
#
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
#
thread1.start()
thread2.start()
#
threads.append(thread1)
threads.append(thread2)
#
for t in threads:
    t.join()
#
print("Exiting main thread")

# Determining name of current thread
import threading


#
def worker():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(2)
    print(threading.currentThread().getName(), "Exiting")


#
def my_service():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(3)
    print(threading.currentThread().getName(), "Exiting")


#
t = threading.Thread(name="my_service", target=my_service)
w = threading.Thread(name="worker", target=worker)
w2 = threading.Thread(target=worker)
#
#
t.start()
w.start()
w2.start()

# Q1
import time
import threading
from threading import Thread


#
def sleepMe():
    print("Thread is sleeping", threading.currentThread().getName())
    time.sleep(5)
    print("Thread is awake", threading.currentThread().getName())


#
t = Thread(target=sleepMe, args=())
t.start()
'''