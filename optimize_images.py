import os
from PIL import Image

IMG_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images')
TARGET_SIZE = (200, 200)

for filename in os.listdir(IMG_DIR):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(IMG_DIR, filename)
        try:
            with Image.open(path) as img:
                img = img.convert('RGB')
                img = img.resize(TARGET_SIZE, Image.LANCZOS)
                img.save(path, 'JPEG', quality=85, optimize=True)
                print(f"Optimized {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}") 