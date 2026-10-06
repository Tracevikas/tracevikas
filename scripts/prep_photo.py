"""Prepare a portrait for ASCII conversion: remove background, boost contrast, flatten on white.

usage: python scripts/prep_photo.py path/to/photo.jpg
writes source-prepped.png in the repo root. rembg/opencv are optional;
without them the photo is only cropped, greyscaled and auto-contrasted.
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "source-prepped.png"


def remove_background(img):
    try:
        from rembg import remove
    except ImportError:
        print("rembg not installed - keeping original background")
        return img
    return remove(img)


def boost_contrast(grey):
    try:
        import cv2
        import numpy as np
    except ImportError:
        return ImageOps.autocontrast(grey, cutoff=1)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    return Image.fromarray(clahe.apply(np.array(grey)))


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    img = ImageOps.exif_transpose(Image.open(sys.argv[1])).convert("RGBA")

    # square-ish crop centred on the upper part of the frame (where the face usually is)
    w, h = img.size
    side = min(w, h)
    top = max(0, int((h - side) * 0.25))
    img = img.crop(((w - side) // 2, top, (w - side) // 2 + side, top + side))
    img.thumbnail((800, 800))

    cut = remove_background(img)
    white = Image.new("RGBA", cut.size, (255, 255, 255, 255))
    flat = Image.alpha_composite(white, cut.convert("RGBA")).convert("L")
    boost_contrast(flat).save(OUT)
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
