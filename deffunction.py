#this is an decorator function that will took the the another functuino in it to decortae the original function
def decorator(func):
    def greet(*args,**kwargs):
        print("good morning, in the below you will get an addition")
        func(*args,**kwargs)
        print("thanks you have done the addition succesfully\n")
    return greet

#here we will execute the original function
#@decorator
#def guddan():
 #   print("i love to explore this")
@decorator
def add():
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a+b)

#now we will call the function thorough using the @ sign with decorator function
#decorator(add)(20,40)
#guddan()
add()