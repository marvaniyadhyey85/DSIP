import cv2
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms
import os

# Set the folder to the Colab content directory
folder = '/content/'

image_paths = [
os.path.join(folder, "2 and Image.jpg"),
os.path.join(folder, "image 4.png"),
os.path.join(folder, "image 5.png"),
os.path.join(folder, "imgae 3.jpg")
]


reference_path = os.path.join(folder, "Screenshot 2026-07-13 123124.png")


# Read reference image
reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)



if reference is None:
    print("Reference image not found:", reference_path)
    exit()

for i, path in enumerate(image_paths):


    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)


    if image is None:
        print("Image not found:", path)
        continue

# Histogram Equalization
    equalized = cv2.equalizeHist(image)


# Histogram Matching
    matched = match_histograms(
image, reference,
channel_axis=None
)


    matched = matched.astype('uint8')




# Display
    plt.figure(figsize=(15, 4))


    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")


    plt.subplot(1, 3, 2)
    plt.imshow(equalized, cmap='gray')
    plt.title("Histogram Equalization")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(matched, cmap='gray')
    plt.title("Histogram Matching")
    plt.axis("off")


    plt.suptitle("Image " + str(i + 1))
    plt.show()

# Save results



    cv2.imwrite(
os.path.join(folder, f"image{i+1}_equalized.jpg"), equalized
)


    cv2.imwrite(
os.path.join(folder, f"image{i+1}_matched.jpg"), matched
)