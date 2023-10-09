from Circle import Circle
from Rectangle import Rectangle
import matplotlib.pyplot as plt

my_circle = Circle()
my_circle.translate(5,5)
my_circle.radius=2

print(my_circle.x, my_circle.y)
print(my_circle.radius)
print(my_circle)

my_second_circle = Circle(2,3,5)
print()
print(my_second_circle)

my_rectangle = Rectangle(1,3,6,3)
my_rectangle.translate(-5,5)

print(my_rectangle)

print(my_second_circle.__repr__())
print(my_rectangle.__repr__())

print(my_rectangle)
print(f"{my_rectangle.is_inside(-4,6.4) = }")
print()
print(my_circle)
print(f"{my_circle.is_inside(5.8,5.8) = }")

rec = Rectangle(0,0,5,5)
cir = Circle(0,0,0)

print(my_circle==my_second_circle)

# Create a figure and axis
fig, ax = plt.subplots()
my_circle.draw(ax)
my_rectangle.draw(ax)
rec.draw(ax,False)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='gray')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()