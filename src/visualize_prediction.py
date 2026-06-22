import glob
import random
import cv2
import matplotlib.pyplot as plt

# Path of output images
image_paths = glob.glob("../demo/*.jpg")

# Checking if we have an image or not
if len(image_paths) == 0:
    print("No images found in predict folder!")
else:
    # Random selection
    img_path = random.choice(image_paths)

    # Reading the image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # show
    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    plt.axis("off")
    plt.title("Random Prediction Result")
    plt.show()

    print("img_path:", img_path)
