from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def removeSpecialCharacters(text):
    return re.sub(r"[^A-Za-z0-9\s]+", "", text)


def getText(image_path):
    img = Image.open(image_path)
    osd = pytesseract.image_to_osd(
        img,
        config="--psm 0 -c min_characters_to_try=5",
        output_type="dict",
    )
    rotate = osd["rotate"]
    temp = img.copy()
    rotate_single_img_fixed = temp.rotate(-rotate, expand=True)
    return pytesseract.image_to_string(rotate_single_img_fixed, config="--psm 6")
