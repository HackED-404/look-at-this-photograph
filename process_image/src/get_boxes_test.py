import cv2
import os
from get_boxes import extract_books  # Import the function

# Set the folder containing the images
IMAGE_FOLDER = "src/handpicked_test_images"

# Get a list of all image files in the folder (only jpg, png, etc.)
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

if not image_files:
    print(f"No images found in {IMAGE_FOLDER}")
    exit()

# Loop through each image and process it
for image_file in image_files:
    image_path = os.path.join(IMAGE_FOLDER, image_file)
    
    # Get extracted book bounding boxes
    book_boxes, _ = extract_books(image_path)  # Only get bounding boxes, ignore book_images

    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"❌ Could not load image: {image_path}")
        continue

    # Draw bounding boxes on the image
    for (x, y, w, h) in book_boxes:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the detected books with bounding boxes
    cv2.imshow(f"Detected Books - {image_file}", image)
    cv2.waitKey(0)  # Wait for user to close each image before proceeding

cv2.destroyAllWindows()

