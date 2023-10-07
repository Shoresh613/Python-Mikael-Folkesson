class Common_supershape:
    def __init__(self, x=0, y=0, side1=0, side2=0 ) -> None:
        self.area = 0
        self.circumference = 0
        self.x = 0
        self.y = 0

    def translate(self,x,y):
        self.x = self.x+x
        self.y = self.y+y

    def is_inside(self, x,y):
        pass

    def draw(self):
        pass

    def is_value_ok(self, value):
        if type(value) == int or type(value) == float:
            return True
        else:
            raise ValueError(f"Value '{value}' must be an integer or a float entered as (a) digit(s).")
