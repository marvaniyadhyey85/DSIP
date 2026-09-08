import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_smoothing_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def apply_sharpening_filter(image):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    return cv2.filter2D(image, -1, kernel)

base_dir = os.path.dirname(os.path.abspath(__file__))
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

image_candidates = []
for file_name in sorted(os.listdir(base_dir)):
    file_path = os.path.join(base_dir, file_name)
    if os.path.isfile(file_path) and file_name.lower().endswith(image_extensions):
        image_candidates.append(file_path)

if not image_candidates:
    print("Error: No image file found in the current directory.")
    raise SystemExit

image_path = image_candidates[0]
input_image = cv2.imread(image_path)

if input_image is None:
    print(f"Error: Unable to read image: {image_path}")
    raise SystemExit

smoothed_image = apply_smoothing_filter(
    input_image,
    kernel_size=5
)

sharpened_image = apply_sharpening_filter(
    input_image
)

input_rgb = cv2.cvtColor(
    input_image,
    cv2.COLOR_BGR2RGB
)

smoothed_rgb = cv2.cvtColor(
    smoothed_image,
    cv2.COLOR_BGR2RGB
)

sharpened_rgb = cv2.cvtColor(
    sharpened_image,
    cv2.COLOR_BGR2RGB
)


plt.figure(figsize=(15, 5))

# Original
plt.subplot(1, 3, 1)
plt.imshow(input_rgb)
plt.title("Original Image")
plt.axis("off")

# Smoothed
plt.subplot(1, 3, 2)
plt.imshow(smoothed_rgb)
plt.title("Smoothed Image")
plt.axis("off")

# Sharpened
plt.subplot(1, 3, 3)
plt.imshow(sharpened_rgb)
plt.title("Sharpened Image")
plt.axis("off")

# Adjust spacing
plt.tight_layout()

# Show output
plt.show()

cv2.imwrite(
    os.path.join(base_dir, "smoothed_image.jpg"),
    smoothed_image
)

cv2.imwrite(
    os.path.join(base_dir, "sharpened_image.jpg"),
    sharpened_image
)

print(f"Smoothed image saved as: {os.path.join(base_dir, 'smoothed_image.jpg')}")
print(f"Sharpened image saved as: {os.path.join(base_dir, 'sharpened_image.jpg')}")