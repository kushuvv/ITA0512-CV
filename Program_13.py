import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
height, width = image.shape[:2]
source = np.float32([[50, 50], [width - 50, 50], [50, height - 50]])
destination = np.float32([[10, 100], [width - 100, 50], [100, height - 100]])
matrix = cv2.getAffineTransform(source, destination)
transformed = cv2.warpAffine(image, matrix, (width, height))
cv2.imshow("Affine Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
