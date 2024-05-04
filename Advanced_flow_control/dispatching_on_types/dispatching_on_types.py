
"""what is strange here is that instructor says, the this is the way the most object oriented designs work, but it may lead to a 
a poor design because it violates the single principle design concept.

Shape classes should be all about shapeness, not about things you can do with shapes such as drawing, serializing or clipping. 
What we'd like to do is move the responsibilities which aren't intrinsic to shapes out of the Shape classes. 

"""
# this is an abstract class.
class Shape():

    def __init__(self, *, stroke_color=None, fill_color=None, stroke_width=None):
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.fill_color = fill_color

    def attrs(self):
        # in this dictionary comprehension, return the dict objects having a value ()
        attrs =' '.join(
            f'{key}="{value}"' for key, value in
            {
                "stroke": self.stroke_color,
                "stroke-width": self.stroke_width,
                "fill": self.fill_color
            }.items()
            if value is not None
        )
        return attrs


class Rectangle(Shape):
    # any rectangle has a starting point and a width and a height.
    def __init__(self, p, width, height, **kwargs):
        super().__init__(**kwargs)
        self.p = p
        self.width = width
        self.height = height

    def draw(self):
        xml_shape = (
            f'<rect '
            f'x="{self.p[0]}" '
            f'y="{self.p[1]}" '
            f'width="{self.width}" '
            f'height="{self.height}" '
            f'{self.attrs()} />'
        )
        print(xml_shape)
        return xml_shape


class Circle(Shape):

    def __init__(self, center, radius, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.radius = radius

    def draw(self):
        xml_shape = (
            f'<circle '
            f'cx="{self.center[0]}" '
            f'cy="{self.center[1]}" '
            f'r="{self.radius}" '
            f'{self.attrs()} />'
        )
        print(xml_shape)
        return xml_shape
    


class Polygon(Shape):

    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def draw(self):
        xml_shape = '<polygon points="{points}" {attrs} />'.\
            format(
            points=" ".join(f"{p[0]} {p[1]}" for p in self.points),
            attrs=self.attrs()
            )
        print(xml_shape)
        return xml_shape
        
 
# If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.
class Group:

    def __init__(self, shapes):
        self.shapes = shapes

    def draw(self):
        """this method returns a group of xml shapes"""
        return (
            '<g>\n{}\n</g>'.format(
                "\n".join(shape.draw() for shape in self.shapes)
            )
        )


def make_svg_document(min_x, min_y, max_x, max_y, shapes):
    """Make an SVG document from a collection of shapes."""
    return (
        '<svg viewBox="{min_x} {min_y} {width} {height}" xmlns="http://www.w3.org/2000/svg">'
        '\n{shapes}\n'
        '</svg>'.format(
            min_x=min_x,
            min_y=min_y,
            width=max_x - min_x,
            height=max_y - min_y,
            shapes="\n".join(shape.draw() for shape in shapes)
        )
    )


if __name__ == "__main__":
    outline = Polygon(points=[
            (300, 425), (580, 425), (560, 155), (510, 155),
            (500, 285), (450, 250), (450, 285), (400, 250),
            (400, 285), (350, 250), (350, 285), (300, 250),
        ],
        stroke_width=8,
        stroke_color="#2a9fbc",
        fill_color="#addbea",
    )
    left_window = Rectangle(
        p=(350, 330),
        width=50, height=40,
        stroke_width=6,
        stroke_color="#2a9fbc",
        fill_color="#ffffff",
    )
    right_window = Rectangle(
        p=(430, 330),
        width=50, height=40,
        stroke_width=6,
        stroke_color="#2a9fbc",
        fill_color="#ffffff",
    )
    smoke = Group(
        [
            Circle(center=(550, 120), radius=30, fill_color="#d8d8d8"),
            Circle(center=(600, 90), radius=40, fill_color="#d8d8d8"),
            Circle(center=(650, 60), radius=50, fill_color="#d8d8d8"),
        ]
    )
    d = make_svg_document(300, 10, 700, 425, [outline, right_window, left_window, smoke])
    with open("Advanced_flow_control/shapes.svg", "wt", encoding="utf=8") as svg_file:
        print(d, file=svg_file)

