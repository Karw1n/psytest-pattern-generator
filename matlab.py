import matplotlib.pyplot as plt
import matplotlib.patches as patches

fix, ax = plt.subplots()
ax.set_aspect('equal')

width,  height = 20, 20

ax.set_xlim(0, width)
ax.set_ylim(0, height)
center = (width/2, height/2)

# Border Box
border = patches.Rectangle((0,0), width=width, height=height, edgecolor='black', fill='light_blue')
ax.add_patch(border)


# Rectangle with no fill
rect = patches.Rectangle((2, 2), width=3, height=1.5, edgecolor='blue', fill=False)
ax.add_patch(rect)

# Red Circle No Fill
circle = patches.Circle((2, 5), radius=2.5, edgecolor='red', fill=False)
ax.add_patch(circle)

plt.axis('off')

plt.show()