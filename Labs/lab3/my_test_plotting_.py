from geometry_shapes.Circle import Circle
from geometry_shapes.Rectangle import Rectangle
from geometry_shapes.Sphere import Sphere
from geometry_shapes.Cube import Cube
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

print(f"{my_circle == my_rectangle}")

# my_circle.translate("TRE",5)

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

# 3D plotting
##############

fig3D = plt.figure()
ax3D = fig3D.add_subplot(111, projection='3d')

my_sphere = Sphere(0,0,0,2)
my_sphere.draw(ax3D)
my_second_sphere = Sphere(10,10,10,5)
my_second_sphere.draw(ax3D)
my_cube = Cube(-10,-10, -10,8,8,8)
my_cube.draw(ax3D)
my_sphere.radius=5
my_sphere.translate(-5,-5, 2)
my_sphere.draw(ax3D)
print(my_sphere.radius)
print(my_sphere)

# Set axis limits to ensure correct scaling
ax3D.set_xlim(-20, +20)
ax3D.set_ylim(-20, +20)
ax3D.set_zlim(-20, +20)

ax3D.set_box_aspect([1,1,1])
plt.show()

print(f"\nSPHERE:\n{my_sphere.is_inside(-5,-2, 0) =}")
print(f"\n{my_sphere.is_unity_sphere() =}\n")
print(f"{my_rectangle==rec =}")

# 2D plotting: Create a figure and axis
#######################################

fig, ax = plt.subplots()
my_circle.draw(ax)
my_rectangle.draw(ax)
rec.draw(ax,False)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='gray')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()