import cv2
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Process_image directory
PARAMS_FILE = os.path.join(BASE_DIR, "best_params.json")

def load_best_params():
    """ Load best parameters from JSON file if available. """
    try:
        with open(PARAMS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise("No best parameters found. Please run the optimization script.")


def extract_books(image_path, **kwargs):
    # Load best parameters if none are provided
    best_params = load_best_params() if not kwargs else kwargs

    GAUSSIAN_BLUR_KERNEL = tuple(best_params["GAUSSIAN_BLUR_KERNEL"])
    ADAPTIVE_THRESH_BLOCK_SIZE = best_params["ADAPTIVE_THRESH_BLOCK_SIZE"]
    ADAPTIVE_THRESH_C = best_params["ADAPTIVE_THRESH_C"]
    CANNY_THRESHOLD1 = best_params["CANNY_THRESHOLD1"]
    CANNY_THRESHOLD2 = best_params["CANNY_THRESHOLD2"]
    MIN_WIDTH = best_params["MIN_WIDTH"]
    MIN_HEIGHT = best_params["MIN_HEIGHT"]
    ASPECT_RATIO_THRESHOLD = best_params["ASPECT_RATIO_THRESHOLD"]

    # Load and preprocess the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, GAUSSIAN_BLUR_KERNEL, 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_C
    )
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    edges = cv2.Canny(morph, CANNY_THRESHOLD1, CANNY_THRESHOLD2)

    # Find contours and extract book coordinates
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    book_coords = []  # List of bounding boxes
    book_images = []  # List of cropped book images

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Filter based on aspect ratio and size
        if h > w * ASPECT_RATIO_THRESHOLD and w > MIN_WIDTH and h > MIN_HEIGHT:
            book_coords.append((x, y, w, h))  # Store bounding box coordinates
            book_spine = image[y:y+h, x:x+w]  # Crop book spine
            book_images.append(book_spine)  # Store the cropped book image

    return book_coords, book_images  # Always return both lists
