import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shape import Shape, Circle, Rectangle

width, height = 20, 20
bottom_left_corner_coord = (-width/2, -height/2) 
corner_coords = [(-width/2, height/2), (width/2, height/2), (width/2, -height/2), (-width/2, -height/2)]

# 
fig, axs = plt.subplots(1, 5, figsize=(10, 10))


for ax in axs.flat:
    ax.set_aspect('equal')
    
    ax.set_xlim(-width/2, width/2)
    ax.set_ylim(-height/2, height/2)
    
    # Set the image border
    border = patches.Rectangle((corner_coords[3]), width=width, height=height, edgecolor='black', fill='light_blue')
    ax.add_patch(border)

    # Test
    middle_circle = Circle((0, 0), 5, 'yellow', True) 
    ax.add_patch(middle_circle.get_patch())

    #ax.axis('off')
   



# Create the first image of the pattern
for i in range (4):
    circle = patches.Circle((corner_coords[i % 4]),  radius=2, color='red')
    (axs.flat[i]).add_patch(circle)



# Incremently apply the rule


plt.tight_layout()
plt.show()

