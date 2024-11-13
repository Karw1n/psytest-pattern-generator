import matplotlib.pyplot as plt
import matplotlib.patches as patches
from abc import ABC, abstractmethod

# Code dump
# def change_position(old_coords, new_coords):
#     if in_boundary(new_coords):
#         return new_coords

#     else:
#         # Detect direction of motion (Up, Down, Left, Right)
#         x_old, y_old = old_coords
#         x_new, y_new = new_coords 
#         x_change, y_change = ((x_new - x_old), (y_new - y_old))

#         # If it goes up we need to move it right
#         if (x_change == 0 and y_change > 0):

# def check_direction(old_coords, new_cords):  
#     # If it goes up and over border then must move right

#     # If it goes down and under border then must move left

#     # If it goes far left must move up

#     # If it goes far gith then must move down

#     # Need to consider if it goes up and right, it would go down and left



# def in_boundary(coords):
#     x , y = coords
#     if x <= width/2 and x >= -width/2 and y <= height/2 and y >= -height/2:
#         return True
#     else:
#         return False

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

    

