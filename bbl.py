import time
import numpy as np
import math.plotlib.pyplot as plt
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if a[i]>a[j+1]:
                a[j],a[j+1]=[j+1],a[j]
                times=list()
                arr=list()
                numtimes=list()
for i in range(1,11):
    start=time.timetime()
    n=int(input("enter the number of element"))
    numtimes.append(n)
    arr.clear()
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(number)
print("list before sorting",x+1,"elements")
print(arr)
bubblesort(arr)
end=time.time()
times.append(end-start)
print("list after bubblesort of",x+1,"element")
print(arr)
print(numtimes)
print(times)

plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(numtimes,times,label="bubblesort")
plt.grid()
plt.legend()
plt.show()
