from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def removeSpecialCharacters(text):
    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)
    return text.replace("\n", " ")


def getText(numpy_image_array):
    img = Image.fromarray(numpy_image_array)

    try:
        osd = pytesseract.image_to_osd(
            img,
            config="--psm 0 -c min_characters_to_try=5",
            output_type="dict",
        )
    except pytesseract.TesseractError as e:
        print(f"Error: {e}")
        return ""

    rotate = osd["rotate"]
    temp = img.copy()
    rotate_single_img_fixed = temp.rotate(-rotate, expand=True)
    try:
        return pytesseract.image_to_string(rotate_single_img_fixed, config="--psm 12")
    except pytesseract.TesseractError as e:
        print(f"Error extracting text: {e}")
