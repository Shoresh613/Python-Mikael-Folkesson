from .Shape import Shape
from typing import Union
import math
import matplotlib.patches as patches
from matplotlib.axes._axes import Axes

class Circle(Shape):
    """
    A class representing a circle in 2D space. Inherits from Shape.

    Attributes:
        x (int | float): The x-coordinate of the circle's center.
        y (int | float): The y-coordinate of the circle's center.
        radius (int | float): The radius of the circle.
        circumference (int | float): The circumference of the circle.
        area (int | float): The area of the circle.
    Raises:
        TypeError if x, y or radius are not (int | float)
        ValueError if radius <= 0.
    """
    def __init__(self, x=0, y=0, radius=1) -> None:
        """
        Initialize a Circle object.

        Args:
            x (int | float): The x-coordinate of the circle's center.
            y ([int  float]): The y-coordinate of the circle's center.
            radius (int | float): The radius of the circle, positive and > 0.
        """
        try:
            self.x = x
            self.y = y
            self.radius = radius
        except ValueError as ex:
            raise(ex)

    def is_inside(self, x, y) -> bool:
        """
        Check if a point (x, y) is inside the circle.

        Args:
            x (int | float): The x-coordinate of the point to check.
            y (int | float): The y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the circle, False otherwise.
        """
        return True if (x - self.x)**2 + (y - self.y)**2 <= self.radius**2 else False

    def is_unity_circle(self) -> bool:
        """
        Check if the circle is a unity circle with center at (0, 0) and radius 1.
        Arguably the method should return True regardless of where the center is at,
        but now it works according to the instructions. 

        Returns:
            bool: True if the circle is a unity circle, False otherwise.
        """
        return True if self.x == 0 and self.y == 0 and self.radius == 1 else False

    def draw(self, ax: Axes, label=True) -> None:
        """
        Draw the circle on a matplotlib Axes.

        Args:
            ax (Axes): The matplotlib Axes on which to draw the circle.
            label (bool, optional): Whether to label the circle with its coordinates and radius. Default is True.

        Returns:
            None
        """
        circle = patches.Circle((self.x, self.y), self.radius, fill=False, color='blue')
        if label:
            ax.text(self.x, self.y if self.radius > 3 else (self.y + self.radius + 1.5), f'x:{self.x} y: {self.y} r:{self.radius}', ha='center', va='center', fontsize=8, color='blue')
        ax.add_patch(circle)

    # Dunder methods and operator overloads
    #######################################

    def __repr__(self) -> str:
        """
        Get a string representation of the Circle object.

        Returns:
            str: A string representation of the Circle.
        """
        return f"Circle{self.x, self.y, self.radius}"
    
    def __str__(self) -> str:
        """
        Get a human-readable or more user friendly string representation of the Circle object.

        Returns:
            str: A human-readable string representation of the Circle.
        """
        return super().__str__() + f": Center point: {self.x, self.y}, radius: {self.radius}, circumference: {self.circumference}, area: {self.area}"
        
    def __eq__(self, other) -> bool:
        """
        Check if two Circle objects are equal.

        Args:
            other: The Circle object to compare to.

        Returns:
            bool: True if the radii of the two circles are equal, False otherwise.
        """
        try:
            if self._check_operand_type(self,other):
                if(self.radius == other.radius):
                    return True
                else:
                    return False
        except TypeError:
            return False

    def __ne__(self, other) -> bool:
        """
        Check if two Circle objects are not equal.

        Args:
            other: The Circle object to compare to.

        Returns:
            bool: True if the radii of the two circles are not equal, False otherwise.
        """
        try:
            if self._check_operand_type(self, other):
                if(self.radius == other.radius):
                    return False
                else:
                    return True
            else:
                return False
        except TypeError as ex:
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
            raise ValueError(ex)

    @property
    def y(self) -> Union[int,float]:
        return self._y

    @y.setter
    def y(self, y):
        try:
            if self._is_value_ok(y):
                self._y = y
        except ValueError as ex:
            raise ValueError(ex)

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
            raise ValueError(ex)

    @property
    def circumference(self) -> Union[int,float]:
        return 2 * math.pi * self._radius
    
    @property
    def area(self) -> Union[int,float]:
        return math.pi * (self._radius**2)