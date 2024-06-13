#overloading
class complex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"{self.x}x + {self.y}y"

    def __add__(self,other):
        return complex(self.x + other.x , self.y +other.y)
    
c=complex(2,3)
print(c)
c1=complex(4,5)
print(c1)
c3=c+c1
print(c3)