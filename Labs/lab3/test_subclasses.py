import pytest
from geometry_shapes.Circle import Circle
from geometry_shapes.Sphere import Sphere
from geometry_shapes.Rectangle import Rectangle
from geometry_shapes.Cube import Cube
import math

# Fixtures to create instances of the classes
@pytest.fixture
def circle():
    return Circle(x=0, y=0, radius=2)

@pytest.fixture
def sphere():
    return Sphere(x=0, y=0, z=0, radius=2)

@pytest.fixture
def rectangle():
    return Rectangle(x=0, y=0, side1=2, side2=3)

@pytest.fixture
def cube():
    return Cube(x=0, y=0, z=0, width=2, height=3, depth=4)

# Tests for the Circle class
def test_circle_area(circle):
    assert circle.area == 12.566370614359172

def test_circle_circumference(circle):
    assert circle.circumference == 12.566370614359172

def test_circle_is_inside(circle):
    assert circle.is_inside(1.0, 1.0)
    assert not circle.is_inside(3.0, 3.0)

def test_circle_is_unity_circle():
    circle = Circle()
    assert circle.is_unity_circle() is True

def test_circle_constructor():
    circle = Circle(x=1, y=2, radius=3)
    assert circle.x == 1
    assert circle.y == 2
    assert circle.radius == 3

def test_circle_is_not_inside(circle):
    assert circle.is_inside(6, 7) is False

def test_circle_gt(circle):
    circle1 = Circle(radius=2)
    circle2 = Circle(radius=3)
    assert (circle1 > circle2) is False

def test_circle_lt(circle):
    circle1 = Circle(radius=2)
    circle2 = Circle(radius=3)
    assert (circle1 < circle2) is True

def test_circle_large_radius(circle):
    circle_large = Circle(radius=1e6)
    assert math.isclose(circle_large.area, 3.141592653589793238e12, rel_tol=0.01)
    assert math.isclose(circle_large.circumference, 6.283185307179586476e6, rel_tol=0.01)

def test_circle_radius_zero(circle):
    with pytest.raises(ValueError):
        circle_zero = Circle(radius=0)

def test_circle_negative_coordinates():
    circle_neg = Circle(x=-1, y=-2, radius=3)  # Negative coordinates
    assert circle_neg.x == -1
    assert circle_neg.y == -2
    assert circle_neg.is_inside(-1, -2) is True

def test_circle_negative_radius():
    with pytest.raises(ValueError):
        circle_neg_radius = Circle(radius=-3)

def test_circle_compare_sizes(circle):
    circle1 = Circle(radius=2)
    circle2 = Circle(radius=3)
    circle3 = Circle(radius=2)
    assert (circle1 > circle2) is False
    assert (circle1 < circle2) is True
    assert (circle1 == circle3) is True

def test_circle_assign_new_values(circle):
    # Test assigning new values for x, y, and radius
    circle.x = 1
    circle.y = 2
    circle.radius = 3
    assert circle.x == 1
    assert circle.y == 2
    assert circle.radius == 3

    # Test assigning negative radius (boundary condition)
    with pytest.raises(ValueError):
        circle.radius = -1

    # Test assigning a large radius (boundary condition)
    circle.radius = 1e6
    assert circle.area == pytest.approx(3.141592653589793238e12, rel=1e-2)

# Tests for the Sphere class
def test_sphere_volume(sphere):
    assert sphere.volume == 33.510321638291124

def test_sphere_is_inside(sphere):
    assert sphere.is_inside(1.0, 1.0, 1.0)
    assert not sphere.is_inside(3.0, 3.0, 3.0)

def test_sphere_is_unity_sphere():
    sphere = Sphere()
    assert sphere.is_unity_sphere() is True

def test_sphere_large_radius():
    sphere = Sphere(radius=1e6)
    assert sphere.volume == pytest.approx(4.1887902047863905e18, rel=1e-2)

def test_sphere_zero_radius():
    with pytest.raises(ValueError):
        sphere = Sphere(radius=0)

def test_sphere_negative_coordinates():
    sphere = Sphere(x=-1, y=-2, z=-3, radius=4)
    assert sphere.volume == pytest.approx(268.082573106329, rel=1e-2)
    assert sphere.y == -2

def test_sphere_negative_radius():
    with pytest.raises(ValueError):
        sphere = Sphere(radius=-4)

def test_sphere_greater_than_less_than():
    sphere1 = Sphere(radius=2)
    sphere2 = Sphere(radius=3)
    assert (sphere1 > sphere2) is False
    assert (sphere1 < sphere2) is True

def test_sphere_constructor():
    sphere = Sphere(x=1, y=2, z=3, radius=4)
    assert sphere.x == 1
    assert sphere.y == 2
    assert sphere.z == 3
    assert sphere.radius == 4

def test_sphere_assign_new_values(sphere):
    # Test assigning new values for x, y, z, and radius
    sphere.x = 1
    sphere.y = 2
    sphere.z = 3
    sphere.radius = 4
    assert sphere.x == 1
    assert sphere.y == 2
    assert sphere.z == 3
    assert sphere.radius == 4

    # Test assigning negative radius (boundary condition)
    with pytest.raises(ValueError):
        sphere.radius = -1

    # Test assigning a large radius (boundary condition)
    sphere.radius = 1e6
    assert sphere.volume == pytest.approx(4.1887902047863905e18, rel=1e-2)

# Tests for the Rectangle class
def test_rectangle_area(rectangle):
    assert rectangle.area == 6.0

def test_rectangle_circumference(rectangle):
    assert rectangle.circumference == 10.0

def test_rectangle_is_inside(rectangle):
    assert rectangle.is_inside(1.0, 1.5)
    assert not rectangle.is_inside(3.0, 3.5)

def test_rectangle_is_square():
    square = Rectangle(x=0, y=0, side1=2, side2=2)
    rectangle = Rectangle(x=0, y=0, side1=2, side2=3)
    assert square.is_square() is True
    assert rectangle.is_square() is False

def test_rectangle_constructor():
    rectangle = Rectangle(x=1, y=2, side1=3, side2=4)
    assert rectangle.x == 1
    assert rectangle.y == 2
    assert rectangle.side1 == 3
    assert rectangle.side2 == 4

def test_rectangle_equal_sides():
    square = Rectangle(side1=2, side2=2)
    assert square.is_square() is True

def test_rectangle_unequal_sides():
    rectangle = Rectangle(side1=2, side2=3)
    assert rectangle.is_square() is False

def test_rectangle_zero_sides():
    with pytest.raises(ValueError):
        rectangle = Rectangle(side1=0, side2=0)

def test_rectangle_negative_coordinates():
    rectangle = Rectangle(x=-1, y=-2, side1=2, side2=3)
    assert(rectangle.x == -1)
    assert(rectangle.y == -2)

def test_rectangle_negative_sides():
    with pytest.raises(ValueError):
        rectangle = Rectangle(side1=-2, side2=-3)

def test_rectangle_greater_than_less_than():
    rectangle1 = Rectangle(side1=2, side2=2)
    rectangle2 = Rectangle(side1=2, side2=3)
    assert (rectangle1 > rectangle2) is False
    assert (rectangle1 < rectangle2) is True

def test_rectangle_assign_new_values(rectangle):
    rectangle.x = 1
    rectangle.y = 2
    rectangle.side1 = 3
    rectangle.side2 = 4
    assert rectangle.x == 1
    assert rectangle.y == 2
    assert rectangle.side1 == 3
    assert rectangle.side2 == 4

    # Test assigning negative side lengths (boundary condition)
    with pytest.raises(ValueError):
        rectangle.side1 = -1

    # Test assigning a large side length (boundary condition)
    rectangle.side1 = 1e6
    assert rectangle.area == pytest.approx(4.0e6, rel=1e-2)


# Tests for the Cube class
def test_cube_volume(cube):
    assert cube.volume == 24.0

def test_cube_is_inside(cube):
    assert cube.is_inside(1.0, 1.5, 2.0)
    assert not cube.is_inside(3.0, 3.5, 5.0)

def test_cube_is_unity_cube():
    unity_cube = Cube()
    assert unity_cube.is_unity_cube() is True
def test_translate_cube(rectangle):
    rectangle.translate(2, 3)
    assert rectangle.x == 2
    assert rectangle.y == 3

def test_translate_3d_cube():
    cube = Cube()
    cube.translate(2, 3, 4)
    assert cube.x == 2
    assert cube.y == 3
    assert cube.z == 4

def test_cube_equal_sides():
    cube = Cube(width=2, height=2, depth=2)
    assert cube.is_cube() is True

def test_cube_unequal_sides():
    cube = Cube(width=2, height=3, depth=4)
    assert cube.is_cube() is False

def test_cube_zero_sides():
    with pytest.raises(ValueError):
        cube = Cube(width=0, height=0, depth=0)

def test_cube_negative_coordinates():
    cube = Cube(x=-1, y=-2, z=-3, width=2, height=3, depth=4)
    assert(cube.x == -1)

def test_cube_negative_sides():
    with pytest.raises(ValueError):
        cube = Cube(width=-2, height=-3, depth=-4)

def test_cube_greater_than_less_than():
    cube1 = Cube(width=2, height=2, depth=2)
    cube2 = Cube(width=3, height=3, depth=3)
    assert (cube1 > cube2) is False
    assert (cube1 < cube2) is True

def test_cube_constructor():
    cube = Cube(x=1, y=2, z=3, width=4, height=5, depth=6)
    assert cube.x == 1
    assert cube.y == 2
    assert cube.z == 3
    assert cube.width == 4
    assert cube.height == 5
    assert cube.depth == 6

def test_cube_assign_new_values(cube):
    # Test assigning new values for x, y, z, width, height, and depth
    cube.x = 1
    cube.y = 2
    cube.z = 3
    cube.width = 4
    cube.height = 5
    cube.depth = 6
    assert cube.x == 1
    assert cube.y == 2
    assert cube.z == 3
    assert cube.width == 4
    assert cube.height == 5
    assert cube.depth == 6

    # Test assigning negative side lengths (boundary condition)
    with pytest.raises(ValueError):
        cube.width = -1

    # Test assigning a large side length (boundary condition)
    cube.width = 1e6
    assert cube.volume == pytest.approx(3.0e7, rel=1e-2)