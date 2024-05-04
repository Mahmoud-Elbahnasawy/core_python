from functools import singledispatch
from termcolor import colored

def intersect_with_rectangle(shape, rectangle):
    print(colored(f"{type(shape).__name__} intersects with {type(rectangle).__name__}.",color='yellow'))
def intersect_with_circle(shape, circle):
    print(colored(f"{type(shape).__name__} intersects with {type(circle).__name__}.", color='green'))
def intersect_with_polygon(shape , polygon):
    print(colored(f"{type(shape).__name__} intersects with {type(polygon).__name__}.", color='blue'))

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
    def intersect(self, shape):
        intersect_with_rectangele(shape, self)
class Dummy(Shape):
    def __init__(self, dummy, **kwargs):
        super().__init__(**kwargs)
        self.dummy = dummy

@singledispatch
def intersect_with_rectangele(shape, rectangle):
    raise TypeError(colored(f"A rectangle can not intersect with this object '{type(shape).__name__}'.", color= 'red'))

@intersect_with_rectangele.register(Rectangle)
def _(shape,rectangle):
    return intersect_with_rectangle(shape,rectangle)   
  
@intersect_with_rectangele.register(Circle)
def _(shape, circle):
    return intersect_with_circle(shape, circle) 

@intersect_with_rectangele.register(Polygon)
def _(shape,polygon):
    return intersect_with_polygon(shape, polygon) 

# here we check our logic

poly = Polygon([100, 120 , 150 , 30 , 80])
circle = Circle((0,0) , 80)

rect = Rectangle((0,0) , 500 , 100)
rect_2 = Rectangle((1,1) , 1000 , 200)

dummy = Dummy(15)


# checking our logic using a the generic methods directly

# this should call intersect_with_rectangle method
intersect_with_rectangele(rect_2, rect)
# this should call intersect_with_circle method
intersect_with_rectangele(circle, rect)
# this should call intersect_with_polygone method
intersect_with_rectangele(poly, rect)
# this should raise a type error
try:
    intersect_with_rectangele(dummy, rect)
except Exception as e:
    print(e)
print("=>"*50)
# check our logic using the class method intersects
rect.intersect(rect_2)
rect.intersect(circle)
rect.intersect(poly)
try:
    rect.intersect(dummy)
except Exception as e:
    print(e)

