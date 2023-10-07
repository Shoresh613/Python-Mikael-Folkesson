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