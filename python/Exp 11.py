import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Load the image
image = cv2.imread('images.jpeg', 0)  # Load as grayscale
# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)
# Perform Erosion
erosion = cv2.erode(image, kernel, iterations=1)
# Perform Dilation
dilation = cv2.dilate(image, kernel, iterations=1)
# Perform Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# Perform Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# Display the original image and the results
cv2_imshow(image)
cv2_imshow(erosion)
cv2_imshow(dilation)
cv2_imshow(opening)
cv2_imshow(closing)
# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()


