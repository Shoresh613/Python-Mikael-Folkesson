from Common_supershape import Common_supershape
from typing import Union
import math
import matplotlib.patches as patches
from matplotlib.axes._axes import Axes

class Circle(Common_supershape):
    def __init__(self, x=0, y=0, radius=1) -> None:
        try:
            self.x = x
            self.y = y
            self.radius = radius
        except ValueError as ex:
            print(ex)

    def is_inside(self, x, y) -> bool:
        return True if (x - self.x)**2 + (y - self.y)**2 <= self.radius**2 else False 
    
    def is_unity_circle(self) -> bool:
        return True if self.x == 0 and self.y == 0 and self.radius == 1 else False

    def _check_operand_type(self, other) -> bool:
        if not isinstance(other, Circle):
           raise TypeError(f"Usupported operand type(s) for == 'Circle' and {type(other)}!")
        return True

    def draw(self, ax: Axes, label=True) -> None:
        circle = patches.Circle((self.x, self.y), self.radius, fill=False, color='blue')
        if label:
            ax.text(self.x, self.y if self.radius > 3 else (self.y + self.radius + 1.5), f'x:{self.x} y: {self.y} r:{self.radius}', ha='center', va='center', fontsize=8, color='blue')
        ax.add_patch(circle)

    # Dunder methods and operator overloads
    #######################################

    def __repr__(self) -> str:
        return f"Circle{self.x, self.y, self.radius}"
    
    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, radius: {self.radius}, circumference: {self.circumference}, area: {self.area}"
        
    def __eq__(self, other) -> bool:
        if self._check_operand_type(other):
            if(self.radius == other.radius):
                return True
            else:
                return False

    def __ne__(self, other) -> bool:
        if self._check_operand_type(other):
            if(self.radius == other.radius):
                return False
            else:
                return True

# Setters and getters beyond this point
#######################################

    @property
    def x(self) -> Union[int,float]:
        return self._x

    @x.setter
    def x(self, x):
        try:
            if self._is_value_ok(x):
                self._x = x
        except ValueError as ex:
            print(ex)

    @property
    def y(self) -> Union[int,float]:
        return self._y

    @y.setter
    def y(self, y):
        try:
            if self._is_value_ok(y):
                self._y = y
        except ValueError as ex:
            print(ex)

    @property
    def radius(self) -> Union[int,float]:
        return self._radius

    @radius.setter
    def radius(self, radius):
        try:
            if self._is_size_value_ok(radius):
                if radius > 0:
                    self._radius = radius
        except ValueError as ex:
            print(ex)

    @property
    def circumference(self) -> Union[int,float]:
        return 2*math.pi*self.radius
    
    @property
    def area(self) -> Union[int,float]:
        return math.pi*(self.radius**2)