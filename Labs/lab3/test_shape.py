import pytest
from geometry_shapes.Shape import Shape

class TestShape:

    def test_is_value_ok_int(self):
        shape = Shape()
        assert shape._is_value_ok(5) is True

    def test_is_value_ok_float(self):
        shape = Shape()
        assert shape._is_value_ok(5.5) is True

    def test_is_value_ok_invalid(self):
        shape = Shape()
        with pytest.raises(ValueError):
            shape._is_value_ok("string")

    def test_is_size_value_ok_int(self):
        shape = Shape()
        assert shape._is_size_value_ok(5) is True

    def test_is_size_value_ok_float(self):
        shape = Shape()
        assert shape._is_size_value_ok(5.5) is True

    def test_is_size_value_ok_invalid(self):
        shape = Shape()
        with pytest.raises(ValueError):
            shape._is_size_value_ok(-5)