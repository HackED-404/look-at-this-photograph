import cv2
import numpy as np

def extract_books(image_path):
    # =============================
    # Adjustable Parameters
    # =============================
    GAUSSIAN_BLUR_KERNEL = (5, 5)  # Kernel size for Gaussian blur
    ADAPTIVE_THRESH_BLOCK_SIZE = 11  # Block size for adaptive thresholding
    ADAPTIVE_THRESH_C = 2  # Constant subtracted from mean in adaptive thresholding
    MORPH_KERNEL_SIZE = (5, 5)  # Kernel size for morphological closing
    CANNY_THRESHOLD1 = 50  # Lower threshold for Canny edge detection
    CANNY_THRESHOLD2 = 150  # Upper threshold for Canny edge detection
    HOUGH_THRESHOLD = 100  # Hough Line Transform threshold
    HOUGH_MIN_LINE_LENGTH = 100  # Minimum line length for Hough Transform
    HOUGH_MAX_LINE_GAP = 10  # Maximum gap between lines for Hough Transform
    MIN_WIDTH = 20  # Minimum width of detected book spines
    MIN_HEIGHT = 100  # Minimum height of detected book spines
    ASPECT_RATIO_THRESHOLD = 2  # Minimum height-to-width ratio for books
    
    # =============================
    # Load and Preprocess Image
    # =============================
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, GAUSSIAN_BLUR_KERNEL, 0)
    
    # Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_C)
    
    # Morphological closing to enhance book spines
    kernel = np.ones(MORPH_KERNEL_SIZE, np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Canny Edge Detection
    edges = cv2.Canny(morph, CANNY_THRESHOLD1, CANNY_THRESHOLD2)
    
    # =============================
    # Find Contours and Extract Books
    # =============================
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    book_images = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter based on aspect ratio and size
        if h > w * ASPECT_RATIO_THRESHOLD and w > MIN_WIDTH and h > MIN_HEIGHT:
            book_spine = image[y:y+h, x:x+w]  # Crop book spine
            book_images.append(book_spine)
    
    return book_images  # Return list of extracted book images
