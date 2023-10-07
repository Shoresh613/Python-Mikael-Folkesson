from Circle import Circle
from Rectangle import Rectangle

my_circle = Circle()
my_circle.translate(5,5)

print(my_circle.x, my_circle.y)
print(my_circle.radius)
print(my_circle)

my_second_circle = Circle(2,3,5)
print()
print(my_second_circle)

my_rectangle = Rectangle()
my_rectangle.translate(-5,5)

print(my_rectangle)

print(my_second_circle.__repr__())
print(my_rectangle.__repr__())