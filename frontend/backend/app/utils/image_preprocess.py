from PIL import Image
import numpy as np
import os


def preprocess_image(image_path: str, target_size: tuple = (640, 640)) -> np.ndarray:
    """
    Preprocessing gambar sebelum masuk ke model YOLOv8.
    - Resize ke 640x640 (standar YOLOv8)
    - Normalisasi pixel ke range 0-1
    - Convert ke RGB kalau RGBA/grayscale
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File tidak ditemukan: {image_path}")

    img = Image.open(image_path)

    if img.mode != "RGB":
        img = img.convert("RGB")

    img = img.resize(target_size, Image.LANCZOS)

    img_array = np.array(img) / 255.0

    return img_array


def validate_image(image_path: str) -> bool:
    try:
        img = Image.open(image_path)
        img.verify()
        return True
    except Exception:
        return False


def get_image_info(image_path: str) -> dict:
    img = Image.open(image_path)
    return {
        "width": img.width,
        "height": img.height,
        "mode": img.mode,
        "format": img.format,
        "size_kb": round(os.path.getsize(image_path) / 1024, 2)
    } 
