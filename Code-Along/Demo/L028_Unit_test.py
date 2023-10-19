from L027_Module import square # Names of Py files to import cannot begin with a number
# A module should in general not do anything except provide methods, i.e. no global print() etc
# Also possible from L027_Module import square
# When importing, the global code of the imported file is run
import pytest

# print(L027_Module.square(27))
# print(L027_Module.sqrt(81))

def main():
    test_positive_square()

def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25

def test_negative_square():
    assert square(-2) == 4

def test_zero_square():
    assert square(0) == 0

if(__name__ == "__main__"):
    main()

# print("start")
# try:
#     assert 1 < 0 # Throws an exception in case assertion false, used in testing
#                 # Essentially converts logical error to runtime error, which is easier to detect
# except AssertionError:
#     print("1 is not less than 0")
# print("end")