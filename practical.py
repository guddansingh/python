#in tihs file we will learn about time module and figure out the complexity between for loop and while loop

import time
import os

#first we will create for loop
def loop():
    for i in range(5000):
        print(i)

#now we will create while loop
def whileloop():
    i=0
    while i<5000:
        i+=1
        print(i)
#here we will call the loops
init=time.time()
loop()
t1=time.time()-init
init=time.time()
whileloop()
print(time.time()-init)
print(t1)