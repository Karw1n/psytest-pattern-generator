import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, axs = plt.subplots(2, 3, figsize=(5, 5))

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
    


# Incremently apply the rule





plt.tight_layout()
plt.show()

