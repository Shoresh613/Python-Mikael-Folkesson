from Common_supershape import Common_supershape
import math

class Circle(Common_supershape):
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.circumference = 2*math.pi*radius
        self.area = math.pi*(radius**2)

    def is_inside(self, x, y):
        return True if (x - self.x)**2 + (y - self.y)**2 < self.radius**2 else False 
    
    def is_unity_circle(self):
        return True if self.x == 0 and self.y == 0 and self.radius else False

    def __repr__(self) -> str:
        return f"Circle({self.x, self.y, self.radius})"
    
    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, radius: {self.radius}, circumference: {self.circumference}, area: {self.area}"