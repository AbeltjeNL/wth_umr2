#!/usr/bin/env python3
"""
Convert WTH logo to optimal format for Home Assistant display.
Creates icon@2x.png (256x256) which Home Assistant can display.
"""

from PIL import Image
import os

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, 'custom_components', 'wth_umr2', 'logo.png')
icon_path = os.path.join(script_dir, 'custom_components', 'wth_umr2', 'icon@2x.png')

# Open and resize
img = Image.open(logo_path)

# Convert to RGBA if needed
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Resize to 256x256 (Home Assistant preferred size)
img_resized = img.resize((256, 256), Image.Resampling.LANCZOS)

# Save
img_resized.save(icon_path, 'PNG', optimize=True)

print(f"Created {icon_path}")
print(f"Size: 256x256 pixels")
