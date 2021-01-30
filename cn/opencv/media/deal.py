import os
import traceback

# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(img, root):
    txt = Image.new('RGBA', img.size, (0, 0, 0, 0))
    fnt = ImageFont.truetype("DENG.TTF", 20)
    d = ImageDraw.Draw(txt)
    d.text((0, txt.size[1] - 30), root, font=fnt, fill=(0, 0, 0, 255))
    out = Image.alpha_composite(img, txt)
    sav = out.convert("RGB")
    sav.save(os.path.join(root, file))


if __name__ == '__main__':
    for root, dirs, files in os.walk('./pic/'):
        for file in files:
            print("------------")
            print(file)
            try:
                file_str = os.path.join(root, file)
                img = Image.open(file_str).convert('RGBA')
                add_text_to_image(img, root)
            except Exception as e:
                print(os.path.join(root, file))
                print(e)
                print(traceback.format_exc())
                pass