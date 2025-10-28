#!/usr/bin/env python3
"""
Create a simple, clean India map with location markers.
"""

import matplotlib.pyplot as plt
import geopandas as gpd
import json

# Read the India GeoJSON
print("Loading India GeoJSON...")
india_gdf = gpd.read_file('india.geojson')
print(f"Loaded {len(india_gdf)} states/territories")

# Location coordinates
locations = {
    'Bengaluru, Karnataka': (77.5946, 12.9716),
    'Guwahati, Assam': (91.7362, 26.1445),
    'Imphal-East, Manipur': (93.9368, 24.8170),
    'Kasaragod, Kerala': (75.0090, 12.4996),
    'Kolkata, West Bengal': (88.3639, 22.5726),
    'Nilgiris, Tamil Nadu': (76.6950, 11.4102)
}

# Create figure to fit the right side
fig, ax = plt.subplots(1, 1, figsize=(8, 9))

# Plot India with solid teal color like the reference image
india_gdf.plot(ax=ax, 
               color='#1a5f7a',  # Solid teal/dark blue like the reference
               edgecolor='#ffffff',  # White borders
               linewidth=1.2,
               alpha=1.0)

# Note: Location markers are now handled entirely in HTML overlay for better interactivity
# This keeps the base map clean and simple

# Remove title for cleaner look
# ax.set_title('Study Locations Across India', 
#              fontsize=20, 
#              fontweight='bold', 
#              color='#2c5aa0',
#              pad=20)

# Remove axis and set proper bounds to include all of India (including Kashmir)
ax.axis('off')

# Set axis limits to include full India territory, with tighter top bound to reduce white space
ax.set_xlim(68, 98)
ax.set_ylim(6, 36)  # Reduced from 38 to 36 to cut white space at top

# Set background to match webpage (#fafafa)
fig.patch.set_facecolor('#fafafa')
ax.set_facecolor('#fafafa')

# Save with high quality
plt.tight_layout(pad=0.2)
plt.savefig('india_map.png', 
            dpi=110, 
            bbox_inches='tight',
            facecolor='#fafafa',
            edgecolor='none',
            transparent=False)

print("\n✅ India map successfully created: india_map.png")
print("(Location markers will be added as interactive HTML overlays)")
    
plt.close()

