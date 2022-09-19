# adapted from source: https://github.com/theacodes/phomemo_m02s/blob/main/phomemo_m02s/_image_helper.py

# Copyright (c) 2021 Alethea Katherine Flowers.
# Published under the standard MIT License.
# Full text available at: https://opensource.org/licenses/MIT

import math

import PIL
import PIL.Image


def preprocess_image(src, width=96):
    src_w, src_h = src.size
    aspect = src_w / src_h
    new_size = (width, math.floor(width / aspect))
    resized = src.resize(new_size)
    converted = PIL.ImageOps.invert(resized.convert("RGB")).convert("1")

    return converted


def split_image(image):
    chunks = image.height // 255

    for chunk in range(chunks + 1):
        i = image.crop((0, chunk * 255, image.width, chunk * 255 + 255))
        yield i


def image_to_bits(image, threshold=127):
    return [
        bytearray(
            [
                1 if image.getpixel((x, y)) > threshold else 0
                for x in range(image.width)
            ]
        )
        for y in range(image.height)
    ]
