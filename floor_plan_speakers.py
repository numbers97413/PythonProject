import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Room dimensions (in meters) for the Stue
length = 7.58  # Front-back (NE to SW wall)
width = 3.97   # Left-right (along NE wall)
height = 2.5   # Assumed ceiling height

# Define the room's vertices (8 corners of a rectangular room)
vertices = np.array([
    [0, 0, 0],        # Bottom-left-NE (0)
    [length, 0, 0],   # Bottom-right-NE (1)
    [length, width, 0],  # Bottom-right-SW (2)
    [0, width, 0],    # Bottom-left-SW (3)
    [0, 0, height],   # Top-left-NE (4)
    [length, 0, height],  # Top-right-NE (5)
    [length, width, height],  # Top-right-SW (6)
    [0, width, height]    # Top-left-SW (7)
])

# Define the edges of the room (connect vertices to form a box)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
]

# Current speaker positions (along the NE wall, facing SW, at 1 m height)
current_left_speaker = [7.08, 0.15, 1.0]  # 0.5 m from right wall
current_right_speaker = [0.5, 0.15, 1.0]  # 0.5 m from left wall

# Suggested speaker positions (0.7 m from side walls, same height)
suggested_left_speaker = [6.88, 0.15, 1.0]  # 0.7 m from right wall
suggested_right_speaker = [0.7, 0.15, 1.0]  # 0.7 m from left wall

# Listening positions
current_listening_pos = [length / 2, width * 2/3, 1.2]  # Current: 2/3 back from NE wall (y=2.65 m)
suggested_listening_pos = [length / 2, width * 1/3, 1.2]  # Suggested: 1/3 back from NE wall (y=1.32 m)

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the room edges
for edge in edges:
    x = [vertices[edge[0]][0], vertices[edge[1]][0]]
    y = [vertices[edge[0]][1], vertices[edge[1]][1]]
    z = [vertices[edge[0]][2], vertices[edge[1]][2]]
    ax.plot(x, y, z, 'b-')  # Blue lines for room edges

# Plot the current speaker positions
ax.scatter([current_left_speaker[0]], [current_left_speaker[1]], [current_left_speaker[2]], color='red', s=100, label='Current Left Speaker (x=7.08m)')
ax.scatter([current_right_speaker[0]], [current_right_speaker[1]], [current_right_speaker[2]], color='orange', s=100, label='Current Right Speaker (x=0.5m)')

# Plot the suggested speaker positions
ax.scatter([suggested_left_speaker[0]], [suggested_left_speaker[1]], [suggested_left_speaker[2]], color='darkred', s=100, label='Suggested Left Speaker (x=6.88m)', marker='^')
ax.scatter([suggested_right_speaker[0]], [suggested_right_speaker[1]], [suggested_right_speaker[2]], color='darkorange', s=100, label='Suggested Right Speaker (x=0.7m)', marker='^')

# Plot the listening positions
ax.scatter([current_listening_pos[0]], [current_listening_pos[1]], [current_listening_pos[2]], color='green', s=100, label='Current Listening Pos (y=2.65m)')
ax.scatter([suggested_listening_pos[0]], [suggested_listening_pos[1]], [suggested_listening_pos[2]], color='purple', s=100, label='Suggested Listening Pos (y=1.32m)', marker='^')

# Labels and title
ax.set_xlabel('Length (m) - NE to SW')
ax.set_ylabel('Width (m) - Along NE Wall')
ax.set_zlabel('Height (m)')
ax.set_title('3D Visualization of Stue with Suggested Speaker and Listening Positions\nDimensions: {:.2f} m x {:.2f} m x {:.2f} m'.format(length, width, height))

# Set axis limits
ax.set_xlim(0, length)
ax.set_ylim(0, width)
ax.set_zlim(0, height)

# Add legend
ax.legend()

# Show the plot
plt.show()