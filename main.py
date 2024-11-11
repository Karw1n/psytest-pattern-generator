import math
from PIL import Image, ImageDraw



# Image dimensions
width, height = 200, 200
center_x, center_y = width // 2, height // 2

# Image Canvas
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

radius = 10


# Top Left Circle (Circle 1)
# Bounding box for circle
c1_top_left = (0, 0)
c1_bottom_right = (center_x/2, center_y/2)
# Draw shape
draw.ellipse([c1_top_left, c1_bottom_right], fill="black")


# Top Right circle (Circle 2)
c2_top_left = (center_x, 0)
c2_bottom_right = (width, center_y)
draw.ellipse([c2_top_left, c2_bottom_right], fill="black")

# Bottom Left Circle (Circle 3)
c3_top_left = (0, center_y)
c3_bottom_right = (center_x, height)
draw.ellipse([c3_top_left, c3_bottom_right], fill="black")

# Bottom Right Circle (Circle 4)
c4_top_left = (center_x, center_y)
c4_bottom_right = (width, height)
draw.ellipse([c4_top_left, c4_bottom_right], fill="black")

image.show()