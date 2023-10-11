from Common_supershape import Common_supershape
from typing import Union
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Cube(Common_supershape):
    def __init__(self, x=0, y=0,  z=0, width=1, height=1, depth=1):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
    
    def is_inside(self, x, y, z) -> bool:
        half_width, half_height, half_depth = self.width / 2, self.height / 2, self.depth / 2

        x_in_range = self.x - half_width <= x <= self.x + half_width
        y_in_range = self.y - half_height <= y <= self.y + half_height
        z_in_range = self.z - half_depth <= z <= self.z + half_depth

        return x_in_range and y_in_range and z_in_range
        
    def is_square(self) -> bool:
        return True if self.width == self.height == self.depth else False

    def is_unity_cube(self) -> bool:
        return True if self.x == 0 and self.y == 0 and self.z == 0 and self.width == 1 and self.height == 1 and self.width == 1 else False
    
    def _check_operand_type(self, other) -> bool:
        if not isinstance(other, Cube):
           raise TypeError(f"Usupported operand type(s) for == 'Cube' and {type(other)}!")
        return True

    def draw(self, ax3D: Axes3D, label=True) -> None:
        # Asked ChatGPT how to adapt the sphere drawing method to a cube drawing method
        center = (self.x, self.y, self.z)
        width = self.width
        height = self.height
        depth = self.depth

        # Define the 8 vertices of the cube
        vertices = [
            (center[0] - width / 2, center[1] - height / 2, center[2] - depth / 2),
            (center[0] + width / 2, center[1] - height / 2, center[2] - depth / 2),
            (center[0] - width / 2, center[1] + height / 2, center[2] - depth / 2),
            (center[0] + width / 2, center[1] + height / 2, center[2] - depth / 2),
            (center[0] - width / 2, center[1] - height / 2, center[2] + depth / 2),
            (center[0] + width / 2, center[1] - height / 2, center[2] + depth / 2),
            (center[0] - width / 2, center[1] + height / 2, center[2] + depth / 2),
            (center[0] + width / 2, center[1] + height / 2, center[2] + depth / 2)
        ]

        # Define the vertices' indices that form the cube's faces
        faces = [
            [0, 1, 3, 2],
            [4, 5, 7, 6],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [0, 2, 6, 4],
            [1, 3, 7, 5]
        ]

        # Plot the cube's faces
        for face in faces:
            x = [vertices[i][0] for i in face]
            y = [vertices[i][1] for i in face]
            z = [vertices[i][2] for i in face]
            ax3D.add_collection3d(Poly3DCollection([list(zip(x, y, z))], alpha=0.5, color='r'))
                                      
    # Dunder methods and operator overloads
    #######################################

    def __repr__(self) -> str:
        return f"Cube({self.x, self.y, self.side1, self.side2})"

    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, width: {self.side1}, height {self.side2}"
    
    def __eq__(self, other) -> bool:
        if self._check_operand_type(other):
            if((self.side1 == other.side1) and (self.side2 == other.side2)):
                return True
            else:
                return False

    def __ne__(self, other) -> bool:
         if self._check_operand_type(other):
            if((self.side1 == other.side1) and (self.side2 == other.side2)):
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
    def z(self) -> Union[int,float]:
        return self._z

    @z.setter
    def z(self, z):
        try:
            if self._is_value_ok(z):
                self._z = z
        except ValueError as ex:
            print(ex)

    @property
    def width(self) -> Union[int,float]:
        return self._width

    @width.setter
    def width(self, width):
        try:
            if self._is_value_ok(width):
                self._width = width
        except ValueError as ex:
            print(ex)

    @property
    def height(self) -> Union[int,float]:
        return self._height

    @height.setter
    def height(self, height):
        try:
            if self._is_value_ok(height):
                self._height = height
        except ValueError as ex:
            print(ex)

    @property
    def depth(self) -> Union[int,float]:
        return self._width

    @depth.setter
    def depth(self, depth):
        try:
            if self._is_value_ok(depth):
                self._width = depth
        except ValueError as ex:
            print(ex)


    @property
    def circumference(self) -> Union[int,float]:
        return 2*self.side2 + 2*self.side1
    
    @property
    def area(self) -> Union[int,float]:
        return self.side2 * self.side1