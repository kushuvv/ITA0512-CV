import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Original", image)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
