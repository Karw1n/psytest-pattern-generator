import matplotlib.pyplot as plt
import matplotlib.patches as patches
from abc import ABC, abstractmethod

def in_boundary(coords, width, height):
    x , y = coords
    if x <= width/2 and x >= -width/2 and y <= height/2 and y >= -height/2:
        return True
    else:
        return False
    
def check_direction(old_coords, new_coords):
    old_x, old_y = old_coords
    new_x, new_y = new_coords

    dx = new_x - old_x
    dy = new_y - old_y

    # North
    if dx == 0 and dy > 0:
        return "North"

    # North East


    # East

    # South East

    # South

    # South West

    # North West

class Shape(ABC):
    def __init__(self, coords, color, fill):
        self._coords = coords
        self._color = color
        self._fill = fill

    def get_coords(self):
        return self._coords
    
    def set_coords(self, coords):
        self._coords = coords

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color

    def get_fill(self):
        return self._fill
    
    def set_fill(self, fill):
        self._fill = fill

class Circle(Shape):
    def __init__(self, coords, radius, color, fill):
        super().__init__(coords, color, fill)
        self._radius = radius
        self._patch = patches.Circle((coords), radius=radius, color=color, fill=fill)

    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius

    def get_patch(self):
        self.update_patch()
        return self._patch
    
    def set_patch(self, patch):
        self._patch = patch
    
    def update_patch(self):
        self._patch = patches.Circle((self._coords), radius=self._radius, color=self._color, fill=self._fill)

# Can also be a squre
class Rectangle(Shape):
    def __init__(self, coords, width, height, color, fill):
        super().__init__(coords, color, fill)
        self._width = width
        self._height = height
        self._patch = patches.Rectangle((coords), width=width, height=height, color=color, fill=fill)    

    def get_width(self):
        return self._width
    
    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height

    def get_patch(self):
        self.update_patch()
        return self._patch
    
    def set_patch(self, patch):
        self._patch = patch
    
    def update_patch(self):
        self._patch = patches.Rectangle((self._coords), width=self._width, height=self._height, color=self._color, fill=self._fill)    


