try:
    import Image, ImageEnhance
except ImportError:
    from PIL import Image, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract\\tesseract'

img = Image.open('Jordan.png')
img.load()

def change_contrast(img, level):

    factor = (259 * (level+255)) / (255 * (259-level))
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = img.getpixel((x, y))
            new_color = tuple(int(factor * (c-128) + 128) for c in color)
            img.putpixel((x, y), new_color)

    return img

def post_smooth(image):
    try:
        import ImageFilter
    except ImportError:
        from PIL import ImageFilter
    return image.filter(ImageFilter.SMOOTH)


# img = ImageEnhance.Contrast(img)
# img = img.enhance(2)

# img = img.convert('L')

# img = img.convert('1', dither=Image.NONE)

img = change_contrast(img, 30)
img = post_smooth(img)
img = change_contrast(img, 20)

img.save("Jordan_contrast.png")

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract"'

# Simple image to string
print(pytesseract.image_to_string(img))