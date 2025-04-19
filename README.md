# 🖼️ ImageEditor

A simple Python script that batch processes images by applying a **sharpening filter** and saving the edited versions as JPEGs. Built using [Pillow](https://python-pillow.org/) (the modern fork of PIL).

---

## 📂 Features

- Applies a **sharpen filter** to all images in a folder
- Converts image mode to **RGB** (to ensure JPEG compatibility)
- Saves edited images to a specified output directory
- Automatically creates the output folder if it doesn’t exist
- Skips non-image files

---

## 🛠️ Requirements

- Python 3.x
- Pillow library

### Install Pillow:
```bash
pip install Pillow
