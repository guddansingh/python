#inheritance class used to change the name of old class and give another body with same class
class students:
    """this is guddan i am using docstring in class"""
    def __init__(self,name,value):
        """this is the docstring """
        self.name=name
        self.value=value
    #@property
    def access(self):
        print(f"the name of first student {self.name}")
        print(f"the value of first student {self.value}")
    
    #here we want to change the name of class we may use this method
class employee(students):
    def new(self):
        print("this is an new class where the first class methos also exist and you may create another methods ahead with this name of class")

class employee1(employee):
    def __init__(self,value):
        self.value=value

#here we will call the objects
obj=students("guddan","1")
obj.access()
obj2=employee("akhil",2)
obj2.new()
print(obj.__doc__) #this is to access the docstring that is wrapped into triple quotes 
print(obj.__init__.__doc__)
obj3=employee1("1234")
obj3.new()

