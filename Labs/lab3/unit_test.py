import pytest
from geometry_shapes.Circle import Circle
from geometry_shapes.Sphere import Sphere
from geometry_shapes.Rectangle import Rectangle
from geometry_shapes.Cube import Cube

my_circle = Circle()

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

# Tests for the Sphere class
def test_sphere_volume(sphere):
    assert sphere.volume == 33.510321638291124

def test_sphere_is_inside(sphere):
    assert sphere.is_inside(1.0, 1.0, 1.0)
    assert not sphere.is_inside(3.0, 3.0, 3.0)

def test_sphere_is_unity_sphere():
    sphere = Sphere()
    assert sphere.is_unity_sphere() is True

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

# Tests for the Cube class
def test_cube_volume(cube):
    assert cube.volume == 48.0

def test_cube_is_inside(cube):
    assert cube.is_inside(1.0, 1.5, 2.0)
    assert not cube.is_inside(3.0, 3.5, 5.0)

def test_cube_is_unity_cube():
    unity_cube = Cube()
    assert unity_cube.is_unity_cube() is True
