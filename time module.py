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
init=time.time()#this is recordng the current time

loop()#call the for loop

t1=time.time()-init#calculate the time to execute the for loop from the current time

init=time.time()#this is recording the current time

whileloop()#call the while loop

print(time.time()-init)# calculate and print the while loopfrom the current time

print(t1)#print the calcultation of the for loop from the current time