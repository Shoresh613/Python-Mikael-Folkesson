import pytest
from geometry_shapes.Circle import Circle
from geometry_shapes.Sphere import Sphere
from geometry_shapes.Rectangle import Rectangle
from geometry_shapes.Cube import Cube

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
class TestCircle:

    def test_circle_constructor(self):
        circle = Circle(x=1, y=2, radius=3)
        assert circle.x == 1
        assert circle.y == 2
        assert circle.radius == 3

    def test_circle_area(self):
        circle = Circle(radius=2)
        assert circle.area == 12.566370614359172

    def test_circle_circumference(self):
        circle = Circle(radius=3)
        assert circle.circumference == 18.84955592153876

    def test_circle_is_inside(self):
        circle = Circle(x=2, y=3, radius=4)
        assert circle.is_inside(2, 3) is True

    def test_circle_is_not_inside(self):
        circle = Circle(x=2, y=3, radius=4)
        assert circle.is_inside(6, 7) is False

    def test_circle_gt(self):
        circle1 = Circle(radius=2)
        circle2 = Circle(radius=3)
        
        print(f"Circle 1: {circle1.area}")
        print(f"Circle 2: {circle2.area}")

        assert (circle1 > circle2) is False

    def test_circle_lt(self):
        circle1 = Circle(radius=2)
        circle2 = Circle(radius=3)
        assert (circle1 < circle2) is True

class TestSphere:

    def test_sphere_constructor(self):
        sphere = Sphere(x=1, y=2, z=3, radius=4)
        assert sphere.x == 1
        assert sphere.y == 2
        assert sphere.z == 3
        assert sphere.radius == 4

    def test_sphere_volume(self):
        sphere = Sphere(radius=3)
        assert sphere.volume - 113.09733552923255 < 0.00001

    # Add more Sphere tests as needed

class TestRectangle:

    def test_rectangle_constructor(self):
        rectangle = Rectangle(x=1, y=2, side1=3, side2=4)
        assert rectangle.x == 1
        assert rectangle.y == 2
        assert rectangle.side1 == 3
        assert rectangle.side2 == 4

    # Add Rectangle tests as needed

class TestCube:

    def test_cube_constructor(self):
        cube = Cube(x=1, y=2, z=3, width=4, height=5, depth=6)
        assert cube.x == 1
        assert cube.y == 2
        assert cube.z == 3
        assert cube.width == 4
        assert cube.height == 5
        assert cube.depth == 6

    # Add Cube tests as needed
