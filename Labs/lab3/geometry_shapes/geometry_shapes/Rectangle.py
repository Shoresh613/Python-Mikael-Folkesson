from Common_supershape import Common_supershape
import matplotlib.patches as patches

class Rectangle(Common_supershape):
    def __init__(self, x=0, y=0, side1=1,side2=1):
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2
    
    def is_inside(self, x, y):
        if self.x - self.side1 / 2 <= x <= self.x + self.side1 / 2:
            if self.y - self.side2 / 2 <= y <= self.y + self.side2 / 2:
                return True
            else:
                return False
        else:
           return False 
    
    def is_square(self):
        return True if self.side1 == self.side2 else False

    def __repr__(self) -> str:
        return f"Rectangle({self.x, self.y, self.side1, self.side2})"

    def __str__(self) -> str:
        return super().__str__() + f": Center point: {self.x,self.y}, width: {self.side1}, height {self.side2}"

    def draw(self, ax, label=True):
        rectangle = patches.Rectangle((self.x, self.y), self.side1, self.side2, fill=False, color='red')
        y = self.y + self.side2/2 if self.side1 > 3 and self.side2 > 2 else (self.y -1.5)
        
        if label:
            ax.text(self.x+self.side1/2, y, f'x:{self.x} y: {self.y}\nw:{self.side1} h:{self.side2}', 
                    ha='center', va='center', fontsize=8, color='red')
        ax.add_patch(rectangle)

# Setters and getters beyond this point
#######################################

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        try:
            if self.is_value_ok(x):
                self._x = x 
        except ValueError as ex:
            print(ex)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        try:
            if self.is_value_ok(y):
                self._y = y
        except ValueError as ex:
            print(ex)

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, side1):
        try:
            if self.is_size_value_ok(side1):
                self._side1 = side1
        except ValueError as ex:
            print(ex)

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, side2):
        try:
            if self.is_size_value_ok(side2):
                self._side2 = side2
        except ValueError as ex:
            print(ex)

    @property
    def circumference(self):
        return 2*self.side2 + 2*self.side1
    
    @property
    def area(self):
        return self.side2 * self.side1