#here we ewatvh the example of overriding
class shape1:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid

    def area(self):
        return self.len * self.wid

class shape2(shape1):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(self.radius,self.radius)
    
    def area(self):
        return 3.14159 * super().area()
    

s1=shape1(2,3)
print(f"the area of the rectanlge",s1.area())
s2=shape2(5)
print(f"the area of the",s2.area())