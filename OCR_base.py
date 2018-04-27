try:
    import Image, ImageEnhance
except ImportError:
    from PIL import Image, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract\\tesseract'

img = Image.open('Jordan.png')
img.load()


tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract"'

# Simple image to string
print(pytesseract.image_to_string(img))