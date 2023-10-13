from geometry_shapes.Circle import Circle
from geometry_shapes.Rectangle import Rectangle
from geometry_shapes.Sphere import Sphere
from geometry_shapes.Cube import Cube
import matplotlib.pyplot as plt

my_rectangle = Rectangle()
my_new_rectangle = Rectangle()
my_circle = Circle()

print(f"{my_new_rectangle == my_rectangle = }")
print(f"{my_circle == my_rectangle = }")
print(f"{my_circle > my_rectangle = }")
print(f"{my_circle.area = }")
print(f"{my_rectangle.area = }")