from .Shape import Shape
from typing import Union
import matplotlib.patches as patches
from matplotlib.axes._axes import Axes

class Rectangle(Shape):
    """
    A class representing a rectangle in 2D space. Inherits from Shape.

    Attributes:
        x (int | float): The x-coordinate of the rectangle's center.
        y (int | float): The y-coordinate of the rectangle's center.
        side1 (int | float): The length of the first side of the rectangle.
        side2 (int | float): The length of the second side of the rectangle.
        circumference (int | float): The circumference of the rectangle.
        area (int | float): The area of the rectangle.
    Raises:
        TypeError if x, y, side1 or side2 are not (int | float)
        ValueError if side1 or side2 <= 0.
    """
    def __init__(self, x=0, y=0, side1=1, side2=1):
        """
        Initialize a Rectangle object.

        Args:
            x (int | float): The x-coordinate of the rectangle's center.
            y (int | float): The y-coordinate of the rectangle's center.
            side1 (int | float): The length of the first side of the rectangle.
            side2 (int | float): The length of the second side of the rectangle.
        """
        try:
            self.x = x
            self.y = y
            self.side1 = side1
            self.side2 = side2
        except ValueError as ex:
            raise(ex)
    
    def is_inside(self, x, y) -> bool:
        """
        Check if a point (x, y) is inside the rectangle.

        Args:
            x (int | float): The x-coordinate of the point to check.
            y (int | float): The y-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the rectangle, False otherwise.
        """
        if self.x - self.side1 / 2 <= x <= self.x + self.side1 / 2:
            if self.y - self.side2 / 2 <= y <= self.y + self.side2 / 2:
                return True
            else:
                return False
        else:
           return False 
    
    def is_square(self) -> bool:
        """
        Check if the rectangle is a square.

        Returns:
            bool: True if the rectangle is a square, False otherwise.
        """
        return True if self.side1 == self.side2 else False
    
    def draw(self, ax: Axes, label=True) -> None:
        """
        Draw the rectangle on a matplotlib Axes.

        Args:
            ax (Axes): The matplotlib Axes on which to draw the rectangle.
            label (bool, optional): Whether to label the rectangle with its coordinates and dimensions. Default is True.

        Returns:
            None
        """
        rectangle = patches.Rectangle((self.x, self.y), self.side1, self.side2, fill=False, color='red')
        y = self.y + self.side2/2 if self.side1 > 3 and self.side2 > 2 else (self.y - 1.5)
        
        if label:
            ax.text(self.x + self.side1/2, y, f'x:{self.x} y: {self.y}\nw:{self.side1} h:{self.side2}', 
                    ha='center', va='center', fontsize=8, color='red')
        ax.add_patch(rectangle)
    
    # Dunder methods and operator overloads
    #######################################

    def __repr__(self) -> str:
        """
        Get a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle.
        """
        return f"Rectangle({self.x, self.y, self.side1, self.side2})"

    def __str__(self) -> str:
        """
        Get a human-readable or more user friendly string representation 
        of the Rectangle object.

        Returns:
            str: A human-readable string representation of the Rectangle.
        """
        return super().__str__() + f": Center point: {self.x, self.y}, width: {self.side1}, height {self.side2}"
    
    def __eq__(self, other) -> bool:
        """
        Check if two Rectangle objects are equal.

        Args:
            other: The Rectangle object to compare to.

        Returns:
            bool: True if the sides of the two rectangles are equal, False otherwise.
        """
        try:
            if self._check_operand_type(self, other):
                if (self.side1 == other.side1) and (self.side2 == other.side2):
                    return True
                else:
                    return False
        except TypeError:
            return False
    def __ne__(self, other) -> bool:
        """
        Check if two Rectangle objects are not equal.

        Args:
            other: The Rectangle object to compare to.

        Returns:
            bool: True if the sides of the two rectangles are not equal, False otherwise.
        """
        try:
            if self._check_operand_type(self, other):
                if (self.side1 == other.side1) and (self.side2 == other.side2):
                    return False
                else:
                    return True
        except TypeError as ex:
            return True
        
    # Setters and getters beyond this point
    #######################################

    @property
    def x(self) -> Union[int, float]:
        return self._x

    @x.setter
    def x(self, x):
        try:
            if self._is_value_ok(x):
                self._x = x 
        except ValueError as ex:
            raise ValueError(ex)

    @property
    def y(self) -> Union[int, float]:
        return self._y

    @y.setter
    def y(self, y):
        try:
            if self._is_value_ok(y):
                self._y = y
        except ValueError as ex:
            raise ValueError(ex)

    @property
    def side1(self) -> Union[int, float]:
        return self._side1

    @side1.setter
    def side1(self, side1):
        try:
            if self._is_size_value_ok(side1):
                self._side1 = side1
        except ValueError as ex:
            raise ValueError(ex)

    @property
    def side2(self) -> Union[int, float]:
        return self._side2

    @side2.setter
    def side2(self, side2):
        try:
            if self._is_size_value_ok(side2):
                self._side2 = side2
        except ValueError as ex:
            raise ValueError(ex)

    @property
    def circumference(self) -> Union[int, float]:
        return 2 * self.side2 + 2 * self.side1
    
    @property
    def area(self) -> Union[int, float]:
        return self.side2 * self.side1