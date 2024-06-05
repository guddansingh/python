'''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Creating objects
rectangle = Rectangle(5, 10)
circle = Circle(7)

print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 50
print("Rectangle Perimeter:", rectangle.perimeter())  # Output: Rectangle Perimeter: 30

print("Circle Area:", circle.area())  # Output: Circle Area: 153.93791
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 43.98226'''
from abc import ABC, abstractmethod 
  
# Create Abstract base class 
class Car(ABC): 
  def __init__(self, brand, model, year): 
    self.brand = brand 
    self.model = model 
    self.year = year 
      
  # Create abstract method       
  @abstractmethod
  def printDetails(self): 
    pass
    
  # Create concrete method 
  def accelerate(self): 
    print("speed up ...") 
    
  def break_applied(self): 
    print("Car stop") 
      
# Create a child class 
class Hatchback(Car): 
    
  def printDetails(self): 
    print("Brand:", self.brand); 
    print("Model:", self.model); 
    print("Year:", self.year); 
    
  def Sunroof(self): 
    print("Not having this feature") 
      
# Create a child class 
class Suv(Car): 
    
  def printDetails(self): 
    print("Brand:", self.brand); 
    print("Model:", self.model); 
    print("Year:", self.year); 
    
  def Sunroof(self): 
    print("Available") 
  
      
car1 = Hatchback("Maruti", "Alto", "2022"); 
  
car1.printDetails() 
car1.accelerate() 
      
   
