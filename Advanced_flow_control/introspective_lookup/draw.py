"""
In this module, we refactored the using of a dict of callable to use the globals() function as it holds the reference to 
lots of functions.
"""
from refactoring_to_separate_concerns import Circle, Rectangle, Polygon, Group
from termcolor import colored
def attrs(shape):
    print(colored(f"the passed object is of type {type(shape)}!." , 'blue'))
    # in this dictionary comprehension, return the dict objects having a value ()
    attributes =' '.join(
        f'{key}="{value}"' for key, value in
        {
            "stroke": shape.stroke_color,
            "stroke-width": shape.stroke_width,
            "fill": shape.fill_color
        }.items()
        if value is not None
    )
    print(colored(f"we returned these attributes for object {shape}\n{attributes}" , color='blue'))
    return attributes

def draw_rectangle(rect):
    """This method draws a rectangle object based on custom attributes like
    point : list or a tuple
    width : int
    length : int
    other attributes of the base class 'shape'
    """
    if not isinstance(rect , Rectangle):
        raise TypeError(f"The passed object should be of type {type(Rectangle)}")
    
    xml_shape = (
        f'<rect '
        f'x="{rect.p[0]}" '
        f'y="{rect.p[1]}" '
        f'width="{rect.width}" '
        f'height="{rect.height}" '
        f'{attrs(rect)} />'
    )
    print(colored(f"Drew A RECT",color='green'))
    print(colored(xml_shape, color='green'))
    if not xml_shape :
        raise ValueError("None is return in draw_plogone")
    return xml_shape

def draw_circle(circle):
    xml_shape = (
        f'<circle '
        f'cx="{circle.center[0]}" '
        f'cy="{circle.center[1]}" '
        f'r="{circle.radius}" '
        f'{attrs(circle)} />'
    )
    print(colored(f"Drew A CIRCLE",color='green'))
    print(colored(xml_shape, color='green'))
    if not xml_shape :
        raise ValueError("None is return in draw_plogone")
    return xml_shape

def draw_polygon(polygone):
    xml_shape = '<polygon points="{points}" {attrs} />'.\
        format(
        points=" ".join(f"{p[0]} {p[1]}" for p in polygone.points),
        attrs=attrs(polygone)
        )
    print(colored(f"Drew A Polygon",color='green'))
    print(colored(xml_shape, color='green'))
    if not xml_shape :
        raise ValueError("None is return in draw_plogone")
    return xml_shape

def draw_group(group):
    print(f"trying to draw the group object {group.shapes}")
    xml_shape  = ('<g>\n{}\n</g>'.\
        format("\n".join(draw(shape) for shape in group.shapes))
    ) 

    print(colored(f"Drew A Group",color='green'))
    print(colored(xml_shape, color='green'))
    if not xml_shape :
        raise ValueError("None is return in draw_plogone")
    return xml_shape

def draw_awkward(shape):
    """
    this is an implementation of a generic draw class, but in an ugly way and it is also much 
    more difficult to maintain.
    """
    if isinstance(shape , Circle):
        draw_circle(shape)
    elif isinstance(shape , Rectangle):
        draw_rectangle(shape)
    elif isinstance(shape , Polygon):
        draw_polygon(shape)
    elif isinstance(shape , Group):
        draw_group(shape)
    else:
        raise TypeError(f"Not a know shape type {shape}!")


def draw(shape):
    shape_type = type(shape)
    name_of_function = f"draw_{type(shape).__name__.lower()}"

    print(name_of_function)

    # print(colored(f"the type of the passed shape is {type_of_shape}, while the shape is {shape}", color='red'))

    try :
        caller_reference = globals()[name_of_function]
        print(f"A successful call to {caller_reference}")
        # print(f"the reference is {caller_reference}")
    except Exception as e:
        print(colored(e,color='yellow'))
        raise TypeError(f"shape type is not supported {shape_type}!.")
    else :
        return caller_reference(shape)
    
def make_svg_document(min_x, min_y, max_x, max_y, shapes):
    print(colored(f"shapes are {shapes}",color="grey"))
    print(colored("{text}".format(text = "\n".join(str(shape) for shape in shapes)),color='grey'))
    """Make an SVG document from a collection of shapes."""
    return (
        '<svg viewBox="{min_x} {min_y} {width} {height}" xmlns="http://www.w3.org/2000/svg">'
        '\n{shapes}\n'
        '</svg>'.format(
            min_x=min_x,
            min_y=min_y,
            width=max_x - min_x,
            height=max_y - min_y,
            shapes="\n".join(draw(shape) for shape in shapes)
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