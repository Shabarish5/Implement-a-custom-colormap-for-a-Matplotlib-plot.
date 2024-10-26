import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap, BoundaryNorm

# Step 1: Generate Synthetic Terrain Elevation Data
# ---------------------------------------------
# Using sine function over a 2D grid to simulate radial terrain (elevation data)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Radial elevation pattern, like hills or mountains

# Plot the generated elevation data for reference
plt.figure(figsize=(8, 6))
plt.imshow(Z, cmap='viridis')  # Default colormap
plt.colorbar(label='Elevation (Synthetic Data)')
plt.title('Synthetic Elevation Data (for Reference)')
plt.show()

# Step 2: Implement Continuous Custom Colormap
# ---------------------------------------------
# Define custom continuous colormap from blue (low) -> white (mid) -> brown (high)
terrain_colors = ['#0000ff', '#ffffff', '#8B4513']  # Blue (water) -> White (snow) -> Brown (land)
custom_cmap = LinearSegmentedColormap.from_list('terrain_cmap', terrain_colors, N=256)

# Plot the data using the continuous custom colormap
plt.figure(figsize=(8, 6))
plt.imshow(Z, cmap=custom_cmap)
plt.colorbar(label='Elevation')
plt.title('Continuous Colormap for Terrain Elevation')
plt.show()

# Step 3: Implement Discrete Custom Colormap with Specific Elevation Ranges
# ---------------------------------------------
# Define discrete colors for different elevation ranges
discrete_terrain_colors = ['#0000ff', '#00ff00', '#ffff00', '#ff8c00', '#8B4513']  # Blue -> Green -> Yellow -> Orange -> Brown
discrete_cmap = ListedColormap(discrete_terrain_colors)

# Define boundaries for the discrete colormap (elevation intervals)
boundaries = [-1, -0.5, 0, 0.5, 1, 1.5]  # Elevation levels corresponding to different colors
norm = BoundaryNorm(boundaries, discrete_cmap.N, clip=True)

# Plot using the discrete colormap with specific elevation ranges
plt.figure(figsize=(8, 6))
plt.imshow(Z, cmap=discrete_cmap, norm=norm)
plt.colorbar(label='Elevation Levels', ticks=boundaries)
plt.title('Discrete Colormap for Specific Elevation Ranges')
plt.show()
