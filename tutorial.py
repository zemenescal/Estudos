'''

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
     self.threadID = threadID
     self.name = name
     self.counter = counter
     threading.Thread.__init__(self)
   def run(self):
     print ("Starting " + self.name)
     print_time(self.name, self.counter, 5)
     print ("Exiting " + self.name)
def print_time(threadName, delay, counter):
   while counter:
     if exitFlag:
       thread.exit()
       time.sleep(delay)
       print( "%s: %s" % (threadName, time.ctime(time.time())))
       counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.run()

while thread2.isAlive():
   if not thread1.isAlive():
     exitFlag = 1
   pass
print ("Exiting Main Thread") '''
"""
import datetime
import calendar

cal = calendar.month(2022, 4)
print("Here is the calendar:")
print(cal)
print(calendar.weekday(2022, 4, 25))
print(datetime.date.today())
"""
"""
import matplotlib.pyplot as plt
from math import pi, sin, cos, tan

x = [0, 1, 2, 3, 4, 5, 6]
y = []
for n in range(0, 7):
    # print(f'{x[n]} ', end="")
    y.append((x[n] ** 2 + 3))
    """
"""
#plt.plot(x, y, 'b')
# plt.show()
#plt.plot(x, y, label='Dados')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.title('Novo Gráfico')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
plt.plot(x, y, 'b', label='Curva de crescimento', linestyle='-', lw='2')
plt.legend()
plt.show()
"""
"""
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
axes[0, 0].set(title='Upper left')
axes[0, 1].set(title='Upper right')
axes[1, 0].set(title='Lower left')
axes[1, 1].set(title='Lower right')
plt.show()
"""
"""
import matplotlib.pyplot as plt

x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y1 = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]
y2 = [35, 52, 96, 77, 36, 66, 50, 12, 35, 63]
plt.plot(x, y1, 'bo-')
plt.plot(x, y2, 'ro-')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend('AB')
plt.show()

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.normal(size=30), index=pd.date_range(start='1/1/2023', periods=30))
ts.plot()  # funciona para plotagem com plt.show()
# plt.plot(ts)
plt.grid(True)
plt.show()
