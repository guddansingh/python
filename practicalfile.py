#property method 
class subjects:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.total=(phy+chem+math)

    @property
    def change(self):
        return self.phy+self.chem+self.math


s=subjects(90,80,70)
print(s.total)
print("this is physics marks",s.phy,"this is maths marks",s.math,"this is chemistry marks",s.chem)
s.phy=85
print("this is physics marks",s.phy,"this is maths marks",s.math,"this is chemistry marks",s.chem)
print(s.change)