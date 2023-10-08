from Common_supershape import Common_supershape
import math
import matplotlib.patches as patches


class Circle(Common_supershape):
    def __init__(self, x=0, y=0, radius=1):
        try:
            self.x = x
            self.y = y
            self.radius = radius
        except ValueError as ex:
            print(ex)

    def is_inside(self, x, y):
        return True if (x - self.x)**2 + (y - self.y)**2 < self.radius**2 else False 
    
    def is_unity_circle(self):
        return True if self.x == 0 and self.y == 0 and self.radius else False

    def __repr__(self) -> str:
        return f"Circle{self.x, self.y, self.radius}"
    
    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, radius: {self.radius}, circumference: {self.circumference}, area: {self.area}"
    
    def draw(self, ax, label=True):
        # Plot a circle using Matplotlib
        circle = patches.Circle((self.x, self.y), self.radius, fill=False, color='blue')
        if label:
            ax.text(self.x, self.y if self.radius > 3 else (self.y + self.radius + 1.5), f'x:{self.x} y: {self.y} r:{self.radius}', ha='center', va='center', fontsize=8, color='blue')
        ax.add_patch(circle)


# Setters and getters beyond this point
#######################################

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        try:
            if self.is_value_ok(x):
                self._x = x
        except ValueError as ex:
            print(ex)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        try:
            if self.is_value_ok(y):
                self._y = y
        except ValueError as ex:
            print(ex)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        try:
            if self.is_size_value_ok(radius):
                if radius > 0:
                    self._radius = radius
        except ValueError as ex:
            print(ex)

    @property
    def circumference(self):
        return 2*math.pi*self.radius
    
    @property
    def area(self):
        return math.pi*(self.radius**2)