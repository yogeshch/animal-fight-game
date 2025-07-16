import os
import urllib.request
from PIL import Image
from io import BytesIO

# Only missing animals with new URLs
animals = {
    'lion': 'https://images.unsplash.com/photo-1518717758536-85ae29035b6d?fit=crop&w=150&h=150',
    'zebra': 'https://images.unsplash.com/photo-1463453091185-61582044d556?fit=crop&w=150&h=150',
}

os.makedirs('Images', exist_ok=True)

for animal, url in animals.items():
    try:
        print(f"Downloading {animal}...")
        response = urllib.request.urlopen(url)
        img_data = response.read()
        img = Image.open(BytesIO(img_data)).convert('RGB')
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        img.save(os.path.join('Images', f'{animal}.jpg'))
        print(f"Saved {animal}.jpg")
    except Exception as e:
        print(f"Failed to download {animal}: {e}")

print("Lion and zebra downloads complete. Check the Images folder.") 