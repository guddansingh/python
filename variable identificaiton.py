#what are private and public variable 
class variables:
    def __init__(self,first,second):
        self.first=first
        self.__second=second

    #next function to understand the variables whom can access or whom not
    def access(self):
        print("this is the public variable",self.first)
        print("this is the private variable",self.__second)
    
    #here we will create objects to call them
    
run=variables("public","private")
print(run.access())
print(run.first)
print(run.__second)