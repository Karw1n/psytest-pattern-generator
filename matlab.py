import matplotlib.pyplot as plt
import matplotlib.patches as patches

fix, ax = plt.subplots()
ax.set_aspect('equal')

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)


# Rectangle with no fill
rect = patches.Rectangle((2, 2), width=3, height=1.5, edgecolor='blue', fill=False)
ax.add_patch(rect)

circle = patches.Circle((2, 5), radius=2.5, edgecolor='red', fill=False)
ax.add_patch(circle)

plt.axis('on')

plt.show()