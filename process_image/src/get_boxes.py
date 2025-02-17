import cv2
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Process_image directory
PARAMS_FILE = os.path.join(BASE_DIR, "best_params_default.json")

def load_best_params():
    """Load best parameters from JSON file if available."""
    try:
        with open(PARAMS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("No best parameters found. Please run the optimization script.")

def resize_image(image, target_width=800):
    """Rescale the image while maintaining aspect ratio."""
    h, w = image.shape[:2]
    scale = target_width / w
    resized = cv2.resize(image, (target_width, int(h * scale)), interpolation=cv2.INTER_AREA)
    return resized, scale

def preprocess_image(image):
    """Apply contrast enhancement and edge detection."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # **Contrast Enhancement using CLAHE**
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    # **Apply Gaussian Blur**
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # **Adaptive Thresholding with Otsu's Method**
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # **Morphological Closing to Connect Edges**
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return gray, morph

def adaptive_canny(gray):
    """Apply adaptive Canny edge detection based on image statistics."""
    median_intensity = np.median(gray)
    lower_threshold = int(max(0, 0.7 * median_intensity))
    upper_threshold = int(min(255, 1.3 * median_intensity))
    return cv2.Canny(gray, lower_threshold, upper_threshold)

def extract_books(image_path, **kwargs):
    """Detect book spines from an image using standard image processing techniques."""

    # Load best parameters if none are provided
    best_params = load_best_params() if not kwargs else kwargs

    MIN_WIDTH = best_params["MIN_WIDTH"]
    MIN_HEIGHT = best_params["MIN_HEIGHT"]
    ASPECT_RATIO_THRESHOLD = best_params["ASPECT_RATIO_THRESHOLD"]

    # Load and preprocess the image
    image = cv2.imread(image_path)
    resized_image, scale = resize_image(image)  # Normalize size
    gray, morph = preprocess_image(resized_image)

    # **Adaptive Canny Edge Detection**
    edges = adaptive_canny(morph)

    # **Find contours and filter based on size**
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    book_coords = []  # List of bounding boxes
    book_images = []  # List of cropped book images

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Scale bounding box back to original size
        x, y, w, h = int(x / scale), int(y / scale), int(w / scale), int(h / scale)

        # Filter based on aspect ratio and size
        if h > w * ASPECT_RATIO_THRESHOLD and w > MIN_WIDTH and h > MIN_HEIGHT:
            book_coords.append((x, y, w, h))  # Store bounding box coordinates
            book_spine = image[y:y+h, x:x+w]  # Crop book spine
            book_images.append(book_spine)  # Store the cropped book image

    # **New Filtering Step: Keep Only Taller Rectangles**
    if book_coords:
        # Sort book rectangles by height in descending order
        book_coords.sort(key=lambda rect: rect[3], reverse=True)  # Sort by h (height)

        # Compute 66th percentile height
        heights = [h for _, _, _, h in book_coords]
        height_threshold = np.percentile(heights, 66)

        # Filter out rectangles shorter than the threshold
        filtered_books = [(x, y, w, h) for (x, y, w, h) in book_coords if h >= height_threshold]
        filtered_images = [book_images[i] for i, (x, y, w, h) in enumerate(book_coords) if h >= height_threshold]

        return filtered_books, filtered_images

    return [], []  # Return empty lists if no books found
