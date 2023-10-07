from Common_supershape import Common_supershape
import math

class Circle(Common_supershape):
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
        self._circumference = 2*math.pi*radius
        self._area = math.pi*(radius**2)

    def is_inside(self, x, y):
        return True if (x - self.x)**2 + (y - self.y)**2 < self.radius**2 else False 
    
    def is_unity_circle(self):
        return True if self.x == 0 and self.y == 0 and self.radius else False

    def __repr__(self) -> str:
        return f"Circle({self.x, self.y, self.radius})"
    
    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, radius: {self.radius}, circumference: {self._circumference}, area: {self._area}"

# Setters and getters beyond this point
#######################################

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if self.is_value_ok(x):
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if self.is_value_ok(y):
            self._y = y

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if self.is_value_ok(radius):
            self._radius = radius