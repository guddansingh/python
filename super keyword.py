#we will learn about the super method
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"this is the student name and the age of the student {self.name},{self.age}")

    def parent_method(self):
        print("this is the parent method")
    
class student_child(student):
    def __init__(self,name,age,father,mother):
        super().__init__(name,age)
        self.father=father
        self.mother=mother
    
    def show1(self):
        #print(f"this is the information for the student\n"
            #f"this is the name of candidate {self.name}\n"
            #f"this is the age of candidate {self.age}\n"
            #f"this is the age of candidat {self.age}\n"
            #f"this is the father's name of candidate {self.father}\n"
            #f"this is the mother's name of candidate{self.mother}")
        super().parent_method()

s=student_child("guddan",20,"kishnanpal","sunita")
s.show()
s.show1()
#s1=student("guddan gautam",21)

#s1.show()

