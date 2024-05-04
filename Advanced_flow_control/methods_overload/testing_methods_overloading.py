from functools import singledispatch

def intersect_with_rectangle():
    print("A rectangle intersect with another rectangle")
def intersect_with_circle():
    print("A rectangle intersect with a circle")
def intersect_with_polygon():
    print("A rectangle intersect with another polygon.")

# this is an abstract class.
class Shape():

    def __init__(self, *, stroke_color=None, fill_color=None, stroke_width=None):
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.fill_color = fill_color

class Circle(Shape):

    def __init__(self, center, radius, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.radius = radius

class Polygon(Shape):

    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points
class Rectangle(Shape) : 
    def __init__(self, p, width, height, **kwargs):
        super().__init__(**kwargs)
        self.p = p
        self.width = width
        self.height = height
    
    @singledispatch
    def intersect(self,shape):
        print (f"A rectangle can not intersect with this object {type(shape).__name__}")
    
    @intersect.register(Circle)
    def _(self, shape):
        return intersect_with_circle(shape) 
    @intersect.register(Polygon)
    def _(self, shape):
        return intersect_with_polygon(shape) 

# here we check our logic

poly = Polygon([100, 120 , 150 , 30 , 80])
circle = Circle((0,0) , 80)

rect = Rectangle((0,0) , 500 , 100)

rect.intersect(poly)
rect.intersect(circle)

