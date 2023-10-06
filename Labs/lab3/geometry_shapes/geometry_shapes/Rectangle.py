import Common_supershape

class Rectangle(Common_supershape):
    def __init__(self, x=0, y=0, side1=1,side2=1):
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2
    
    def is_inside(self, x, y):
        if self.x <= x <= self.side_1 + self.side1:
            if self.y <= y <= self.side_2 + self.side1:
                return True
        else:
           return False 
    
    def is_square(self):
        return True if self.side1 == self.side2 else False