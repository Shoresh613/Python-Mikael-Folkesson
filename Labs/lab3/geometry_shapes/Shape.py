class Shape:
    """
    A common base class for various 2D and 3D geometric shapes.

    Methods:
        translate(x: (int | float), y: (int | float), *args: (int | float)) -> None: Translate the shape's position.
        is_inside(x: (int | float), y: (int | float)) -> bool: Check if a point is inside the shape.
        draw() -> None: Draw the shape.
        _is_value_ok(value: (int | float)) -> bool: Check if a value is an integer or a float.
        _is_size_value_ok(value: (int | float)) -> bool: Check if a value is a positive integer or float (>0).
    """
    def __init__(self) -> None:
        pass

    def translate(self, x, y, *args):
        """
        Translate the shape's position, i.e. move the object.

        Args:
            x (int | float): The x-translation.
            y (int | float): The y-translation.
            *args: Optional z-translation for 3D objects.

        Returns:
            None
        """
        self.x = self.x + x
        self.y = self.y + y        
        if len(args) == 1:
            self.z = self.z + args[0]

    def _is_value_ok(self, value):
        """
        Check if a value is an integer or a float, to see if it is a valid coordinate.

        Args:
            value (int | float): The value to check.

        Returns:
            bool: True if the value is an integer or a float, False otherwise.
        """
        if type(value) == int or type(value) == float:
            return True
        else:
            raise ValueError(f"Value '{value}' must be an integer or a float entered as (a) digit(s).")

    def _is_size_value_ok(self, value):
        """
        Check if a value is a positive integer or float (>0), to see if it is a valid spacial extension.

        Args:
            value (int | float): The value to check.

        Returns:
            bool: True if the value is a positive integer or float (>0) entered as (a) digit(s), False otherwise.
        """
        if (type(value) == int or type(value) == float) and value > 0:
            return True
        else:
            raise ValueError(f"Value '{value}' must be a positive integer or float (>0) entered as (a) digit(s).")

    def _check_operand_type(self, calling, other) -> bool:
        """
        Check if the operand type is valid for comparison.

        Args:
            other: The object to compare.

        Returns:
            bool: True if the operand type is valid, raises TypeError otherwise.
        """
        if not isinstance(other, calling):
           raise TypeError(f"Unsupported operand type(s) for == '{type(calling)}' and {type(other)}!")
        return True

    # Comparison operator overloads
    ###############################

    def __gt__(self, other):
        """
        Check if the area of the current shape is greater than the area of another shape.

        Args:
            other: The other shape to compare to.

        Returns:
            bool: True if the current shape's area is greater, False otherwise.
        """
        if not isinstance(other, Shape):
            raise TypeError(f"Unsupported operand type(s) for > 'Shape' and {type(other)}!")
        return self.area > other.area

    def __lt__(self, other):
        """
        Check if the area of the current shape is less than the area of another shape.

        Args:
            other: The other shape to compare to.

        Returns:
            bool: True if the current shape's area is less, False otherwise.
        """
        if not isinstance(other, Shape):
            raise TypeError(f"Unsupported operand type(s) for > 'Shape' and {type(other)}!")
        return self.area < other.area

    def __ge__(self, other):
        """
        Check if the area of the current shape is greater than or equal to the area of another shape.

        Args:
            other: The other shape to compare to.

        Returns:
            bool: True if the current shape's area is greater than or equal, False otherwise.
        """
        if not isinstance(other, Shape):
            raise TypeError(f"Unsupported operand type(s) for > 'Shape' and {type(other)}!")
        return self.area >= other.area

    def __le__(self, other):
        """
        Check if the area of the current shape is less than or equal to the area of another shape.

        Args:
            other: The other shape to compare to.

        Returns:
            bool: True if the current shape's area is less than or equal, False otherwise.
        """
        if not isinstance(other, Shape):
            raise TypeError(f"Unsupported operand type(s) for > 'Shape' and {type(other)}!")
        return self.area <= other.area