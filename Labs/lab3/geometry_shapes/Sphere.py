from .Shape import Shape
from typing import Union
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

class Sphere(Shape):
    """
    A class representing a 3D sphere. Inherits from Shape.

    Attributes:
        x (int | float): The x-coordinate of the sphere's center.
        y (int | float): The y-coordinate of the sphere's center.
        z (int | float): The z-coordinate of the sphere's center.
        radius (int | float): The radius of the sphere.
    """
    def __init__(self, x=0, y=0, z=0, radius=1):
        try:
            self.x = x
            self.y = y
            self.z = z
            self.radius = radius
        except ValueError as ex:
            print(ex)

    # Asked ChatGPT for the formula to check whether a point is inside a sphere
    def is_inside(self, x, y, z) -> bool:
        """
        Check if a point is inside the sphere.

        Args:
            x (int | float): The x-coordinate of the point.
            y (int | float): The y-coordinate of the point.
            z (int | float): The z-coordinate of the point.

        Returns:
            bool: True if the point is inside the sphere, False otherwise.
        """
        return True if math.sqrt(sum((p - c) ** 2 for p, c in zip((x,y,z), (self.x,self.y,self.z)))) <= self.radius**2 else False 
    
    def is_unity_sphere(self) -> bool:
        """
        Check if the sphere is a unity sphere.

        Returns:
            bool: True if the sphere is a unity sphere, False otherwise.
        """
        return True if self.x == 0 and self.y == 0 and self.z == 0 and self.radius == 1 else False

    def draw(self, ax3D:Axes3D, label=True) -> None:
        """
        Draw the 3D sphere on a given Axes3D.

        Args:
            ax3D (Axes3D): The 3D axes on which to draw the sphere.
            label (bool): Whether to label the sphere (not implemented).

        Returns:
            None
        """
        # Sphere parameters
        center = (self.x, self.y, self.z)
        radius = self.radius

        # Create a sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
        y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
        z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))

        # Plot the sphere
        ax3D.plot_surface(x, y, z, color='b', alpha=0.5)

    # Dunder methods and operator overloads
    #######################################

    def __repr__(self) -> str:
        return f"Sphere{self.x, self.y, self.z, self.radius}"
    
    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y,self.z}, radius: {self.radius}, circumference: {self.circumference}, area: {self.area}"
        
    def __eq__(self, other)  -> bool:
        """
        Check if two spheres are of equal size.

        Args:
            other: The object to compare.

        Returns:
            bool: True if the spheres are equal, False otherwise.
        """
        try:
            if self._check_operand_type(self, other):
                if(self.radius == other.radius):
                    return True
                else:
                    return False
        except TypeError as ex:
            print(ex)
            return False

    def __ne__(self, other)  -> bool:
        """
        Check if two spheres are not of equal size.

        Args:
            other: The object to compare.

        Returns:
            bool: True if the spheres are not equal, False otherwise.
        """
        try:
            if self._check_operand_type(self, other):
                if(self.radius != other.radius):
                    return True
                else:
                    return False
        except TypeError as ex:
            print(ex)
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
    def z(self) -> Union[int,float]:
        return self._z

    @z.setter
    def z(self, z):
        try:
            if self._is_value_ok(z):
                self._z = z
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
    def circumference(self) -> float:
        return 2*math.pi*self.radius
    
    @property
    def area(self) -> float:
        return  4*math.pi*self.radius**2
    
    @property
    def volume(self) -> float:
        return  (4/3) * math.pi * self.radius**3
