"""here we extract the drawing behaviour from our shape classes to achieve the single principle design
we will use two modules that are this one , and draw.py new module
"""

# this is an abstract class.
class Shape():

    def __init__(self, *, stroke_color=None, fill_color=None, stroke_width=None):
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.fill_color = fill_color

class Rectangle(Shape):
    # any rectangle has a starting point and a width and a height.
    def __init__(self, p, width, height, **kwargs):
        super().__init__(**kwargs)
        self.p = p
        self.width = width
        self.height = height

class Circle(Shape):

    def __init__(self, center, radius, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.radius = radius

class Polygon(Shape):

    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

        
 
# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.
class Group:

    def __init__(self, shapes):
        self.shapes = shapes








