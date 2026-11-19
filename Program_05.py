import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
colors = ("b", "g", "r")
for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
plt.xlim([0, 256])
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.title("Color Histogram")
plt.show()
