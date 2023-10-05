# Packages consist of not only one file, e.g. matplotlib

import math

# If __name__ is __main__, run main, if not only import functionality
def main():
    print(f"{square(2) = }")
    print(f"{square(3) = }")
    print(f"{square(-3) = }")
    print(f"{square(0) = }")
    print(f"{square(1.2) = }")

def square(n):
    return n*n

def sqrt(n):
    return math.sqrt(n)

# If the function is run directly __name__ is "__main__"
# If the module is imported it is the name of the module

# print(__name__)

# Standard check
if(__name__ == "__main__"):
    main()