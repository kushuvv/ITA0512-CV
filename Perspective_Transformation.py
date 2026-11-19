import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
height, width = image.shape[:2]
source = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
destination = np.float32([[50, 50], [width - 50, 0], [0, height - 50], [width - 1, height - 1]])
matrix = cv2.getPerspectiveTransform(source, destination)
transformed = cv2.warpPerspective(image, matrix, (width, height))
cv2.imshow("Perspective Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
