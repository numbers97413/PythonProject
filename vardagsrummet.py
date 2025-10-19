import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Room dimensions (in meters)
length = 4.15  # From 41.325 Hz room mode
width = 3.0    # Assumed
height = 2.5   # Assumed

# Define the room's vertices (8 corners of a rectangular room)
vertices = np.array([
    [0, 0, 0],        # Bottom-left-front (0)
    [length, 0, 0],   # Bottom-right-front (1)
    [length, width, 0],  # Bottom-right-back (2)
    [0, width, 0],    # Bottom-left-back (3)
    [0, 0, height],   # Top-left-front (4)
    [length, 0, height],  # Top-right-front (5)
    [length, width, height],  # Top-right-back (6)
    [0, width, height]    # Top-left-back (7)
])

# Define the edges of the room (connect vertices to form a box)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
]

# Speaker positions (approximate, assuming Forte A5s are along the front wall)
# Left speaker: 0.5 m from left wall, 0.15 m from front wall (per manual), 0 m height (on floor)
# Right speaker: 0.5 m from right wall, 0.15 m from front wall, 0 m height
left_speaker = [0.5, 0.15, 0]  # (x, y, z)
right_speaker = [length - 0.5, 0.15, 0]

# Listening position (approximate, centered, 1/3 from back wall, 1.2 m height for seated ear level)
listening_pos = [length / 2, width * 2/3, 1.2]

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the room edges
for edge in edges:
    x = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y = [vertices[edge[0]][1], vertices[edge[1]][1]]
    z = [vertices[edge[0]][2], vertices[edge[1]][2]]
    ax.plot(x, y, z, 'b-')  # Blue lines for room edges

# Plot the speakers
ax.scatter([left_speaker[0]], [left_speaker[1]], [left_speaker[2]], color='red', s=100, label='Left Speaker')
ax.scatter([right_speaker[0]], [right_speaker[1]], [right_speaker[2]], color='orange', s=100, label='Right Speaker')

# Plot the listening position
ax.scatter([listening_pos[0]], [listening_pos[1]], [listening_pos[2]], color='green', s=100, label='Listening Position')

# Labels and title
ax.set_xlabel('Length (m)')
ax.set_ylabel('Width (m)')
ax.set_zlabel('Height (m)')
ax.set_title('3D Visualization of Listening Room\nDimensions: {:.2f} m x {:.2f} m x {:.2f} m'.format(length, width, height))

# Set axis limits
ax.set_xlim(0, length)
ax.set_ylim(0, width)
ax.set_zlim(0, height)

# Add legend
ax.legend()

# Show the plot
plt.show()