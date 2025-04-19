from PIL import Image, ImageEnhance, ImageFilter
import os

path = r'C:\Users\Jeevan\Pictures\Saved Pictures'
pathOut = r'C:\Users\Jeevan\Pictures\Edited'

os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(path, filename)
        img = Image.open(img_path)

        edit = img.filter(ImageFilter.SHARPEN)

        clean_name = os.path.splitext(filename)[0]

        # Convert to RGB if image has transparency
        edit = edit.convert("RGB")

        save_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")
        edit.save(save_path)

        print(f"Saved: {save_path}")
