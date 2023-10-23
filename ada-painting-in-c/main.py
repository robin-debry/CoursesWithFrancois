from PIL import Image
from time import time

def convert_rgb_rgb24(r: int, g: int, b: int) -> int:
    return r << 16 | g << 8 | b

def convert_rgb24_rgb(color: int) -> tuple[int, int, int]:
    return (color >> 16, (color >> 8) & 0xFF, color & 0xFF)

def convert_rgb24_rgb12(color: int) -> int:
    return ((color >> 12) & 0xF00) | ((color >> 8) & 0xF0) | ((color >> 4) & 0xF)

SIZE_DECIMAL_FIXED = 8

def convert_float_fixed(x: float) -> int:
    return int(x * (1 << SIZE_DECIMAL_FIXED))

def convert_fixed_float(x: int) -> float:
    return x / (1 << SIZE_DECIMAL_FIXED)

def fixed_sum(a: int, b: int) -> int:
    return a + b

def fixed_mul(a: int, b: int) -> int:
    return (a * b) >> SIZE_DECIMAL_FIXED

def merge_rgb24(color1: int, color2: int) -> int:
    return (
        (((color1 >> 1) + (color2 >> 1)) & 0xFF0000) |
        ((((color1 & 0x00FF00) + (color2 & 0x00FF00)) >> 1) & 0x00FF00) |
        ((((color1 & 0x0000FF) + (color2 & 0x0000FF)) >> 1) & 0x0000FF)
    )

def luminance(img: Image.Image) -> Image.Image:
    start = time()
    img2 = Image.new("L", img.size)
    # img3 = Image.new("L", img.size)
    for y in range(img.height):
        for x in range(img.width):
            rgb = img.getpixel((x, y))
            factors = (0.2126, 0.7152, 0.0722)
            luminance_fixed = 0
            # luminance = 0
            for component, factor in zip(rgb, factors):
                component_fixed, factor_fixed = convert_float_fixed(component), convert_float_fixed(factor)
                luminance_fixed = fixed_sum(luminance_fixed , fixed_mul(component_fixed, factor_fixed))
                # luminance += component * factor
            img2.putpixel((x, y), int(convert_fixed_float(luminance_fixed)))
            # img3.putpixel((x, y), int(luminance))
    # return img2, img3
    print(time()-start)