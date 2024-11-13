import matplotlib.pyplot as plt
import matplotlib.patches as patches


# 
fig, axs = plt.subplots(1, 4, figsize=(10, 10))

width, height = 10, 10
for ax in axs.flat:
    ax.set_aspect('equal')
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    
    # Set the image border
    border = patches.Rectangle((0,0), width=width, height=height, edgecolor='black', fill='light_blue')
    ax.add_patch(border)
    ax.axis('off')

    
    
# Create the first image of the pattern
for i in range (3):
    circle = patches.Circle((2.5, 7.5),  radius=1, color='red')
    (axs.flat[i]).add_patch(circle)


# Incremently apply the rule





plt.tight_layout()
plt.show()

