import matplotlib.pyplot as plt
class Common_supershape:
    def __init__(self) -> None:
        pass

    def translate(self,x,y):
        self.x = self.x+x
        self.y = self.y+y

    def is_inside(self, x,y):
        pass

    def draw(self):
        pass

    def _is_value_ok(self, value):
        if type(value) == int or type(value) == float:
            return True
        else:
            raise ValueError(f"Value '{value}' must be an integer or a float entered as (a) digit(s).")
    def _is_size_value_ok(self, value):
        if (type(value) == int or type(value) == float) and value > 0:
            return True
        else:
            raise ValueError(f"Value '{value}' must be a positive integer or float (>0) entered as (a) digit(s).")

    # Comparison operator overloads
    ###############################

    def __gt__(self, other):
        if not isinstance(other, Common_supershape):
            raise TypeError(f"Usupported operand type(s) for > 'Common_supershape' and {type(other)}!")
        if(self.circumference>other.circumference):
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Common_supershape):
            raise TypeError(f"Usupported operand type(s) for > 'Common_supershape' and {type(other)}!")
        if(self.circumference>other.circumference):
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, Common_supershape):
            raise TypeError(f"Usupported operand type(s) for > 'Common_supershape' and {type(other)}!")
        if(self.circumference>=other.circumference):
            return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, Common_supershape):
            raise TypeError(f"Usupported operand type(s) for > 'Common_supershape' and {type(other)}!")
        if(self.circumference>=other.circumference):
            return True
        else:
            return False