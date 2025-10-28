#!/usr/bin/env python3
"""
Generate an India map with location markers for the annotation viewer.
Requires: geopandas, matplotlib
Install: pip install geopandas matplotlib
"""

import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.patches import Circle
import numpy as np
import os

# Location coordinates
locations = {
    'Bengaluru, Karnataka': (77.5946, 12.9716),
    'Guwahati, Assam': (91.7362, 26.1445),
    'Imphal-East, Manipur': (93.9368, 24.8170),
    'Kasaragod, Kerala': (75.0090, 12.4996),
    'Kolkata, West Bengal': (88.3639, 22.5726),
    'Nilgiris, Tamil Nadu': (76.6950, 11.4102)
}

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(12, 14))
ax.set_aspect('equal')

# Try to load India shapefile
shapefile_paths = [
    r'Maps_with_python/india-polygon.shp',
    r'../Maps_with_python/india-polygon.shp',
    r'../../Maps_with_python/india-polygon.shp',
    'india-polygon.shp'
]

india_loaded = False
for fp in shapefile_paths:
    if os.path.exists(fp):
        try:
            print(f"Loading shapefile from: {fp}")
            map_df = gpd.read_file(fp)
            map_df_copy = gpd.read_file(fp)
            print(f"Shapefile loaded successfully!")
            print(f"Columns: {map_df.columns.tolist()}")
            
            # Plot India
            map_df.plot(ax=ax, color='#2c5aa0', edgecolor='#1a3a6b', linewidth=1.5, alpha=0.85)
            india_loaded = True
            break
        except Exception as e:
            print(f"Error loading from {fp}: {e}")
            continue

if not india_loaded:
    print("Could not find india-polygon.shp shapefile.")
    print("Using simplified outline instead...")
    
    # Alternative: Use a simplified polygon for India
    india_coords = np.array([
        [68, 35], [70, 34], [72, 33], [74, 32], [76, 30], [78, 28],
        [80, 26], [82, 24], [84, 23], [86, 23], [88, 24], [90, 25],
        [92, 26], [94, 27], [95, 28], [95, 30], [93, 29], [91, 28],
        [89, 27], [88, 25], [86, 24], [84, 24], [82, 25], [80, 26],
        [78, 28], [76, 30], [74, 32], [73, 33], [72, 34], [71, 34],
        [70, 33], [70, 30], [71, 28], [72, 26], [73, 24], [74, 22],
        [75, 20], [76, 18], [77, 16], [78, 14], [79, 12], [78, 10],
        [77, 9], [76, 8], [75, 8], [74, 9], [73, 10], [72, 11],
        [71, 12], [70, 13], [69, 15], [68, 17], [68, 20], [68, 23],
        [68, 26], [68, 29], [68, 32], [68, 35]
    ])
    
    ax.fill(india_coords[:, 0], india_coords[:, 1], color='#2c5aa0', 
            edgecolor='#1a3a6b', linewidth=2, alpha=0.85)

# Plot location markers
for name, (lon, lat) in locations.items():
    # Main marker
    ax.plot(lon, lat, 'o', color='#ff6b6b', markersize=12, 
            markeredgecolor='white', markeredgewidth=2, zorder=5)
    
    # Add location name
    ax.text(lon, lat + 0.8, name.split(',')[0], 
            fontsize=10, ha='center', va='bottom',
            fontweight='bold', color='#1a1a1a',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor='none', alpha=0.7))

# Set limits to India bounds
ax.set_xlim(68, 98)
ax.set_ylim(6, 38)

# Remove axes
ax.axis('off')

# Set background color
fig.patch.set_facecolor('#f5f7fa')
ax.set_facecolor('#e8f4f8')

# Add title
plt.title('Study Locations Across India', fontsize=18, fontweight='bold', 
          color='#2c5aa0', pad=20)

# Save the figure
plt.tight_layout()
plt.savefig('india_map.png', dpi=150, bbox_inches='tight', 
            facecolor='#f5f7fa', edgecolor='none')
print("India map saved as 'india_map.png'")
plt.close()

print("\nGenerated map with the following locations:")
for name in locations.keys():
    print(f"  - {name}")

